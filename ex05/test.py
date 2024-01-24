from nnf import negation_normal_form
from truth_table import print_truth_table

def compare_tables(nf):
    nnf = negation_normal_form(nf)
    print(f"\n{nf} == {nnf}")
    print_truth_table(nnf)
    print()
    print_truth_table(nf)

if __name__=="__main__":
    compare_tables("A")
    compare_tables("A!")
    compare_tables("AB&!")
    compare_tables("AB|!")
    compare_tables("AB>!")
    compare_tables("AB=!")
    compare_tables("AB>")
    compare_tables("AB=")
    compare_tables("AB|C&!")
    compare_tables("ABC||!")
    compare_tables("ABC&|!")
    compare_tables("ABC^^")
    compare_tables("ABC>>")
