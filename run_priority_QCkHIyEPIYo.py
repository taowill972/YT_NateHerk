#!/usr/bin/env python3
import sys
import json
import time
from pathlib import Path

from config import REPO_DIR, STATE_FILE, CATALOG_FILE
from pipeline import process_single_video
from git_manager import update_readme_index, commit_and_push_repo

print("====================================================================")
print("🚀 [PRIORITY] Traitement prioritaire de la vidéo QCkHIyEPIYo via Gemini Audio")
print("====================================================================")

res = process_single_video("QCkHIyEPIYo", use_gemini_audio=True)

# Mise à jour state.json
if STATE_FILE.exists():
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)
else:
    state = {"processed_ids": [], "processed_videos": [], "known_baseline_ids": []}

if "QCkHIyEPIYo" not in state["processed_ids"]:
    state["processed_ids"].append("QCkHIyEPIYo")
state["processed_videos"].append(res)
state["completed_count"] = len(state["processed_ids"])
state["last_run_timestamp"] = time.time()

with open(STATE_FILE, "w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

# Mise à jour README
with open(CATALOG_FILE, "r", encoding="utf-8") as f:
    cat = json.load(f)

update_readme_index(state["processed_videos"], total_catalog_count=len(cat))

# Git commit & push
commit_and_push_repo(f"feat: transcription prioritaire QCkHIyEPIYo - {res.get('title_fr')[:50]}")

print("\n🎉 Traitement prioritaire de QCkHIyEPIYo terminé avec succès !")
