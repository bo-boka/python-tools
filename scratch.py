def count_letters(s):
    int_str = ""
    while s > 0:
        remain = s % 10
        int_str += str(remain)
        s - remain
    return int_str

print count_letters(123)