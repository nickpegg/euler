s = 0
go = 1
num1 = 0
num2 = 1

while go:
  #If number is even, add it to the sum
  if num2 % 2 == 0:
    s += num2
  
  #Fibbonaci sequence GOOOOOO
  temp = num2
  num2 += num1
  num1 = temp
  
  #Are we still under 1000000?
  if num2 >= 1000000:
    go = 0
    
print 'Answer: '
print s
