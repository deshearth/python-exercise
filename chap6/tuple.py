# tuple is unchangable, but the changable object in the tuple can be changed
t = (['xyz',123],23,-199)
print t
t[0][1] = ['abc','def']
print t


# something different from list
print ['a']
t = ('a')
print type(t)
tt = ('a',)
print type(tt)
# a list with only element can be defined, but tuple cannot
# in order to define a tuple with one element, add ',' at the end
