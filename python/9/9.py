#!/usr/bin/python

a=0
b=0
c=0
count = 0

for a in range (999):
  for b in range(1000):
    for c in range(1001):
      if a**2 + b**2 == c**2:
        if (a+b+c) == 1000:
          if a<b<c:
            print "Set: {",a,",",b,",",c,"}"
            print "Answer:",a*b*c
            break
            break
            break
