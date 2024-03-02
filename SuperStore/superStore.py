import csv
from client import Client
from laptop import Laptop
from smartPhone import Smartphone
from exceptions import ClientNotFoundError, ShirtNotFoundError, DuplicateEntryInCsvFile, InvalidYear
from shirts import Shirts
from order import Order




class SuperStore:

    def __init__(self, products_path, clients_path, orders_path, shirts_path):
        self.products = {}
        self.clients = {}
        self.orders = {}
        self.min_year_to_be_popular = 2017
        self.max_price_to_be_popular = 3000

        self.read_products(products_path)
        self.read_clients(clients_path)
        self.read_shirts(shirts_path)
        self.read_orders(orders_path)

    def read_products(self, products_path):
        with open(products_path) as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)

            for row in reader:
                p_id, p_type, p_brand, p_model, p_year, p_price, p_cpu, p_hard_disk, p_screen, cell_net, num_cores, cam_res = row
                p_id = int(p_id)
                p_year = int(p_year)
                p_price = float(p_price)

                if p_id in self.products:
                    raise DuplicateEntryInCsvFile(f"duplicate product id: {p_id}")

                if p_type == "laptop":  # laptop
                    product = self.build_laptop(p_id, p_brand, p_model, p_year, p_price, p_cpu, int(p_hard_disk), float(p_screen))
                else:  # smartphone
                    product = self.build_phone(p_id, p_brand, p_model, p_year, p_price, cell_net, int(num_cores), int(cam_res))
                #self.__iadd__(product)
                self.add_product(product)

    def add_product(self, product):
        self.__iadd__(product)

    @staticmethod
    def build_laptop(p_id, p_brand, p_model, p_year, p_price, p_cpu, p_hard_disk, p_screen):
        return Laptop(p_id, p_brand, p_model, p_year, p_price, p_cpu, p_hard_disk, p_screen)

    @staticmethod
    def build_phone(p_id, p_brand, p_model, p_year, p_price, cell_net, num_cores, cam_res):
        return Smartphone(p_id, p_brand, p_model, p_year, p_price, cell_net, num_cores, cam_res)


    def read_shirts(self,shirts_path):
        with open(shirts_path) as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                shirt_id, shirt_name, shirt_price, units_in_stock = row
                shirt_id = int(shirt_id)
                shirt_price = float(shirt_price)
                units_in_stock = int(units_in_stock)

                if shirt_id in self.products:
                    raise DuplicateEntryInCsvFile(f"duplicate product id: {shirt_id}")

                shirt = Shirts(shirt_id, shirt_name, shirt_price, units_in_stock)
                #self.__iadd__(shirt)
                self.add_product(shirt)

    def __iadd__(self, other):
        MIN_YEAR = 1000
        MAX_YEAR = 10000
        if type(other) is Laptop or type(other) is Smartphone or type(other) is Shirts:
            if other.year < MIN_YEAR or other.year >= MAX_YEAR:
                raise InvalidYear(f"please enter different year that bigger then {MIN_YEAR} and lower then {MAX_YEAR}")
            if other.product_id not in self.products:
                self.products[other.product_id] = other
        return self

    def read_orders(self, orders_path):
        with open(orders_path) as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                order_id, client_id, product_id, quantity = row
                order_id = int(order_id)
                client_id = int(client_id)
                product_id = int(product_id)
                quantity = int(quantity)
                if order_id in self.orders:
                    raise DuplicateEntryInCsvFile(f"duplicate order id: {order_id}")
                order = Order(order_id, client_id, product_id, quantity)
                self.orders[order_id]=order

    def get_shirt(self,shirt_id):
        if shirt_id in self.products:
            product = self.products.get(shirt_id)
            if type(product) is Shirts:
                return product

    def get_max_order_id(self):
        return max(self.orders.keys())

    def add_order(self,client_id,product_id,quantity):
        order_id = self.get_max_order_id() + 1
        if client_id not in self.clients:
            raise ClientNotFoundError(f"client id not found: {client_id}")
        if product_id not in self.products:
            raise ShirtNotFoundError(f"shirt id not found: {product_id}")
        product = self.products.get(product_id)
        if type(product) is Shirts:
            if quantity > product.units_in_stock:
                raise ValueError(f"quantity is too big: {quantity} ,in object: {product.units_in_stock}")
        else:
            if quantity > 1:
                raise ValueError(f"quantity is too big: {quantity}")
        new_order = Order(order_id,client_id,product_id,quantity)
        self.orders[order_id] = new_order

    def print_orders(self):
        for o_id,order in self.orders.items():
            print(order)


    def read_clients(self, clients_path):
        with open(clients_path) as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)

            for row in reader:
                c_id,c_name,c_email,c_address,c_phone_number,c_gender = row
                c_id = int(c_id)
                c_gender = c_gender.upper() # fix for last exercise
                if c_gender not in ["M", "F"]:
                    c_gender = "M"
                if c_id in self.clients:
                    raise DuplicateEntryInCsvFile(f"duplicate client id: {c_id}")
                client = Client(c_id, c_name, c_email, c_address, c_phone_number, c_gender)
                self.add_client(client)

    def print_products(self):
        for p_id, product in self.products.items():
            print(product)

    def print_clients(self):
        for c_id, client in self.clients.items():
            print(client)

    def get_product(self, p_id):
        if p_id in self.products:
            product = self.products[p_id]
            return product

    def get_client(self, c_id):
        if c_id in self.clients:
            client = self.clients[c_id]
            return client


    def add_client(self, client):
        email = client.email
        found = email.find("@")
        if found == -1 or found == len(email) - 1:
            client.email = "random@random.com"
        phone = client.phone_number
        if len(phone) != 10 or not phone.isnumeric():
            client.phone = "0500000000"
        gender = client.gender
        if gender not in ["M", "F"]:
            client.gender = "M"

        if client.client_id in self.clients:
            return False
        self.clients[client.client_id] = client
        return True

    def remove_product(self,p_id):
        if p_id in self.products:
            del self.products[p_id]
            return True
        return False

    def remove_client(self, c_id):
        if c_id in self.clients:
            del self.clients[c_id]
            return True
        return False

    def get_all_by_brand(self,brand):
        result = []
        for p_id, product in self.products.items():
            if product.brand == brand:
                result.append(product)
        return result

    def get_all_by_price_under(self,max_price):
        result = []
        for p_id, product in self.products.items():
            if product.price < max_price:
                result.append(product)
        return result

    def get_most_expensive_product(self):
        max_price = 0
        most_expensive_product = None
        for p_id, product in self.products.items():
            if product.price > max_price:
                max_price = product.price
                most_expensive_product = product
        return most_expensive_product

    def print_shirts(self):
        for p_id in self.products:
            product = self.products[p_id]
            if type(product) is Shirts:
                print(product)

    def get_all_phones(self):
        phone_list = []
        for p_id, product in self.products.items():
            if type(product) is Smartphone:
                phone_list.append(product)
        return phone_list

    def get_all_laptops(self):
        laptop_list = []
        for p_id, product in self.products.items():
            if type(product) is Laptop:
                laptop_list.append(product)
        return laptop_list

    def phone_average_price(self):
        sum_prices = 0
        phones = self.get_all_phones()
        if len(phones) == 0:
            return 0
        for phone in phones:
            sum_prices += phone.price
        sum_prices /= len(phones)
        return sum_prices


    def get_max_screen(self):
        max_screen_size = 0
        laptops = self.get_all_laptops()
        if len(laptops) == 0:
            return 0
        for laptop in laptops:
            max_screen_size = max(max_screen_size, laptop.screen)
        return max_screen_size

    def get_common_cam(self):
        phones = self.get_all_phones()
        res_dict = {}
        for p in phones:
            if p.cam_res not in res_dict:
                res_dict[p.cam_res] = 1
            else:
                res_dict[p.cam_res] += 1

        most_pop_res = 0 # most popular resolution
        pop_count = 0 # most popular resolution popularity

        for resolution, popularity in res_dict.items():
            if popularity > pop_count:
                most_pop_res = resolution
                pop_count = popularity
        #phone_res = max(res_dict, key=res_dict.get)
        #print(phone_res)

        return most_pop_res

    def list_popular(self):
        pop_list = []
        for p_id, item in self.products.items():
            if item.is_popular(self.min_year_to_be_popular, self.max_price_to_be_popular):
                pop_list.append(item)
        return pop_list






























