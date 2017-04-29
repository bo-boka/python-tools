nested_num_list = [1, 2, [11, 13], 8, [2, 3, 5]]

def sum_nnl(x):
    sum = 0
    for elem in x:
        if type(elem) == type([]):
            sum = sum + sum_nnl(elem)
        else:
            sum = sum + elem
    return sum

print sum_nnl(nested_num_list)