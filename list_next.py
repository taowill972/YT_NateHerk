#!/usr/bin/env python3
import json

with open("/root/YT_NateHerk/catalog.json") as f:
    cat = json.load(f)
with open("/root/YT_NateHerk/state.json") as f:
    st = json.load(f)

p_ids = set(st.get("processed_ids", []))
cat_sorted = sorted(cat, key=lambda x: x.get("upload_date", ""), reverse=True)
unprocessed = [v for v in cat_sorted if v["id"] not in p_ids]
print(f"Total remaining unprocessed: {len(unprocessed)}")
for i, v in enumerate(unprocessed[:7]):
    print(f" {i+1}. {v['id']} | {v.get('upload_date')} | {v.get('title')}")
