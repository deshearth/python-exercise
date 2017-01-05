class FooClass(object):
  """my very first class: FooClass"""
  version = 0.1 # class (data) attribute
  
  def __init__(self, nm='John Doe'):
    """constructor"""
    self.name = nm
    print 'Create instance for:', self.name 

x = FooClass()
print x.version
print x.name
