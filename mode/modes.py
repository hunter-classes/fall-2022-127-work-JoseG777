list = [43, 42, 44, 43, 43, 56, 54, 55, 1, 11, 11, 43]

def findLargest(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest
print(findLargest(list))

def findSmallest(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest
print(findSmallest(list))

def freq(list):
    num = int(input("What number would you like to find?"))
    total = 0
    for i in list:
        if num == i:
            total = total + 1
    return total
print (freq(list))

