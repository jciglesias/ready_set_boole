from nnf import negation_normal_form
import binarytree as bt

print(negation_normal_form("AB&!"))
# A!B!|
print(negation_normal_form("AB|!"))
# A!B!&
print(negation_normal_form("AB>"))
# A!B|
print(negation_normal_form("AB="))
# AB&A!B!&|
print(negation_normal_form("AB|C&!"))
# A!B!&C!|
print(negation_normal_form("AB=!"))
