def multiples_of(num, numlist):
    """
        >>> multiples_of(35, [1, 2, 3, 4, 5, 6, 7, 8, 9, 20])
        [1, 5, 7]
        >>> multiples_of(70, [2, 5, 10, 35, 8, 12])
        [2, 5, 10, 35]
    """
    l = []
    for x in numlist:
        if num % x == 0:
            l += [x]
    print l

if __name__ == '__main__':
    import doctest
    doctest.testmod()
print "pass"
