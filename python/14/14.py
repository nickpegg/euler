#!/usr/bin/python

def iseven(num):
  return num % 2 == 0

maxcount = 0
startnum = 0
count = 0
num = 0 
i = 0

for i in range(1, 1000001):
  count = 0
  num = i
  
  while i != 1:
    if iseven(i):
      i = i / 2
    else:
      i = 3*i + 1
    count += 1
    
  if count > maxcount:
    print "New Max:",count,"@",num
    maxcount = count
    startnum = num
    
print "Answer:",startnum
