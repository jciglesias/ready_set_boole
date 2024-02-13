from powerset import powerset
from random import sample

if __name__=="__main__":
    # lst = [sample(range(1000), 5) for _ in range(5)]
    # pwset = powerset(lst)
    # for x in pwset:
    #     print(x)

    print(powerset([]))
    print(powerset([0]))
    print(powerset([0,1]))
    print(powerset([0,1,2]))