import requests
import json
import os
from datetime import datetime

minute = int(datetime.now().strftime("%M"))
num = minute + 1
if num > 60:
    num = 1

url = f"https://jsonplaceholder.typicode.com/todos/{num}"
res = requests.get(url).json()

file_path = "data/chaerin_test.json"

os.makedirs("data", exist_ok=True)

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except:
            data = []
else:
    data = []

data.append(res)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Saved todo {num}")
