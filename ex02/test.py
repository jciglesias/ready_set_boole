from gray_code import gray_code
from graycode import gray_code as gc
from random import randrange

if __name__=="__main__":
    for x in [randrange(100) for _ in range(10)]:
        print(f"{x:2} = {gray_code(x):3} | {gc.tc_to_gray_code(x)}")
