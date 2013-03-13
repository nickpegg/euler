-- Needs work
-- While correct, too slow to find a solution in a reasonable amount of time

bigNum = 600851475143

divBy x y = (x `mod` y) == 0
factors x = filter (divBy x) [1..x]
isPrime x = (length $ factors x) == 2

primeFactors x = filter (isPrime) (factors x)

doit = max $ primeFactors bigNum