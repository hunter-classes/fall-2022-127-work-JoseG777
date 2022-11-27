#1 EXTRA, MAKING DICTIONARY FORM .DAT FILE
text = open('input.txt')
text1 = text.read()
text2 = text1.lower()
text3 = text2.split()

trans = open('pirates.dat')
trans1 = trans.read()
trans2 = trans1.split()

dict = {}
for kv in trans2:
    ind = kv.find(':')
    dict.update({kv[0:ind]:kv[ind + 1:]})

text4 =[]
for word in text3:
    if word in dict.keys():
        text4.append(dict[word])
    else:
        text4.append(word)

print(" ".join(text4))
    

