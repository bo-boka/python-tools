f = open('text.txt', 'r')
f2 = f.read()
print f2
f.seek(0)  # to read file again from beginning, have to set pointer at beginning
print f.read()
f.readlines()  # returns a list of all the lines
f.close()

f = open('text.txt', 'r')
for line in f:
    print line
f.close()

# another way to ensure file will be closed automatically 'with' statement
with open('text.txt', 'r') as f:
    for line in f:
        print line

fw = open('try2.txt', 'w')  # if file doesn't exist, will be created
contents = 'Writing stuff into file'
fw.write(contents)
fw.close()
