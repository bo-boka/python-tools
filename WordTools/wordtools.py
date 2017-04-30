def cleanword(word):
    """
      >>> cleanword('what?')
      'what'
      >>> cleanword('"now!"')
      'now'
      >>> cleanword('?+="word!,@$()"')
      'word'
    """
    x = ''
    for char in word:
        for i in range(97, 122):
            if char == chr(i):
                x += char
    return x

def has_dashdash(s):
    """
      >>> has_dashdash('distance--but')
      True
      >>> has_dashdash('several')
      False
      >>> has_dashdash('critters')
      False
      >>> has_dashdash('spoke--fancy')
      True
      >>> has_dashdash('yo-yo')
      False
    """
    x = 0
    for char in s:
        if char == '-':
            x += 1
    if x == 2:
        return True
    else:
        return False

def extract_words(s):
    """
      >>> extract_words('Now is the time!  "Now", is the time? Yes, now.')
      ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
      >>> extract_words('she tried to curtsey as she spoke--fancy')
      ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
    """
    x = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                x += char.swapcase()
            else:
                x += char
        else:
            x += ' '
    print x.split()

def wordcount(word, wordlist):
    """
      >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['now', 2]
      >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
      ['is', 4]
      >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['time', 1]
      >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['frog', 0]
    """
    x = 0
    for elem in wordlist:
        if elem == word:
            x += 1
    return [word, x]


def wordset(wordlist):
    """
      >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['is', 'now', 'time']
      >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
      ['I', 'a', 'am', 'is']
      >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
      ['a', 'am', 'are', 'be', 'but', 'is', 'or']
    """
    nl = ['zzz']
    x = []
    for w in wordlist:
        for char in nl:         
            if w in nl:
                x = [w]
            elif w < char:
                nl[nl.index(char):nl.index(char)] = [w]
    del nl[-1]
    print nl
    
def longestword(wordset):
    """
      >>> longestword(['a', 'apple', 'pear', 'grape'])
      5
      >>> longestword(['a', 'am', 'I', 'be'])
      2
      >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
      34
    """
    nl = [wordset[0]]
    for w in wordset:
        for char in nl:         
            if len(w) > len(char):
                nl[nl.index(char)] = w
    print len(nl[0])
                
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

print "pass"
