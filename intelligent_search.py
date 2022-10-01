from txtai.embeddings import Embeddings
import json
embeddings = Embeddings({
    
    "path": "sentence-transformers/all-MiniLM-L6-v2"
})
with open("data/vol7.json", "r") as f:
    data = json.load(f)["descriptions"]
len(data)