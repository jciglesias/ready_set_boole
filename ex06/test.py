from cnf import conjunctive_normal_form
from truth_table import print_truth_table

def compare_tables(nf):
    nnf = conjunctive_normal_form(nf)
    print(f"\n{nf} == {nnf}")
    print_truth_table(nnf)
    print()
    print_truth_table(nf)

if __name__=="__main__":
    compare_tables("A")
    compare_tables("A!")
    compare_tables("AB&!")# A!B!|
    compare_tables("AB|!")# A!B!&
    compare_tables("AB>!")
    compare_tables("AB=!")
    compare_tables("AB>")
    compare_tables("AB=")
    compare_tables("AB|C&") # AB|C&
    compare_tables("ABC||!")
    compare_tables("ABC&|!")
    compare_tables("ABC^^")
    compare_tables("ABC>>")

    
    # print(conjunctive_normal_form("AB|C|D|"))
    # ABCD|||
    # print(conjunctive_normal_form("AB&C&D&"))
    # ABCD&&&
    # print(conjunctive_normal_form("AB&!C!|"))
    # A!B!C!||
    # print(conjunctive_normal_form("AB|!C!&"))
    # A!B!C!&&
    # print(conjunctive_normal_form("ABC>>"))