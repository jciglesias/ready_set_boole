from sat import sat

if __name__=="__main__":
    print(sat("AB|"))
    # true
    print(sat("AB&"))
    # true
    print(sat("AA!&"))
    # false
    print(sat("AA^"))
    # false