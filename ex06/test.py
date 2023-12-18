from cnf import conjunctive_normal_form

if __name__=="__main__":
    print(conjunctive_normal_form("AB&!"))
    # A!B!|
    print(conjunctive_normal_form("AB|!"))
    # A!B!&
    print(conjunctive_normal_form("AB|C&"))
    # AB|C&
    print(conjunctive_normal_form("AB|C|D|"))
    # ABCD|||
    print(conjunctive_normal_form("AB&C&D&"))
    # ABCD&&&
    print(conjunctive_normal_form("AB&!C!|"))
    # A!B!C!||
    print(conjunctive_normal_form("AB|!C!&"))
    # A!B!C!&&