#!/usr/bin/python

# What is the smallest number that is evenly divisible by all of the numbers 
# from 1 to 20?

i = 20  #Starting value

while 1:
  good = 1
  for j in range(1, 21):
    if i % j != 0:
      good = 0
      break
  if good == 1:
    print "Answer:",i
    break
    
  if i % 10000000 == 0:
    print i
  i += 20
