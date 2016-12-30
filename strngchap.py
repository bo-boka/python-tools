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
    index = -1
    revwerd = ""
    while index > (-1 - len(s)):
        letter = s[index]
        revwerd += letter
        index -= 1
    return revwerd
        
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
    index = -1
    mirwerd = ""
    for char in s:
        mirwerd += char
    while index > (-1 - len(s)):
        letter = s[index]
        mirwerd += letter
        index -= 1
    return mirwerd

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
    index = -1
    revwerd = ""
    while index > (-1 - len(s)):
        letter = s[index]
        revwerd += letter
        index -= 1
    if s == revwerd:
        print "True"
    else:
        print "False"
        
def count(sub, s):
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
    n = 0
    b = len(sub)
    m = n + b
    while n < len(s):
        if s[n:m] == sub:
            count += 1
        n += 1
        m = n + b
    print count

def remove(sub, s):
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
    n = 0
    b = len(sub)
    m = n + b
    if sub in s:
        while n < len(s):
            if s[n:m] == sub:
                s = s[:n] + s[m:]
                n = 0
            else:
                n += 1
            m = n + b
        return s
    else:
        return s
    
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

def count_letters(strng, ch):
    fruit = strng
    count = 0
    for char in fruit:
        if char == ch:
            count += 1
    print count

