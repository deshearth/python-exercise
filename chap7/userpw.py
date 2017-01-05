#!/user/bin/env python
db = {}
def newuser():
  print 'login desired: '
  while True:
	name = raw_input()
	if db.has_key(name):
	  print 'name taken'
	  continue
	else:
	  break
  pw = raw_input('Enter password: ')
  db[name] = pw

def olduser():
  name = raw_input('login: ')
  pw = raw_input('password: ')
  password = db.get(name)
  if pw == password:
	print 'welcome back', name
  else:
	print 'login incorrect'

def showmenu():
  prompt = """
N)ew User Login
E)xisting User Login
Q)uit
Enter choice: """
  done = False
  while not done:
	chosen = False
	while not chosen:
	  try:
		choice = raw_input(prompt).strip()[0].lower()
	  except (EOFERROR, KeyboardInterrupt):
		choice = 'q'
	  print '\nYou picked: [%s]' % choice
	  if choice not in 'neq':
		print 'invalid option, try again'
	  else:
		chosen = True
	if choice == 'q': done = True
	if choice == 'n': newuser()
	if choice == 'e': olduser()
  


if __name__ == '__main__':
  showmenu()


