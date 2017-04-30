def matrix_mult(m1, m2):
    """
      >>> matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])
      [[19, 22], [43, 50]]
      >>> matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])
      [[31, 19], [85, 55]]
      >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
      [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
    x = 0
    k = 0
    r = 0
    c = 0
    l = []
    a = []
    while r < len(m1):
        while c < len(m1):
            while x < len(m1[0]):
                k += m1[r][x] * m2[x][c]
                x += 1
            l.append(k)
            x = 0
            k = 0
            c += 1
        a.append(l)
        c = 0
        l = []
        r += 1
    print a
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print "pass"
