from boolean_evaluation import eval_formula

if __name__=="__main__":
    print(eval_formula("10&"))
    # false
    print(eval_formula("10|"))
    # true
    print(eval_formula("11>"))
    # true
    print(eval_formula("10="))
    # false
    print(eval_formula("1011||="))
    # true
    print(eval_formula("1!"))
    # false
