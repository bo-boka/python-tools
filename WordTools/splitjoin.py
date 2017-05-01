def myreplace(old, new, s):
    """
        >>> myreplace(',', ';', 'this, that, and, some, other, thing')
        'this; that; and; some; other; thing'
        >>> myreplace(' ', '**', 'Words will now be separated by stars.')
        'Words**will**now**be**separated**by**stars.'
    """
    return new.join(s.split(old))
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

print "pass"
