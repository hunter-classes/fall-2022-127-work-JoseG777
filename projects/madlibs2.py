import random

VERBS = ["DESTROY", "FIGHT", "WALK", "RUN"]
NOUNS = ["PUPPY", "DRAGON", "APPLE", "ORANGE"]
HERO = ["Jose", "Ace", "Zero"]

s1 = open('story.dat')
s2 = s1.read()

def dh(H, V, N):
  H1 = random.choice(H)
  s3 = s2.replace("<HERO>", H1)
  s4 = s3.split()
  for i in s4:
    if i == '<VERB>':
      i1 = s4.index(i)
      s4.pop(i1)
      s4.insert(i1, random.choice(V))
  for i in s4:
    if i == '<NOUN>':
      i1 = s4.index(i)
      s4.pop(i1)
      s4.insert(i1, random.choice(N))
  s5 = ' '.join(s4)
  return s5

def cap():
  s7 = dh(HERO, VERBS, NOUNS)
  s8 = s7.split()
  s7 = s7.lower()
  for i in s8:
    t1 = s8.index(".")
    for i in s7:
      if s7.index(i) == t1 + 1:
        s7[s7.index(i)].capitalize
        s8.pop(t1)
  
  return t1
  

print(cap())