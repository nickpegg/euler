#!/usr/bin/python

def isprime(num):
  i = 2
  while i < num:
    if num % i == 0:
      return 0
    i += 1
  return 1
  
  
count = 1
num = 3

while count < 10001:
  if isprime(num):
    count += 1
    print count,":",num
  if num > 2:
    num += 2
