from boolean_evaluation import eval_formula

if __name__=="__main__":
    print(eval_formula("10&"))
    print(eval_formula("10|"))
    print(eval_formula("11>"))
    print(eval_formula("10="))
    print(eval_formula("1011||="))
