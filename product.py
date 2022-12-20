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
        self.__id = Product.__auto_increment_id
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
        
    def add_product(self):
        """Add the current product to list of products"""
        Product.__products[self] = self.__id
        
    @property
    def user_id(self):
        return self.__id
    
    def delete_product(self):
        """Delete the current product object"""
        try:
            del Product.__products[self]
            print('-'*5,f'\nProduct {self.title} (id {self.__id}) has been deleted','-'*5)
        except:
            print('-'*5,f'\nProduct {self.title} (id {self.__id}) has already been deleted','-'*5)
            
    @staticmethod
    def get_all_products():
        """return all products from list of products"""
        return tuple(Product.__products.keys())
    
    def get_info(self):
        """Return all attributes as a dictionary"""
        return self.__dict__
        
    def __repr__(self) -> str:
        return self.title + ' ' + 'id:' + str(self.__id)