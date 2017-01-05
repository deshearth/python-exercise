# examples to create a dictionary
dict(zip(('x','y'),(1,2)))
# the dictionary would be {'x':1,'y':2}

#dict(['x',1]) why this does not work
# may when there is only one key, it must be like this
#   dict1 = {'x':1}
dict([['x',1],['y',2]])
# the dictionary would be {'x':1,'y':2}
# so I think if the parameter in the dict is sequence container, every
# elements in the container must have two elements
# and the number of parameter must be one and the number of parameter's
# elements must be larger than one
# in detail:
'''  dict(['x',1]) NO
     dict(['x',1],['y',2]) NO
	 dict(['x',2,3],['y',3,5]) NO
	 dict([['x',1],['y',2],['u',4]]) YES
	 '''



# some other methods to create dictionary
d = {} # it means that d is a dictionary
d['a'] = 2
print d['a']
# or d = {'a':2}

dict8 = dict(x=1,y=2)
# copy
dict9 = dict8.copy()
