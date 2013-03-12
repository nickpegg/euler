def fact(x): return (1 if x==0 else x * fact(x-1))

num = fact(100)
num = str(num)

s = 0

for i in range(len(num)):
  s += int(num[i])
print "Answer:",s
