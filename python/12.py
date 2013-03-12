#!/usr/bin/which python

# INCOMPLETE

import math

i = 0
last_tnum = 0
top_num_divisors = 0
run = True

while run:
    i += 1
    tnum = 0

    # Generate the triangle number
    tnum = last_tnum + i
#    for x in range(i):
#        tnum += x


    # Find the divisors
    divisors = []
    num_divisors = 0

    for d in xrange(1, math.sqrt(tnum)):
        if d in divisors:
            break
        elif tnum % d == 0:
            num_divisors += 2
#            divisors.append(tnum / d)
#            divisors.append(d)

    if num_divisors > 500:
        run = False
#        divisors.sort()
#        print("Divisors: " + str(divisors))

#    if tnum == 28:
#        run = False
    top_num_divisors = max(num_divisors, top_num_divisors)

    if i % 100 == 0 or run is False:
        print("i: " + str(i))
        print("Triangle number: " + str(tnum))
        print("Number of divisors: " + str(num_divisors))
        print("Max num divisors: " + str(top_num_divisors)) 
        print('')

    last_tnum = tnum
