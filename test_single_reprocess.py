
import sys
sys.path.insert(0, '/root/YT_NateHerk')

from pipeline import process_single_video
from git_manager import update_readme_index, commit_and_push_repo
from config import STATE_FILE, CATALOG_FILE
import json

vid_id = "saxdE-U_YS8"
print(f"=== TESTING CLEAN REPROCESS FOR {vid_id} ===", flush=True)

res = process_single_video(vid_id, use_gemini_audio=False)
print(f"Result: {res}", flush=True)

with open(STATE_FILE, 'r', encoding='utf-8') as f:
    state = json.load(f)

pv_list = [p for p in state.get('processed_videos', []) if p.get('id') != vid_id]
pv_list.append(res)
state['processed_videos'] = pv_list

with open(STATE_FILE, 'w', encoding='utf-8') as f:
    json.dump(state, f, indent=2, ensure_ascii=False)

with open(CATALOG_FILE, 'r', encoding='utf-8') as f:
    cat = json.load(f)

update_readme_index(state['processed_videos'], total_catalog_count=len(cat))
commit_and_push_repo(f"fix(reprocess): vraie transcription authentique {vid_id} - {res.get('title_fr')[:45]}")
print("=== SUCCESSFUL REPROCESS COMPLETED ===", flush=True)
