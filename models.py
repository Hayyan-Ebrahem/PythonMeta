import api

class MetaModel(api.Meta):
    def __init__(self, name, bases, attrs):
        if not self._register:
            self._register = True
            super(MetaModel, self).__init__(name, bases, attrs)
            return

class BaseModel(metaclass=MetaModel):
    _register = False
    _table = None

    @api.multi
    def callme(self):
        return 'callme'
    @api.one
    def get_id(self):
        return 'get_id'

AbstractModel = BaseModel

class Model(AbstractModel):
    pass

class A(Model):
    def A_func(self):
        return 'A_func_return'

a=A()
a._register
print(a.callme)
