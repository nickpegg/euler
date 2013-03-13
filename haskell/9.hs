isTriplet [a,b,c] = a^2 + b^2 == c^2
isSum [a,b,c] = a + b + c == 1000

doit =
    let theList = [[a,b,c] | c <- [1..1000], b <- [1..c], a <- [1..b]]
    in filter (isTriplet) $ filter (isSum) theList
main = print (head doit, product $ head doit)