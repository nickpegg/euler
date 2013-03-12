#!/usr/bin/python

def isprime(num):
  print "Is", num, "prime?"
  i = 2
  while i < num:
    if num % i == 0:
      print "No."
      return 0
    i += 1
  print "Yes."
  return 1

  
meganum = 317584931803

#Find all the factors of 317584931803
factors = []
#i = 2        #initial value
i = 62500000  #resuming work
answer = 0

maxnum = meganum/2

while i <= maxnum:
  if meganum % i == 0:
    if isprime(meganum / i):
      answer = meganum / i
      break
  if i % 1000000 == 0:
    print i
  i += 1
  
print "LOL DONE!"
print answer
