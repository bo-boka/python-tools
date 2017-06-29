def reverse(s):
    """
      >>> reverse('happy')
      'yppah'
      >>> reverse('Python')
      'nohtyP'
      >>> reverse("")
      ''
      >>> reverse("P")
      'P'
    """
    # index = -1
    # revwerd = ""
    # while index > (-1 - len(s)):
    #     letter = s[index]
    #     revwerd += letter
    #     index -= 1
    # return revwerd

# less convoluted version
    rev_str = ""
    for i in range(1, len(s) + 1):
        rev_str += s[-i]
    return rev_str
# or simiply: s[::-1] to reverse
# s[::2] gets every other letter

# print function_name.__doc__ prints out anything within triple quotes
        
def mirror(s):
    """
      >>> mirror("good")
      'gooddoog'
      >>> mirror("yes")
      'yessey'
      >>> mirror('Python')
      'PythonnohtyP'
      >>> mirror("")
      ''
      >>> mirror("a")
      'aa'
    """
    mir_str = s
    for i in range(1, len(s) + 1):
        mir_str += s[-i]
    return mir_str

def remove_letter(letter, strng):
    """
      >>> remove_letter('a', 'apple')
      'pple'
      >>> remove_letter('a', 'banana')
      'bnn'
      >>> remove_letter('z', 'banana')
      'banana'
      >>> remove_letter('i', 'Mississippi')
      'Msssspp'
    """
    remlet = ""
    for char in strng:
        if char != letter:
            remlet += char
    return remlet

def is_palindrome(s):
    """
      >>> is_palindrome('abba')
      True
      >>> is_palindrome('abab')
      False
      >>> is_palindrome('tenet')
      True
      >>> is_palindrome('banana')
      False
      >>> is_palindrome('straw warts')
      True
    """
    rev_str = ""
    for let in range(1, len(s) + 1):
        rev_str += s[-let]
    return rev_str == s
        
def count_sub(sub, s):
    """
      >>> count('is', 'Mississippi')
      2
      >>> count('an', 'banana')
      2
      >>> count('ana', 'banana')
      2
      >>> count('nana', 'banana')
      1
      >>> count('nanan', 'banana')
      0
    """
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            count += 1
    return count

def remove_a_sub(sub, s):
    """
      >>> remove('an', 'banana')
      'bana'
      >>> remove('cyc', 'bicycle')
      'bile'
      >>> remove('iss', 'Mississippi')
      'Missippi'
      >>> remove('egg', 'bicycle')
      'bicycle'
    """
    n = 0
    b = len(sub)
    m = n + b
    if sub in s:
        while n < len(s):
            if s[n:m] == sub:
                s = s[:n] + s[m:]
                return s
            n += 1
            m = n + b
    else:
        return s

    #another way but better to combine this way with top way by adding while statement and reassigning value to s
    # for i in range(len(s) - len(sub) + 1):
    #     if s[i:i + len(sub)] == sub:
    #         new_str = s[:i] + s[i + len(sub):]
    #         return new_str
    #     return s
    
def remove_all(sub, s):
    """
      >>> remove_all('an', 'banana')
      'ba'
      >>> remove_all('cyc', 'bicycle')
      'bile'
      >>> remove_all('iss', 'Mississippi')
      'Mippi'
      >>> remove_all('eggs', 'bicycle')
      'bicycle'
    """
    i = 0
    while i < len(s):
        if s[i:i + len(sub)] == sub:
            s = s[:i] + s[i + len(sub):]
            i = 0
        i += 1
    return s

    # n = 0
    # b = len(sub)
    # m = n + b
    # if sub in s:
    #     while n < len(s):
    #         if s[n:m] == sub:
    #             s = s[:n] + s[m:]
    #             n = 0
    #         else:
    #             n += 1
    #         m = n + b
    #     return s
    # return s

    #another removes all subs even if it was part of already removed sub
    # wall = 0
    # new_str = ""
    # for i in range(len(s) - len(sub) + 1):
    #     if s[i:i + len(sub)] == sub:
    #         new_str += s[wall:i]
    #         wall = i + len(sub)
    # return new_str + s[wall:]
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()


prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print letter + 'u' + suffix
    else:
        print letter + suffix


def find(strng, ch, start=0):
    index = start
    while index < len(strng):
        if strng[index] == ch:
            print index
        index += 1
    return

def count_letters(s, ch):
    count = 0
    for char in s:
        if char == ch:
            count += 1
    return count

