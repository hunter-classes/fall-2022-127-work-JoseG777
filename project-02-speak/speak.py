text = open('input.txt')
text1 = text.read()
text2 = text1.lower()
text3 = text2.split()

dict = {'of': "o'", 'buddy':'matey', 'before':'afore', 'guys':'scurvey dogs', 'hero':'pirate', "and":"an'"}

text4 =[]
for word in text3:
    if word in dict.keys():
        text4.append(dict[word])
    else:
        text4.append(word)

print(" ".join(text4))
    

