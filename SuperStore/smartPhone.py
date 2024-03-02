from product import Product

class Smartphone (Product):
    def __init__(self, product_id, brand, model, year, price, cell_net, num_cores, cam_res):
        super().__init__(product_id, brand, model, year, price)
        self.cell_net = cell_net
        self.num_cores = num_cores
        self.cam_res = cam_res

    def print_me(self):
        super().print_me()
        print(self.cell_net)
        print(self.num_cores)
        print(self.cam_res)

    def __str__(self):
        return f"{super().__str__()},{self.cell_net},{self.num_cores},{self.cam_res}"




