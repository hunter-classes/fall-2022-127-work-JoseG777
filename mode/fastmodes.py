#RECIEVED HELP FROM THOMAS
#Will continue to work on this
import random
def buildRandomList(size,maxvalue):
    result = [random.randrange(maxvalue) for x in range(size)]
    return result 

def testFastModes(size, maxvalue):
  dataset = buildRandomList(size, maxvalue)
  result = fmodes(dataset)
  print(dataset)
  print(result)

def fmodes(list):
  largest = max(list)
  tallies = [0] * 100
  for i in list:
    tallies[i] += 1
  largest = max(tallies)
  mode = tallies.index(max)
  return mode
print(fmodes(testFastModes(100, 100)))
