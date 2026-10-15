import json
import time
import sys
from pathlib import Path

sys.path.insert(0, "/root/YT_NateHerk")

from pipeline import process_single_video
from git_manager import update_readme_index, commit_and_push_repo
from config import STATE_FILE, CATALOG_FILE

vid_id = "J-6pnl5DQg8"
print(f"Testing single video processing for {vid_id} with updated config...")
res = process_single_video(vid_id, use_gemini_audio=False)

with open(STATE_FILE, "r", encoding="utf-8") as f:
    state = json.load(f)

if vid_id not in state["processed_ids"]:
    state["processed_ids"].append(vid_id)
state["processed_videos"].append(res)
state["completed_count"] = len(state["processed_ids"])
state["last_run_timestamp"] = time.time()

with open(STATE_FILE, "w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

with open(CATALOG_FILE, "r", encoding="utf-8") as f:
    cat = json.load(f)

update_readme_index(state["processed_videos"], total_catalog_count=len(cat))
commit_and_push_repo(f"feat: transcription {vid_id} - {res.get('title_fr')[:50]}")
print("TEST_FINISHED_SUCCESS")
