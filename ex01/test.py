from multiplier import multiplier
from random import randrange

if __name__=="__main__":
    for x, y in [(randrange(100), randrange(100)) for _ in range(10)]:
        print(f"{x:2} x {y:2} = {multiplier(x,y)}\t| {x * y}")