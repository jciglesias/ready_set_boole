from set_evaluation import eval_set

if __name__=="__main__":
    # sets = [{0, 1, 2}, {0, 3, 4}]
    # print(eval_set("AB&", sets))
    # # [0]
    # sets = [{0, 1, 2}, {3, 4, 5}]
    # print(eval_set("AB|", sets))
    # # [0, 1, 2, 3, 4, 5]
    # sets = [{0, 1, 2}]
    # print(eval_set("A!", sets))
    # # []

    sets = [{}]
    print(eval_set("A", sets)) # {}
    print(eval_set("A!", sets)) # {}
    sets = [{42}]
    print(eval_set("A", sets)) # {42}
    print(eval_set("A!", sets)) # {}
    sets = [{1,2,3},{2,3,4}]
    print(eval_set("A!B&", sets)) # {4} 
    sets = [{0,1,2},{}]
    print(eval_set("AB|", sets)) # {0,1,2}
    sets = [{0,1,2},{}]
    print(eval_set("AB&", sets)) # {}
    sets = [{0,1,2},{0}]
    print(eval_set("AB&", sets)) # {0}
    sets = [{0,1,2},{42}]
    print(eval_set("AB&", sets)) # {}
    sets = [{0,1,2},{0}]
    print(eval_set("AB^", sets)) # {1,2} 
    sets = [{0},{1,2}]
    print(eval_set("AB>", sets)) # {1,2}
    sets = [{0},{0,1,2}]
    print(eval_set("AB>", sets)) # {0,1,2}
    
    
    sets = [{},{}, {}]
    print(eval_set("ABC||", sets)) # {}
    sets = [{0},{1},{2}]
    print(eval_set("ABC||", sets)) # {0,1,2}
    sets = [{0},{0},{0}]
    print(eval_set("ABC||", sets)) # {0}
    sets = [{0},{0},{}]
    print(eval_set("ABC&&", sets)) # {}
    sets = [{0},{0},{0}]
    print(eval_set("ABC&&", sets)) # {0}
    sets = [{0},{0},{0}]
    print(eval_set("ABC^^", sets)) # {0}
    sets = [{0},{0},{0}]
    print(eval_set("ABC>>", sets)) # {0}