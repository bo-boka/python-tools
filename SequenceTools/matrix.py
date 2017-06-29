# getting diagonal
row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]
m = [row1, row2, row3]

d = []
i = 0
for row in m:
    d.append(i)
    i += 1
print 'Diagonal is {x}'.format(x=d)

def add_row(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_row(m)
      [[0, 0], [0, 0], [0, 0]]
      >>> n = [[3, 2, 5], [1, 4, 7]]
      >>> add_row(n)
      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
      >>> n
      [[3, 2, 5], [1, 4, 7]]
    """
    x = 0
    j = []
    while x < len(matrix[0]):
        j += [0]
        x += 1
    print matrix + [j]

def add_column(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_column(m)
      [[0, 0, 0], [0, 0, 0]]
      >>> n = [[3, 2], [5, 1], [4, 7]]
      >>> add_column(n)
      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
      >>> n
      [[3, 2], [5, 1], [4, 7]]
    """
    x = 0
    b = 0
    c = []
    while x < len(matrix):
        c += [matrix[x][:]]
        x += 1    
    while b < len(c):
        c[b] += [0]
        b += 1
    print c

def add_matrices(m1, m2):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> b = [[2, 2], [2, 2]]
      >>> add_matrices(a, b)
      [[3, 4], [5, 6]]
      >>> c = [[8, 2], [3, 4], [5, 7]]
      >>> d = [[3, 2], [9, 2], [10, 12]]
      >>> add_matrices(c, d)
      [[11, 4], [12, 6], [15, 19]]
      >>> c
      [[8, 2], [3, 4], [5, 7]]
      >>> d
      [[3, 2], [9, 2], [10, 12]]
   """
    x = 0
    b = 0
    c1 = []
    c2 = []
    while x < len(m1):
        c1 += [m1[x][:]]
        x += 1
    while b < len(m2):
        c2 += [m2[b][:]]
        b += 1
    s = 0
    i = 0    
    while s < len(c1):
        while i < len(c1[0]):
            c1[s][i] += c2[s][i]
            i += 1
        s += 1
        i = 0
    print c1

def scalar_mult(s, m):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> scalar_mult(3, a)
      [[3, 6], [9, 12]]
      >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
      >>> scalar_mult(10, b)
      [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
      >>> b
      [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    x = 0
    c1 = []
    while x < len(m):
        c1 += [m[x][:]]
        x += 1
    d = 0
    i = 0    
    while d < len(c1):
        while i < len(c1[0]):
            c1[d][i] *= s
            i += 1
        d += 1
        i = 0
    print c1
    
def row_times_column(m1, row, m2, column):
    """
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
      19
      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
      22
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
      43
      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
      50
    """
    x = 0
    k = 0
    while x < len(m1):
        k += m1[row][x] * m2[x][column]
        x += 1
    print k
    
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
            l += [k]
            x = 0
            k = 0
            c += 1
        a += [l]
        c = 0
        l = []
        r += 1
    print a
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print "pass"
