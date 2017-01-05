seq = ['abs','cdh','tek','dfg']
print seq[:2] # [0,2)
print seq[1:] # [1,3]
print seq[:-1]
print seq[:-2]

# example each time to print, cut off the last char
s = 'abcde'
for i in [None] + range(-1,-len(s),-1):
    print s[:i]
#

# object to use 'join' method is the element to join the parameters in join
s = '     '.join(('Spanish','Inquisition','Made Easy')) 
print s


# string format output
## %% output %
print 'we are at %d%%' % 100
## \ escape
print '\\'

## dictionary format
print 'There are %(howmany)d %(lang)s ...' % \
        {'lang':'Python','howmany':3}

# alternative for format output: string template
from string import Template
s = Template('There are ${howmany} ${lang}')
print s.substitute(lang='Python')
