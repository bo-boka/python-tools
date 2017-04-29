
def max_nnl(x):
    max = x[0]
    while type(max) == type([]):
        max = max[0]
    for elem in x:
        if type(elem) == type([]):
            max_of_list_elem = max_nnl(elem)
            if max < max_of_list_elem:
                max = max_of_list_elem
        else:
            if max < elem:
                max = elem
    return max

nnl = [1, 2, [11, 13], 8, [2, 3, 5]]
print max_nnl(nnl)