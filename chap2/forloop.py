foo = 'enumerate vs for loop'
for i in foo:
  print i
for i, ch in enumerate(foo):
  print ch, '(%d)' % i
