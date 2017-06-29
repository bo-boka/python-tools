
# dictionary reverse value function --> dict['key'][::-1]

ed = {}
ed['fruit']='orange'
ed['bird']='parrot'
print ed['fruit'].upper()

d = {'key1':{'key2':{'key3':'You\'re in.'}}}
print d['key1']['key2']['key3']

# print all by iteration
d = {'k1':1, 'k2':2, 'k3':3}
for k,v in d.iteritems():
    print "%s = %s" % (k, v)
