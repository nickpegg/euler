-- NOT DONE

clean x y = x `mod` y == 0
dalist = filter (clean 7 == 0) [1..10]

--isPrime x = (length (filter ((mod) x == 0) [1..x])) == 0