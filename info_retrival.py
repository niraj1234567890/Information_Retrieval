import spacy
import textacy
import bs4 as bs
import urllib.request
import re

#read and parse webpage:
before_parse=urllib.request.urlopen(r'https://en.wikipedia.org/wiki/Delhi').read()
parsed=bs.BeautifulSoup(before_parse,'lxml')

#read paragraphs:

para=[]
for p in parsed.find_all('p'):
    para.append(p.text)

#preprocessing of text:
paragraph=[]
for p in range(0,len(para)):
    Re=re.sub('[+[\d{1-4}]+]','',para[p])
    Re=re.sub('[^a-zA-Z0-9.,]',' ',Re)
    paragraph.append(Re)

#prepare a document:
info=' '.join(paragraph)

#load english model:

nlp=spacy.load('en_core_web_md')

#apply this model to our document:

doc=nlp(info)

#apply textacy model for information retrival:
statements=textacy.extract.semistructured_statements(doc,"Delhi")
print('Delhi is:')

for statement in statements:
    subject,verb,fact=statement
    print(fact)


statements=textacy.extract.semistructured_statements(doc,"Delhi",cue='have')

print('Delhi has:')
for statement in statements:
    subject,verb,fact=statement
    print(fact)
















    
