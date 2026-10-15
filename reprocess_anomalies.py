import os
import sys
import json
import time
import subprocess
from pathlib import Path
from typing import Dict, Any, List

from config import (
    BASE_DIR,
    REPO_DIR,
    CATALOG_FILE,
    STATE_FILE,
    TRANSCRIPTS_DIR,
    SCREENSHOTS_DIR,
    WORK_DIR
)
from pipeline import process_single_video
from git_manager import update_readme_index, commit_and_push_repo

PROGRESS_FILE = BASE_DIR / "reprocess_progress.json"
ANOMALIES_FILE = BASE_DIR / "anomalies_to_reprocess.json"

def load_anomalies() -> List[Dict[str, Any]]:
    if ANOMALIES_FILE.exists():
        with open(ANOMALIES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def load_progress() -> List[str]:
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                return json.load(f).get("completed_reprocess_ids", [])
        except Exception:
            pass
    return []

def save_progress(completed_ids: List[str]):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "completed_reprocess_ids": completed_ids,
            "count": len(completed_ids),
            "last_update": time.strftime("%Y-%m-%d %H:%M:%S UTC")
        }, f, indent=2, ensure_ascii=False)

def main():
    print("====================================================================", flush=True)
    print("🚀 [Reprocess] Démarrage de la remise à niveau intégrale avec Gemini-3.5-Flash-Lite", flush=True)
    print(f"⏱️ Horodatage : {time.strftime('%Y-%m-%d %H:%M:%S UTC')}", flush=True)
    print("====================================================================", flush=True)

    anomalies = load_anomalies()
    if not anomalies:
        print("[Reprocess] Aucune anomalie répertoriée dans anomalies_to_reprocess.json", flush=True)
        return

    completed_ids = set(load_progress())
    remaining = [a for a in anomalies if a["vid_id"] not in completed_ids]

    print(f"[Reprocess] Total anomalies : {len(anomalies)} | Déjà corrigées : {len(completed_ids)} | Restantes : {len(remaining)}", flush=True)

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)

    with open(CATALOG_FILE, "r", encoding="utf-8") as f:
        catalog = json.load(f)
    cat_map = {c["id"]: c.get("title", "") for c in catalog}

    for idx, item in enumerate(remaining):
        vid_id = item["vid_id"]
        v_title = cat_map.get(vid_id, item.get("file", vid_id))
        print(f"\n[{idx+1}/{len(remaining)}] 🔄 Reprocessing vidéo : {vid_id} — {v_title}", flush=True)

        try:
            # Traitement complet avec téléchargement authentique et Gemini 3.5 Flash-Lite
            res = process_single_video(vid_id, catalog_title=v_title, use_gemini_audio=False)

            # Mettre à jour state.json (remplacement de l'ancienne entrée)
            pv_list = state.get("processed_videos", [])
            new_pv_list = [p for p in pv_list if p.get("id") != vid_id]
            new_pv_list.append(res)
            state["processed_videos"] = new_pv_list

            if vid_id not in state.get("processed_ids", []):
                state["processed_ids"].append(vid_id)
            state["completed_count"] = len(state["processed_ids"])
            state["last_run_timestamp"] = time.time()

            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(state, f, ensure_ascii=False, indent=2)

            # Mise à jour README et déploiement Git
            update_readme_index(state["processed_videos"], total_catalog_count=len(catalog))
            commit_and_push_repo(f"fix(reprocess): mise à niveau gemini-3.5-flash-lite {vid_id} - {res.get('title_fr', v_title)[:50]}")

            completed_ids.add(vid_id)
            save_progress(list(completed_ids))
            print(f"[Reprocess] ✓ Vidéo {vid_id} remise à niveau avec succès ({res.get('screenshots_count', 0)} screenshots).", flush=True)

        except Exception as e:
            print(f"[Reprocess] ❌ Erreur sur {vid_id} : {e}", flush=True)

        time.sleep(2.0)

    print("\n🏁 [Reprocess] Fin de la routine de remise à niveau !", flush=True)

if __name__ == "__main__":
    main()
