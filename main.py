from re import search
import PyPDF2
file=open("E:/vs python/PDF/AccountStatement.pdf","rb")
reader = PyPDF2.PdfFileReader(file)

for i in range(reader.numPages):
    page=reader.getPage(i)
    #print(page.extractText())
search_Keywords=['ACCOUNT NUMBER','ACCOUNT TYPE']

for sentence in search_Keywords:
    lst = []
    for word in search_Keywords:
        if word in sentence:
            lst.append(word)
    print('{0} key word(s) in sentence: {1}'.format(len(lst),','.join(lst)))
    print(sentence + "\n")