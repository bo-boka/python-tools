li = [x for x in range(1,10)]
print li  # prints 1 - 9 in list form

st_li = [ch for ch in 'string']
print st_li  # prints string in list form

series = [s**2 for s in range(1, 6)]
print series  # prints the square of each num in range

even = [e for e in range(1, 21) if e%2==0]
print even  # prints evens

row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]
m = [row1, row2, row3]
# to get the first column can use list comprehension
col1 = [row[0] for row in m]

tup_li = [(1, 2), (3, 4), (5, 6)]
for (t1, t2) in tup_li:
    print t1  # prints 1st elem in tuple


