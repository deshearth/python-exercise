s = 'string'
print id(s)
s2 = s
print id(s2)
list1 = ['a','b']
print id(list1[0])
list1[0] = 'cd'
print id(list1[0])

print id(list1)
list2 = list1
print '= assignment\n',id(list2)

list3 = list1[:]
print 'list3 = list1[:]\n',id(list3)

list4 = list(list1)
print 'list4 = list(list1)\n',id(list4)

list3[0] = 'u'
print 'after list3 is modified, list1 now is: ', list1

print 'the following is the example in core python programming'

person = ['name',['savings',100]]
hubby = person[:] #slice copy
wifey = list(person) #fac func copy
print [id(x) for x in person, hubby, wifey]
#why slice copy and fac func copy will give a different address
hubby[0] = 'joe'
wifey[0] = 'jane'
print hubby, wifey
hubby[1][1] = 50
print hubby, wifey
print '\nprint the id of element in each list'
print 'person',[id(x) for x in person]
print 'hubby',[id(x) for x in hubby]
print 'wifey',[id(x) for x in wifey]
# hubby[1] and wifey[1] are different reference name for the same
# list object. slice copy and fac func copy are all superficial
# copy. In order to get deep copy, use function copy.deepcopy in copy
# module


