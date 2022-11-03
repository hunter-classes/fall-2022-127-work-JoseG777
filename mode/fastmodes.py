#RECIEVED HELP FROM THOMAS
import random
ranlist = []
for i in range (0, 100):
  ran = random.randint(0,100)
  ranlist.append(ran)
print(ranlist)

def fmode(list):
  tallies = [0] * 100
  for i in list:
    tallies[i] += 1
  mode = max(tallies)
  mode1 = tallies.index(mode)
  return mode1

print(fmode(ranlist))