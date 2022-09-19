import pdfplumber
from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig


with pdfplumber.open(r'19830024525.pdf') as pdf:
  l=len(pdf.pages)
  summary=[]
  text=[]
  for i in range(l):
    extracted_page =pdf.pages[i] 
    extracted_text = extracted_page.extract_text()
    text.append(extracted_text)
print(len(text))
extracted_text=' '.join(text)
  
model = BartForConditionalGeneration.from_pretrained('sshleifer/distilbart-cnn-12-6')
tokenizer = BartTokenizer.from_pretrained('sshleifer/distilbart-cnn-12-6')

inputs = tokenizer([extracted_text], truncation=True, return_tensors='pt')

# Generate Summary
summary_ids = model.generate(inputs['input_ids'], num_beams=4, early_stopping=True, min_length=0, max_length=int(len(pdf.pages)/4))
summarized_text = ([tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in summary_ids])

summary.append(summarized_text)
print(summary)