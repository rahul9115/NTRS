import PyPDF2
pdffileobj=open("19830024525.pdf","rb")
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
completed=0
for i in range(0,x):
    try:
        pageobj=pdfreader.getPage(i)
        text=pageobj.extractText()
        print(i)
        
        with open("19830024525.txt","a",encoding='utf-8') as f:
            
            f.write(str(text))
    except Exception as e:
        print(e)
        print(text)
        break