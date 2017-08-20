import models

class Sale(models.Model):

    def salecreate(self):
        return 'salecreate'

sale = Sale()
print('\n')
print(Sale.__mro__)
print('\n')
print(sale.callme())
print(sale.get_id())
# print(sale.addedfrommeta())
# print(product.addedfrommeta())
