#1 EXTRA, GRAPHING
import pandas as pd
import matplotlib.pyplot as plot

data1 = open('cereal.csv')
data2 = pd.read_csv(data1)
data3 = data2.to_string()

sugarL = []
nameL = []
data4 = {}

for sugars in data2['sugars']:
    sugarL.append(sugars)
for name in data2['name']:
    nameL.append(name)
pH = 0
for item in nameL:
    data4.update({nameL[pH]:sugarL[pH]})
    pH = pH + 1

def average(list):
    tv = 0
    for num in list:
        tv = tv  + num
    return tv / len(list)

smallest = sugarL[0]
indS = 0
for i in sugarL:
    if i < smallest:
        smallest = i
        indS = sugarL.index(i)

plot.figure(figsize = (77, 30)) #GRAPHING BRAND NAMES WITH THEIR TOTAL AMOUNT OF SUGAR
plot.bar(data4.keys(), data4.values(), width = 1)
plot.xlabel('Brand Names')
plot.ylabel('Sugar')
plot.show() 

print('The average amount of sugar across the 77 brands was', average(sugarL),'grams. The brand with the least amount of sugar was', nameL[indS],'with', smallest,'grams.')
