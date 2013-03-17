-- problem 16

import Data.Char

digitSum x = sum [digitToInt n | n <- show x]

main = print $ digitSum (2^1000)