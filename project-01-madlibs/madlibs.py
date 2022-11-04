#2 EXTRAS, STORY PULLED & READ FROM FILE + UNIQUE REPLACEMENTS THAT STAY CONSTANT
import random

VERBS = ["DESTROY", "FIGHT", "WALK", "RUN"]
NOUNS = ["PUPPY", "DRAGON", "APPLE", "ORANGE"]
HERO = ["Jose", "Ace", "Zero"]

s1 = open('story.dat') #Story pulled & read from file
s2 = s1.read()

def dh(H, V, N):
  H1 = random.choice(H)
  s3 = s2.replace("<HERO>", H1) # Unique replacement. Remains constant
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

print(dh(HERO,VERBS,NOUNS))