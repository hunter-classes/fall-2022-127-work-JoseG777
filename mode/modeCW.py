list = [44, 32, 32, 33, 34, 56, 76, 766, 22, 22, 22, 22, 22, 22, 22, 22]
def mode(list):
    fv = list[0]
    fvc = list.count(fv)
    biggest = list[0]
    for i in list:
        if fvc < list.count(list[list.index(i)]):
            newlargest = list.count(list[list.index(i)])
            fvc = newlargest
            biggest = i
    return biggest
print(mode(list))


