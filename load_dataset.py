from datasets import load_dataset
import json

# טעינה ב-Streaming ללא הורדת כל ה-673GB
ds = load_dataset("HuggingFaceFW/fineweb-edu", name="sample-10BT", split="train", streaming=True)

target_file = "fineweb_edu_3gb.jsonl"
max_samples = 600000  # קובע נפח של כ-2.5GB עד 3GB על הדיסק

print("Downloading subset...")
with open(target_file, "w", encoding="utf-8") as f:
    for i, sample in enumerate(ds):
        if i >= max_samples:
            break
        f.write(json.dumps({"text": sample["text"]}) + "\n")

print("Done! File saved locally.")