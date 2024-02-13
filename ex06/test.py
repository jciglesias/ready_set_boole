from cnf import conjunctive_normal_form
from truth_table import print_truth_table

def compare_tables(nf):
    nnf = conjunctive_normal_form(nf)
    print(f"\n{nf} == {nnf}")
    print_truth_table(nnf)
    print()
    print_truth_table(nf)

if __name__=="__main__":
    # Basic tests
    compare_tables("A")
    compare_tables("A!")
    compare_tables("AB&!") # A!B!|
    compare_tables("AB|!") # A!B!&
    compare_tables("AB>!")
    compare_tables("AB=!")
    
    # Composition
    compare_tables("ABC||")
    compare_tables("ABC||!")
    compare_tables("ABC|&")
    compare_tables("ABC&|")
    compare_tables("ABC&|!")
    compare_tables("ABC^^")
    compare_tables("ABC>>")
   
    # compare_tables("AB>")
    # compare_tables("AB=")
    # compare_tables("AB|C&") # AB|C&
    # compare_tables("ABCD&|&") # ABC|BD|&&
    # compare_tables("AB|C|D|") # ABCD|||
    # compare_tables("AB&C&D&") # ABCD&&&   
    # compare_tables("AB&!C!|") # A!B!C!||
    # compare_tables("AB|!C!&") # A!B!C!&&
