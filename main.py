from datetime import datetime

class Product:
    products = []
    def __init__(self):
        self.title = None
        self.short_description = None
        self.description = None 
        self.slug = None
        self.permalink = None
        self.isAvailable = None
        self.sku = None
        self.price = None
        self.regular_price = None
        self.sale_price = None
        self.manage_stoke = None
        self.stoke_quantity = None
        self.isVisible = None
        self.date_created_gmt = None
        self.date_modified_gmt = None
        
    @staticmethod
    def add_product():
        """Add a new product"""
        print('-'*5,'\nAdd a new product','-'*5)
        new_product = Product()
        new_product.title = input("Enter the title of the product: ")
        new_product.short_description = input("Enter the short description of the product: ")
        new_product.description = input("Enter the description of the product: ")
        new_product.slug = input("Enter the slug of the product: ")
        new_product.permalink = input("Enter the permalink of the product: ")
        availability = input("Enter the availability of the product(true/false): ")
        if availability.lower() == 'true': new_product.isAvailable = True
        else: new_product.isAvailable = False
        new_product.sku = input("Enter the sku of the product: ")
        new_product.price = int(input("Enter the price of the product: "))
        new_product.regular_price = int(input("Enter the regular price of the product: "))
        new_product.sale_price = int(input("Enter the sale price of the product: "))
        new_product.manage_stoke = int(input("Enter the manage stoke of the product: "))
        new_product.stoke_quantity = int(input("Enter the stoke quantity of the product: "))
        visibility = input("Enter the visibility of the product(true/false): ")
        if visibility.lower() == 'true': new_product.isVisible = True
        else: new_product.isVisible = False
        new_product.date_created_gmt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_product.date_modified_gmt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Product.products.append(new_product)
    
    @staticmethod
    def delete_product():
        """Delete a product"""
        print('-'*5,'\nDelete a product','-'*5)
        product_to_delete = input('Enter the title of the product: ')
        for p in Product.products:
            if p.title == product_to_delete:
                Product.products.remove(p)
                break
        else:
            print(f'The {product_to_delete} does not exist!')
    
    @staticmethod
    def update_product():
        """Update a product"""
        print('-'*5,'\nUpdate a product','-'*5)
        product_to_update = input('Enter the title of the product: ')
        for p in Product.products:
            if p.title == product_to_update:
                print('-'*5,f'\nUpdate {p.title} product','-'*5)
                p.title = input("Enter the new title of the product: ")
                p.short_description = input("Enter the short description of the product: ")
                p.description = input("Enter the description of the product: ")
                p.slug = input("Enter the slug of the product: ")
                p.permalink = input("Enter the permalink of the product: ")
                availability = input("Enter the availability of the product(true/false): ")
                if availability.lower() == 'true': p.isAvailable = True
                else: p.isAvailable = False
                p.sku = input("Enter the sku of the product: ")
                p.price = int(input("Enter the price of the product: "))
                p.regular_price = int(input("Enter the regular price of the product: "))
                p.sale_price = int(input("Enter the sale price of the product: "))
                p.manage_stoke = int(input("Enter the manage stoke of the product: "))
                p.stoke_quantity = int(input("Enter the stoke quantity of the product: "))
                visibility = input("Enter the visibility of the product(true/false): ")
                if visibility.lower() == 'true': p.isVisible = True
                else: p.isVisible = False
                p.date_modified_gmt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            print(f'The {product_to_update} does not exist!')

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title