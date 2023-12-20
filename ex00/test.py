from adder import adder
from random import randrange

if __name__=="__main__":
    for x, y in [(randrange(100), randrange(100)) for _ in range(10)]:
        print(f"{x:2} + {y:2} = {adder(x,y)}")