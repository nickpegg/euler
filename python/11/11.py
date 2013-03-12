#!/usr/bin/python

file = open('data')
grid = []
answer = 0

for line in file:
  line = line.rstrip()
  grid.append(line.split(' '))
  
#Convert strings into ints
for row in range(len(grid)):
  for col in range(len(grid[row])):
    grid[row][col] = int(grid[row][col])

for row in range(len(grid)):
  for col in range(len(grid[row])):
    #Check east
    if col + 3 < len(grid[row]):
      product = grid[row][col]*grid[row][col+1]*grid[row][col+2]*grid[row][col+3]
      if product > answer:
        answer = product
        
    #Cehck south
    if row + 3 < len(grid):
      product = grid[row][col]*grid[row+1][col]*grid[row+2][col]*grid[row+3][col]
      if product > answer:
        answer = product
        
    #Check southeast
    if row + 3 < len(grid) and col + 3 < len (grid[row]):
      product = grid[row][col]*grid[row+1][col+1]*grid[row+2][col+2]*grid[row+3][col+3]
      if product > answer:
        answer = product
    
    #Check southwest
    if row + 3 < len(grid) and col - 3 > 0:
      product = grid[row][col]*grid[row+1][col-1]*grid[row+2][col-2]*grid[row+3][col-3]
      if product > answer:
        answer = product
        
    #Check northeast
    if row - 3 > 0 and col + 3 < len(grid[row]):
      product = grid[row][col]*grid[row-1][col+1]*grid[row-2][col+2]*grid[row-3][col+3]
      if product > answer:
        answer = product
        
    #Check northwest
    if row - 3 > 0 and col - 3 > 0:
      product = grid[row][col]*grid[row-1][col-1]*grid[row-2][col-2]*grid[row-3][col-3]
      if product > answer:
        answer = product
    
print "Answer:",answer
