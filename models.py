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

