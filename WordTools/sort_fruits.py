infile = open('unsorted_fruits.txt', 'r')
text = infile.readlines()
infile.close()

nl = ['zzz']
x = []
for w in text:
    for char in nl:         
        if w in nl:
            x = [w]
        elif w < char:
            nl[nl.index(char):nl.index(char)] = [w]
del nl[-1]

outfile = open('sorted_fruits.txt', 'w')
for elem in nl:
    outfile.write("%s" % (elem))

outfile.close()

sf = open('sorted_fruits.txt', 'r')
print sf.read()
