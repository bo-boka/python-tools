infile = open('hb.txt', 'r')
text = infile.read()
infile.close()

wdlst = text.split()
x = 0
for w in wdlst:
    x += 1

print x
