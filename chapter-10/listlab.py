list = [23 ,43, 44, 95, 10, 29, 11, 24, 34]
list1 = [15, 16, 29, 10, 38, 43, 34, 76, 13]
str1ng = "Just an example for the lab assignment stuff"
list11 = str1ng.split()
samlist = ["word", "words", "more", "sam", "even", "odd"]

def n1(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

print(n1(list))

def n2(list):
    odd = []
    for i in list:
        if i % 2 != 0:
            odd.append(i)
    return odd

print(n2(list))

def n3(x):
    c = " "
    c = x.title()
    return c

print(n3(str1ng))

def n4(x):
    str1ng.lower()
    list5 = str1ng.split()
    list6 = []
    for i in list5:
        l1 = list5.index(i)
        if len(list5[l1]) > 5:
            l2 = i.capitalize()
            list6.insert(l1, l2)
        else:
            list6.insert(l1, i)
    list7 = ' '.join (list6)
    return list7

print(n4(str1ng))

def n5(list):
    list8 = []
    for i in list:
        l3 = i * i
        list8.append(l3)
    return list8

print(n5(list))

def n6(list):
    listA = [x + y for x, y in zip(list, list1)]
    return listA

print(n6(list))

#10
def n10(x):
    l4 = 0
    for i in list11:
        l44 = list11.index(i)
        if l44 == 5:
            l4 = l4 + 1
    return l4

print(n10(str1ng))

#11
def n11(list):
    total = 0
    i = 0
    while list[i] % 2 != 0 and i < len(list):
        total = total + list[i]
        i = i + 1
    return total

print(n11(list))

#12
def n12(samlist):
    var = 0
    l12 = samlist.index("sam")
    del samlist[l12 + 1:]
    for i in samlist:
        var = var + 1
    return var

print(n12(samlist))





    
