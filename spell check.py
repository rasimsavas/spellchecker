#RASIM SAVAS


import difflib
import csv
from collections import Counter
import re

kelimeler = []
kelimes = []
with open("dataa.csv",encoding='utf-8-sig') as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        kelimeler.append(line)
        #print ('line[{}] = {}'.format(i, line))

with open('kelime-listesi.txt','r+',encoding='utf-8-sig') as d:
    for i in kelimeler:
        i = str(i).replace("[","")
        i = str(i).replace("]","")
        i = str(i).replace("'","")
        i = str(i).replace("-","")
        if i.isnumeric == True:
            continue
        else:
            d.writelines(str(i)+"\n")

with open('kelime-listesi.txt','r+',encoding='utf-8-sig') as txt:
    for i in txt:
        kelimes.append(i)
def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('kelime-listesi.txt').read()))

def P(word, N=sum(WORDS.values())): 
    return WORDS[word] / N

def correction(word): 
    return max(candidates(word), key=P)

def candidates(word): 
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    return set(w for w in words if w in WORDS)

def edits1(word):
    letters    = 'abcçdefghıijklmnoöpqrsştuüvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))   
  
words = kelimes
#words = ['selamlar','devlet','masa','araba']

def yazim_duzelt(s):   
    for word in s.casefold().split():
        if word not in words:
            suggestion = difflib.get_close_matches(word,words)
            print(f"bunlardan birisi mi? \n-{'-'.join(str(x) for x in suggestion)}veya")
    print("*"+correction(s) +"* mi demek istediniz?")
s = input('kelime giriniz:.. ')
yazim_duzelt(s)

