from typing import final
import pdfplumber
from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
import pickle
import gensim   
with open("19830024525_cleaned.pickle","rb") as f:
    final_cleaned_data1=pickle.load(f)
print(len(final_cleaned_data1))
extracted_text = '. '.join(final_cleaned_data1)
def textrank(corpus, ratio=0.2):    
    if type(corpus) is str:        
       corpus = [corpus]    
    lst_summaries = [gensim.summarization.summarize(txt,  
                     ratio=ratio) for txt in corpus]    
    return lst_summaries


