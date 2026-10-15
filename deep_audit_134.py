#!/usr/bin/env python3
import json
import re
from pathlib import Path

BASE_DIR = Path("/root/YT_NateHerk")
STATE_FILE = BASE_DIR / "state.json"
CATALOG_FILE = BASE_DIR / "catalog.json"
TRANSCRIPTS_DIR = BASE_DIR / "YT_NateHerk_Transcript"
SCREENSHOTS_DIR = BASE_DIR / "screenshots"

print("================================================================")
print("🔍 AUDIT COMPLET DES 134 VIDÉOS TRAITÉES DANS YT_NATEHERK")
print("================================================================")

with open(STATE_FILE, "r", encoding="utf-8") as f:
    state = json.load(f)

processed_videos = state.get("processed_videos", [])
processed_ids = state.get("processed_ids", [])

print(f"Total processed_ids: {len(processed_ids)}")
print(f"Total processed_videos entries: {len(processed_videos)}")

# Check for duplicates in processed_ids
seen_ids = set()
duplicates = []
for vid in processed_ids:
    if vid in seen_ids:
        duplicates.append(vid)
    seen_ids.add(vid)

if duplicates:
    print(f"⚠️ ATTENTION : {len(duplicates)} IDs en doublon trouvés dans processed_ids: {duplicates}")
else:
    print("✓ Aucun ID en doublon dans processed_ids.")

# Audit each video
anomalies = []
total_md_ok = 0
total_html_ok = 0
total_screenshots = 0
missing_md = []
missing_html = []
corrupt_md = []
corrupt_html = []
low_audit_score = []

required_patterns = [
    ("Synthèse Exécutive", r"##\s*.*Synth.*Ex.*cutiv"),
    ("Résumé", r"###\s*.*R.*sum"),
    ("Outils", r"###\s*.*Outils"),
    ("Points Clés", r"###\s*.*Points\s+Cl"),
    ("Chronologie", r"##\s*.*Chronologie"),
    ("Audio Verbatim", r"\*\*.*Audio.*(Transcription|Verbatim)"),
    ("Analyse Visuelle", r"\*\*.*Analyse\s+Visuelle")
]

for idx, v in enumerate(processed_videos):
    vid_id = v.get("id")
    title = v.get("title_fr") or v.get("title") or vid_id
    md_rel = v.get("md_file")
    html_rel = v.get("html_file")
    audit_score = v.get("audit_score", 0)
    audit_passed = v.get("audit_passed", False)
    sc_count = v.get("screenshots_count", 0)
    total_screenshots += sc_count

    # Check Markdown
    md_path = BASE_DIR / md_rel if md_rel else None
    if not md_path or not md_path.exists():
        # Try finding in TRANSCRIPTS_DIR
        found_mds = list(TRANSCRIPTS_DIR.glob(f"*{vid_id}*.md"))
        if found_mds:
            md_path = found_mds[0]
        else:
            missing_md.append((vid_id, title))
            anomalies.append(f"[{vid_id}] Fichier Markdown manquant")
            continue

    if md_path.stat().st_size < 1000:
        corrupt_md.append((vid_id, md_path.name, md_path.stat().st_size))
        anomalies.append(f"[{vid_id}] Markdown trop petit ({md_path.stat().st_size} bytes)")
    else:
        # Check sections
        md_text = md_path.read_text(encoding="utf-8", errors="ignore")
        missing_sec = []
        for label, pat in required_patterns:
            if not re.search(pat, md_text, re.IGNORECASE):
                missing_sec.append(label)
        if missing_sec:
            anomalies.append(f"[{vid_id}] Sections manquantes dans MD : {missing_sec}")
        else:
            total_md_ok += 1

    # Check HTML
    html_path = BASE_DIR / html_rel if html_rel else None
    if not html_path or not html_path.exists():
        found_htmls = list(TRANSCRIPTS_DIR.glob(f"*{vid_id}*.html"))
        if found_htmls:
            html_path = found_htmls[0]
        else:
            missing_html.append((vid_id, title))
            anomalies.append(f"[{vid_id}] Fichier HTML manquant")
            continue

    if html_path.stat().st_size < 2000:
        corrupt_html.append((vid_id, html_path.name, html_path.stat().st_size))
        anomalies.append(f"[{vid_id}] HTML trop petit ({html_path.stat().st_size} bytes)")
    else:
        total_html_ok += 1

    # Check audit score
    if audit_score < 98.0 or not audit_passed:
        low_audit_score.append((vid_id, audit_score))

print(f"\n📊 RÉSULTATS DU SCAN TECHNIQUE :")
print(f"- Vidéos audités : {len(processed_videos)}")
print(f"- Fichiers Markdown 100% conformes : {total_md_ok} / {len(processed_videos)}")
print(f"- Fichiers HTML 100% conformes : {total_html_ok} / {len(processed_videos)}")
print(f"- Total captures d'écran cumulées : {total_screenshots}")
print(f"- Fichiers Markdown manquants : {len(missing_md)}")
print(f"- Fichiers HTML manquants : {len(missing_html)}")
print(f"- Scores d'audit < 98% : {len(low_audit_score)}")
print(f"- Nombre total d'anomalies détectées : {len(anomalies)}")

if anomalies:
    print("\n🚨 DÉTAIL DES ANOMALIES TROUVÉES :")
    for a in anomalies[:25]:
        print("  -", a)
    if len(anomalies) > 25:
        print(f"  ... et {len(anomalies) - 25} autres anomalies.")
else:
    print("\n🎉 AUCUNE ANOMALIE DÉTECTÉE SUR LE CONTENU DES 134 VIDÉOS TRAITÉES !")

EOF
