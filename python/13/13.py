f = open('data')
s = 0

for line in f:
  s += int(line)
  
print str(s)[:10]
