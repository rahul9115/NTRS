from typing import final
import pdfplumber
from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
import pickle
import gensim 
import nltk  
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow.keras import callbacks, models, layers, preprocessing as kprocessing
with open("19830024525_cleaned.pickle","rb") as f:
    final_cleaned_data1=pickle.load(f)
extracted_text = ' '.join(final_cleaned_data1)
lst_tokens = nltk.tokenize.word_tokenize(extracted_text)
ngrams = [1]

bigrams=list(nltk.bigrams(lst_tokens))
d={}
for i in bigrams:
    d[i]=d.get(i,0)+1

## calculate
dtf_freq = pd.DataFrame()
for n in ngrams:
    dic_words_freq = nltk.FreqDist(nltk.ngrams(lst_tokens, n))
    dtf_n = pd.DataFrame(dic_words_freq.most_common(), columns=
                            ["word","freq"])
    dtf_n["ngrams"] = n
    dtf_freq = dtf_freq.append(dtf_n)
    dtf_freq["word"] = dtf_freq["word"].apply(lambda x: " ".join(string for string in x) )
    dtf_freq_X= dtf_freq.sort_values(["ngrams","freq"], ascending=
                            [True,False])
    thres = 5 #<-- min frequency
    X_top_words = len(dtf_freq_X[dtf_freq_X["freq"]>thres])
    
    lst_corpus = extracted_text
    ## tokenize text
    tokenizer = kprocessing.text.Tokenizer(num_words=X_top_words, lower=False, split=' ', oov_token=None, 
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n')
    tokenizer.fit_on_texts(lst_corpus)
    dic_vocabulary = {"<PAD>":0}
    dic_vocabulary.update(tokenizer.word_index)
    ## create sequence
    lst_text2seq= tokenizer.texts_to_sequences(lst_corpus)
    ## padding sequence
    X_train = kprocessing.sequence.pad_sequences(lst_text2seq, 
                        maxlen=15, padding="post", truncating="post")
    
    
## plot
df1=pd.DataFrame(columns=["Bigrams","Freq"])
df1["Bigrams"]=d.keys()
df1["Freq"]=d.values()

'''
sns.barplot(x="freq", y="word", hue="ngrams", dodge=False,
 data=dtf_freq.groupby('ngrams')["ngrams","freq","word"].head(30))
plt.show()
'''
df1=df1.sort_values(by="Freq",ascending=False)
sns.barplot(x="Freq", y="Bigrams", dodge=False,hue="Bigrams",data=df1.head(10))
plt.show()

