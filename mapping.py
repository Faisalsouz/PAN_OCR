import spacy as sp
from pprint import pprint
import os
from spacy import displacy
from IPython.core.display import display
from spacy.matcher import Matcher
file=open(os.path.join(r'C:\Users\fkhalil\primeStone\docrecog\converterText\Nachtragsangebot Nr 2.pdf.txt'),'r',encoding='utf-8').read()
# print(type(file))
line=file.split('Seite')
import re
text= line[3]
print(text)


# print(len(line)) #line, 2,3,4 is pos mange
# for page in line:
#     con='Pos' and 'Mange'and'Beschreibung'
#     total_pages= len(line)
#     count=1
#     if con in page: #'Pos' and 'Mange' and 'Beschreibung'
#         count=+1
#         print('possible pos page',count)
#         print()
#
#
#
#     else:
#         count=+1
#         print('not sure')
##########################################################################

# nlp = sp.load('en_core_web_sm')
#
# # # Initialize the matcher with the shared vocab
# matcher = Matcher(nlp.vocab)
# #
# # Add the pattern to the matcher
# pattern = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]
# matcher.add('IPHONE_PATTERN', None, pattern)
#
# # Process some text
# doc = nlp("New iPhone X release date leaked")
#
# # Call the matcher on the doc
# matches = matcher(doc)
# print(matches)


##############################################################

#########################################
# doc = nlp("New iPhone X release date leaked")
# matches = matcher(doc)
#
# # Iterate over the matches
# for match_id, start, end in matches:
#     # Get the matched span
#     matched_span = doc[start:end]
#     print(matched_span.text)


################################################


# pprint(line[2])
# print(line[3])
nlp= sp.load('de_core_news_sm')
nlp1=sp.load('en')
page= nlp(line[3])
text=' 2.this is an example of simple text that contais spaces 14      \n newlines with some \n onother newline \n this  EU 233,00 and $222 London is very beautiful city'
# doc=nlp1(text)
# pat= re.search(r'\d(.*?)\d',line[3],re.M)
# print(pat.group())
# print(line[3])
# sent= page.sents
# for i in sent:
#     print(i)
    # regex=re.findall(r'\d',i)
    # print(regex)
# matcher = Matcher(nlp1.vocab)
# pattern=[{'REGEX' : '\d'},{'lower':'city'}]
# matcher.add('cnt',None, pattern)
# search=matcher(doc)
# #
# for match_id, start, end in search:
#     # Get the matched span
#     matched_span = doc[start:end]
#     print(matched_span.text)

# for words in doc.ents:
#     print(words.text,words.label_)


# for i in page:
#     b=i.like_num
#     if b is True:
#         print(i.i)

# print([toc.i for toc in doc])




# span= doc[1:3]
# print(span.text)
# for chunk in page.noun_chunks:
    # print(chunk.text, chunk.root.text, chunk.root.dep_,
    #       chunk.root.head.text)

# print([token.text for token in page])
# sent= list(page.sents)
# print(sent)
# for ent in page.ents:
#     print(ent.text, ent.label_)
#     if ent.label_=='MISC':
#         print(ent.text)
# print(page)
# dis=displacy.render(page, style='ent', jupyter=True)
# display(dis)
# print(page)