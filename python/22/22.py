f=open("names.txt", "r")
namestring=f.readline()
names=namestring.split(',')

total=0

for i in range(len(names)):
  names[i] = names[i].strip('"')

names.sort()

for i in range(len(names)):
  name = names[i]
  score = 0
#  for letter in name:
#    
  total += score
