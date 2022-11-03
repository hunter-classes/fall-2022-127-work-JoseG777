
#WILL CONTINUE TO WORK ON THIS
list = [44, 44, 44, 44, 44, 32, 32, 33, 34, 56, 76, 766, 33, 33, 33, 33, 33, 33, 33, 33, 33 ,33]
def mode(list):
    first = 0
    start = list[first]
    largest = list.count(start)
    biggest = list[first]
    for i in list:
        if largest < list.count(list[first + 1]):
            newlargest = list.count(list[first + 1])
            largest = newlargest
            biggest = i
    return biggest
print(mode(list))


