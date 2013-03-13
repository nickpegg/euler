doit =
    let sumOfSquares = sum $ map (^2) [1..100]
        squareOfSums = (sum [1..100]) ^ 2
    in squareOfSums - sumOfSquares