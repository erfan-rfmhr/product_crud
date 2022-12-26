from datetime import datetime

class Product:
    __products = {} # stores object and id
    __auto_increment_id = -1
        
    def __init__(self, title:str, short_description:str='', description:str='',
                 slug:str='', permalink:str='', price:float=0, regular_price:float=0,
                 sale_price:float=0, manage_stoke:int=0, stoke_quantity:int=0,
                 isAvailable=True, isVisible=True):
        
        assert price>=0, 'price is not greater than or equal to 0'
        assert regular_price>=0, 'regular price is not greater than or equal to 0'
        assert sale_price>=0, 'sale price is not greater than or equal to 0'
        assert manage_stoke>=0, 'manage_stoke is not greater than or equal to 0'
        assert stoke_quantity>=0, 'stoke_quantity is not greater than or equal to 0'
        Product.__auto_increment_id += 1
        self.id_ = Product.__auto_increment_id
        self.title = title
        self.short_description = short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.isAvailable = isAvailable
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stoke = manage_stoke
        self.stoke_quantity = stoke_quantity
        self.isVisible = isVisible
        self.date_created_gmt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_modified_gmt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def create(self):
        """Add the current product to list of products"""
        Product.__products[self] = self.id_

    def update(self, **kwargs):
        """Update the current product object"""
        for key, value in kwargs.items():
            if key in self.__dict__:
                if key in ('price', 'regular_price', 'sale_price', 'manage_stoke', 'stoke_quantity'):
                    assert isinstance(value, (int, float)), f'{key} has to be a number'
                    assert value >= 0, f'{key} has to be positive'
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = value
            else:
                print(f'No attribute called {key}')
        self.date_modified_gmt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def delete(self):
        """Delete the current product object"""
        try:
            del Product.__products[self]
            print('-'*5,f'\nProduct {self.title} (id {self.id_}) has been deleted','-'*5)
        except:
            print('-'*5,f'\nProduct {self.title} (id {self.id_}) has already been deleted','-'*5)
            
    def read(self):
        """Return all attributes as a dictionary"""
        return self.__dict__

    @staticmethod
    def read_all():
        """return all products from list of products"""
        return tuple(Product.__products.keys())
        
    def __repr__(self) -> str:
        return f"({self.title}, {self.id_})"