class Product:

    def __init__(self, product_id, brand, model, year, price):
        self.product_id = product_id
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price


    def print_me(self):
        print("----", self.product_id, "----")
        print("brand:", self.brand)
        print("model:", self.model)
        print("year:", self.year)
        print("price:", self.price)

    def __str__(self):
        return f"{self.product_id},{self.brand},{self.model},{self.year},{self.price}"


    def __repr__(self):
        return str(self)

    def is_popular(self, min_year, max_price):
        return self.year > min_year and self.price <= max_price

