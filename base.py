class DjangoBaseModel(metaclass=Meta):
    pass

class DjangoModel(metaclass=ModelBase):
    pass

class DjangoSale(DjangoModel):
    @one
    def djangosalefunc(self):
        return 'djangosalefunc'
