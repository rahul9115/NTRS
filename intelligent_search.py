import pickle
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
with open("19830024525_cleaned_10.pickle","rb") as f:
    final_cleaned_data1=pickle.load(f)
text=' '.join(final_cleaned_data1)
word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis("off")
plt.show()