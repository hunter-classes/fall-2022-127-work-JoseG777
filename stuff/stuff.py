d = {}
d[2] = 12345
d[5] = "hello"
d['hello'] = 'world'
d['list']=[2,3,4,5,6]
d[ (1,2) ] = 55
print(d)
d['list']  = 55.3
print(d)

person = {'fist' : "John",
          'last' : "Smith",
          'age' : 50,
          'height' : 60}
person['age'] = person['age'] + 1

print(person)

k = person.keys()
print(k)
for item in k:
    print('person[',item,'] = ',person[item])

# convert the dict_keys thing into a list:
klist = [x for x in person.keys()]
print(klist)

# pull out the values and convert to list
vlist = [x for x in person.values()]
print(vlist)

