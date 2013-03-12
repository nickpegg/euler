#!/usr/bin/python

#Find the sum of all the primes below one million.

def isprime(num):
  i = 2
  while i < num:
    if num % i == 0:
      return 0
    i += 1
  return 1
  

s = 2
i = 3

while i <= 1000000:
  if isprime(i):
    s += i    
  if i % 1005 == 0:
    print i, s
  i += 2
    
print "Answer:",s
