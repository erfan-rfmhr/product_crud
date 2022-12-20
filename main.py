from product import Product

p = Product('test')

print(type(Product))    # type of every class in python is "type"
print(type(p))
print(isinstance(p, Product))   # output is True because p is an instance of Product class