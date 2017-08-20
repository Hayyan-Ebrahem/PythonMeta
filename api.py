class Meta(type):

  def __new__(metaclass, name, bases, namespace):
    # print('Meta __new__ parent name',name, ' bases:',  bases)
    for key,  value in namespace.items():
      if hasattr(value, '_api'):
        print('------------------------------------', value)
    print('namespace', namespace)
    # print('\n')
    return type.__new__(metaclass, name, bases, namespace)


  def addedfrommeta(cls):
    print(cls.__dict__)
    return cls.__name__

class MetaModel(Meta):
    def __init__(self, name, bases, attrs):
        if not self._register:
            self._register = True
            super(MetaModel, self).__init__(name, bases, attrs)

def multi(method):
    method._api = 'multi'
    return method
def one(method):
    method._api = 'one'
    return method
