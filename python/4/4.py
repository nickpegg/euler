#!/usr/bin/python

def ispalindrome(string):
  string = str(string)
  length = len(string)
  
  if length % 2 == 0:
    front = string[0:length/2]
    back = string[length/2:length]
    back = back[::-1] #reverse the back half
    
    if front == back:
      return 1
    else:
      return 0
  else:
    front = string[0:length/2]
    back = string[length/2+1:length]
    back = back[::-1] #reverse the back half

    if front == back:
      return 1
    else:
      return 0    


largest = 0

for i in range(100,1000):
  for j in range(100,1000):
    num = i*j

    if ispalindrome(num):
      if num > largest:
        largest = num

print "Answer:",largest
