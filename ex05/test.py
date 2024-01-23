from nnf import negation_normal_form

# print(negation_normal_form("A") == "A")
# print(negation_normal_form("A!") == "A!")
# print(negation_normal_form("AB&!") == "A!B!|")
# print(negation_normal_form("AB|!") == "A!B!&")
# print(negation_normal_form("AB>!") == "AB!&")
# print(negation_normal_form("AB=!") == "A!B!|AB|&")
# print(negation_normal_form("AB>") == "A!B|")
# print(negation_normal_form("AB=") == "AB&A!B!&|")
# print(negation_normal_form("AB|C&!") == "A!B!&C!|")
print(negation_normal_form("ABC||!"))