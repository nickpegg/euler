-- Naive fib stolen from the Haskell wiki.
-- Really slow in the interpreter, not bad when compiled
-- I should really come up with a better Fibonacci generator
fib 0 = 1
fib 1 = 2
fib n = fib (n-1) + fib (n-2)

doit = sum (filter even (takeWhile (<4000000) (map fib [1..])))

main = print doit
