import os
import json
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# Find clinic_info.json dynamically regardless of execution depth
current_dir = os.path.dirname(os.path.abspath(__file__))
possible_paths = [
    os.path.join(current_dir, "..", "data", "clinic_info.json"),
    os.path.join(current_dir, "..", "..", "data", "clinic_info.json")
]

json_path = None
for path in possible_paths:
    if os.path.exists(path):
        json_path = path
        break

if not json_path:
    raise FileNotFoundError("Could not locate data/clinic_info.json in project root.")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)