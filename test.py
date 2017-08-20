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

def multi(method):
    method._api = 'multi'
    return method
def one(method):
    method._api = 'one'
    return method

class MetaModel(Meta):
    def __init__(self, name, bases, attrs):
        if not self._register:
            self._register = True
            super(MetaModel, self).__init__(name, bases, attrs)

class BaseModel(metaclass=MetaModel):
    _register = False
    @multi
    def callme(self):
        return 'callme'
    def get_id(self):
        return 'get_id'

AbstractModel = BaseModel


class Model(AbstractModel):
    pass


class Sale(Model):

    def salecreate(self):
        return 'salecreate'

sale = Sale()
msale  =  DjangoSale()
print('\n')
print(MetaModel.__mro__)
print(Sale.__mro__)
print(DjangoSale.__mro__)
print('\n')
print(msale.djangosalefunc())
print(sale.callme())
print(sale.get_id())
# print(sale.addedfrommeta())
# print(product.addedfrommeta())
