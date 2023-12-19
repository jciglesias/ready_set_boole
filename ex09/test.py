from set_evaluation import eval_set

if __name__=="__main__":
    sets = [{0, 1, 2}, {0, 3, 4}]
    print(eval_set("AB&", sets))
    # [0]
    sets = [{0, 1, 2}, {3, 4, 5}]
    print(eval_set("AB|", sets))
    # [0, 1, 2, 3, 4, 5]
    sets = [{0, 1, 2}]
    print(eval_set("A!", sets))
    # []