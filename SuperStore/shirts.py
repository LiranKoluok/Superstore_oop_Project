from product import Product

class Shirts (Product):
    def __init__(self, product_id,product_name, price,  units_in_stock, brand="SuperStore", year=2023, model=""):
        super().__init__(product_id, brand, model, year, price)
        self.product_name = product_name
        self.units_in_stock = units_in_stock

    def __str__(self):
        return f"{self.product_id},{self.product_name},{self.price},{self.units_in_stock}"

    def __repr__(self):
        return str(self)


