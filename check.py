import pickle
with open("final_ids.pickle","rb") as f:
        set1=pickle.load(f)
        count=0
        for i in set1:
            try:
                int(i)
                count+=1
                print(i)
            except:
                continue
print(count)


