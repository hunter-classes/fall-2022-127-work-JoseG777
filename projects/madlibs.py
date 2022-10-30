import random

VERBS = ["DESTROY", "FIGHT", "WALK", "RUN"]
NOUN = ["PUPPY", "DRAGON", "APPLE", "ORANGE"]
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
      i = random.choice(V)
  return s5
  
  
print(dv(VERBS)) 

