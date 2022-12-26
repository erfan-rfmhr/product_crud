from product import Product

def run():
    car = Product('car')
    bike = Product('bike')
    bike.create()
    car.create()
    car.update(title='car2', price=100)
    print(car.reade())
    print()
    car.delete()
    bike.update(regular_price=30)
    print(bike.reade())
    bike.delete()
    print()
    print(Product.reade_all())

if __name__ == '__main__':
    run()