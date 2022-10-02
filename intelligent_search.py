from txtai.embeddings import Embeddings
import json
import pickle
embeddings = Embeddings({
    
    "path": "sentence-transformers/all-MiniLM-L6-v2"
})
with open("final_all_short_summary2.pickle","rb") as f:
    set1=pickle.load(f)

with open("final_conclusion_summary2.pickle","rb") as f1:
    set2=pickle.load(f1)
summary_data=[]
for i,j in set1.items():
    summary=j+". "+set2.get(i)
    summary_data.append(summary)
'''
with open("data/vol7.json", "r") as f:
    data = json.load(f)["descriptions"]
print(data)
'''

txtai_data = []
i=0
for text in summary_data:
    txtai_data.append((i, text, None))
    i=i+1
txtai_data[0]
embeddings.index(txtai_data)
with open("embeddings.pickle","wb") as f:
    pickle.dump(embeddings,f)
res = embeddings.search("CII line dominant FIR emission line Galaxy primary coolant", 10)
for r in res:
    print(f"Text: {summary_data[r[0]]}")
    print(f"Similarity: {r[1]}")
    print()
    break