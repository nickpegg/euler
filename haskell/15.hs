-- 'Working' naive solution
-- Holy crap, it seriously took me over 24 hours to calculate this, compiled.
-- I pass N in to see how the speed dies as N increases (see testIt)
dive (x, y, n)
    | x == n && y == n = 1
    | x == n = dive (x, succ y, n)
    | y == n = dive (succ x, y, n)
    | otherwise = dive (succ x, y, n) + dive (x, succ y, n)


-- Better solution: Central Binomial Coefficients lololololololol
-- This is super-fast. N = 50,000 only takes a few seconds when left uncompiled
choose n 0 = 1
choose 0 k = 0
choose n k = choose (n-1) (k-1) * n `div` k

doit n = choose (2*n) n


testIt = [(n, dive (0, 0, n)) | n <- [2..20]]
testIt' = [(n, solve n) | n <- [2..200]]

main = print $ doit 20