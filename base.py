class DjangoBaseModel(metaclass=Meta):
    pass

class DjangoModel(metaclass=ModelBase):
    pass

class DjangoSale(DjangoModel):
    
    def djangosalefunc(self):
        return 'djangosalefunc'
