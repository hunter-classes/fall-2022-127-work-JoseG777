#Q4
numlist = [32, 64, 16, 2, 4, 8]

def average(numlist):

    tv = 0
    for num in numlist:
        tv = tv  + num

    return tv / len(numlist)
print(average(numlist))

#Q6
list = [2, 3, 4]
def sum_of_squares(xs):
    sum = 0
    for number in xs:
        sum = sum + (number * number) 
    
    return sum

print(sum_of_squares(list))