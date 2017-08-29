INHERITED_ATTRS  =  ('_returns', )

class Meta(type):

    def __new__(meta, name, bases, attrs):
        parent = type.__new__(meta, name, bases, {})
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        for key, value in attrs.items():
            if not key.startswith('__') and callable(value):
                value = propagate(getattr(parent, key, None), value)
                attrs[key] = value
                print('key:', key, 'value ', value)

        return type.__new__(meta, name, bases, attrs)
def attrsetter(attr, value):
    return lambda method: setattr(method, attr, value) or method

def propagate(method1, method2):

    if method1:
        for attr in INHERITED_ATTRS:
            if hasattr(method1, attr) and not hasattr(method2, attr):
                setattr(method2, attr, getattr(method1, attr))
    return method2


def multi(method):
    method._api = 'multi'
    return method
def one(method):
    method._api = 'one'
    return method

class MyBaseModel(metaclass=Meta):
    _inherit = None
    _inherits = {}

    @classmethod
    def _build_model(cls):
        print('cls: ', cls)

AbstractModel = MyBaseModel
class MyModel(AbstractModel):
    def my_model_fuc(self):
        return 'my_model_func'

class Product(MyModel):
    def product_func(self):
        return 'product_func'


