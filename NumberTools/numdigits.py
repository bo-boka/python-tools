def num_digits(n):
    count = 0
    if n == 0:
        print 1
    else:
        while n:
            count = count + 1
            n = abs(n) / 10
        return count

