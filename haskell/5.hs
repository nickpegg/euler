-- Fairly slow when ran in GHCI, not bad when compiled

isGood x = 
    let daMod = (mod) x
        mods = map daMod [1..20]
    in and (map (==0) mods)

main = print (take 1 [x | x <- [20,40..], isGood x])