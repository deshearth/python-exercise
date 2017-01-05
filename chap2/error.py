try:
  filename = raw_input('Enter filename: ')
  fobj = open(filename,'r')
    
  for eachline in fobj:
	print eachline,
  fobj.close()
except IOError, e:
	print 'file open error:', e
