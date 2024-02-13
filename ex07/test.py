from sat import sat

if __name__=="__main__":
    # Basic tests
    print("OK" if sat("A") == True else "KO") # true
    print("OK" if sat("A!") == True else "KO") # true
    print("OK" if sat("AA|") == True else "KO") # true
    print("OK" if sat("AA&") == True else "KO") # true
    print("OK" if sat("AA!&") == False else "KO") # false
    print("OK" if sat("AA^") == False else "KO") # false
    print("OK" if sat("AB^") == True else "KO") # true
    print("OK" if sat("AB=") == True else "KO") # true
    print("OK" if sat("AA>") == True else "KO") # true
    print("OK" if sat("AA!") == True else "KO") # true
    
    # Composition
    print("OK" if sat("ABC||") == True else "KO") # true
    print("OK" if sat("AB&A!B!&&") == False else "KO") # false
    print("OK" if sat("ABCDE&&&&") == True else "KO") # true
    print("OK" if sat("AAA^^") == True else "KO") # true
    print("OK" if sat("ABCDE^^^^") == True else "KO") # true
