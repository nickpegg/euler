num1 = 1
num2 = 1
count = 2

while len(str(num2)) < 1000:
  count += 1
  
  tmp = num2
  num2 += num1
  num1 = tmp

print "Length:",len(str(num2))
print "Term:",count
print "Number:",num2
