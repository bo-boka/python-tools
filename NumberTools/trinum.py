def trinumb(n):  # triangle number sequence
    result = (n * (n + 1))/2
    print n, '\t', result

def tritable(high):  # makes table for triangle numbers
    i = 1
    while i <= high:
        trinumb(i)
        i += 1
    
