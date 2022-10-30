import random

VERBS = ["DESTROY", "FIGHT", "WALK", "RUN"]
NOUNS = ["PUPPY", "DRAGON", "APPLE", "ORANGE"]
HERO = ["Jose", "Ace", "Zero"]

s1 = open('story.dat')
s2 = s1.read()

def dh(H):
  H1 = random.choice(H)
  s3 = s2.replace("<HERO>", H1)
  return s3

s4 = dh(HERO)  

def dv(V):
  s5 = s4.split()
  for i in s5:
    if i == '<VERB>':
      i1 = s5.index(i)
      s5.pop(i1)
      s5.insert(i1, random.choice(V))
  return s5
s6 = dv(VERBS)

def dn(N):
  for i in s6:
    if i == '<NOUN>':
      i1 = s6.index(i)
      s6.pop(i1)
      s6.insert(i1, random.choice(N))
  s7 = ' '.join(s6)
  return s7

print(dn(NOUNS)) 

