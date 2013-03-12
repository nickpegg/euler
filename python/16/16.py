meganum = 2 ** 1000

num = str(meganum)
answer = 0

for i in range(len(num)):
  answer = answer + int(num[i])
print "Answer:",answer
