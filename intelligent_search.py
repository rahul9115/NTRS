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
summary_data={}
for i,j in set1.items():
    summary=j+". "+set2.get(i)
    summary_data.update({i:summary})

'''
with open("data/vol7.json", "r") as f:
    data = json.load(f)["descriptions"]
print(data)
'''
values_summary=summary_data.values()

txtai_data = []
i=0
for text in values_summary:
    txtai_data.append((i, text, None))
    i=i+1
txtai_data[0]
embeddings.index(txtai_data)
with open("embeddings.pickle","wb") as f:
    pickle.dump(embeddings,f)
res = embeddings.search("HYDRODYNAMIOCSFACCELERATEDDROPS", 10)
keys=list(summary_data.keys())
values=list(summary_data.values())
values=list()

values_summary=list(values_summary)
final_list=[]
for r in res:

    print(f"Text: {values_summary[r[0]]}")
    k=0
    m=0
    for i in values:
        
        if i==summary_data[r[0]]:
            m=k
            break
        k+=1
    final_list.append(keys[m])
    
    print(f"Similarity: {r[1]}")
    print()
    break
print(final_list)