import random

for counter in range(5):
  print(counter)

loop_counter = 0
while random.randrange(0,100) < 80:
  print ("hello", loop_counter)
  loop_counter= loop_counter + 1
print("The above loop ran this many times:", loop_counter)

s = "hello world"
for i in range(len(s)):
  print(s[i])
  