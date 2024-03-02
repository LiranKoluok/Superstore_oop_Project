from product import Product

class Laptop (Product):
    def __init__(self, product_id, brand, model, year, price, CPU, hard_disk, screen):
        super().__init__(product_id, brand, model, year, price)
        self.CPU = CPU
        self.hard_disk = hard_disk
        self.screen = screen

    def print_me(self):
        super().print_me()
        print(self.CPU)
        print(self.hard_disk)
        print(self.screen)

    def __str__(self):
        return f"{super().__str__()},{self.CPU},{self.hard_disk},{self.screen}"

