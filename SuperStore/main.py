from shirt_orders_analysis import ShirtOrdersAnalysis
from shirts import Shirts
from laptop import Laptop
from smartPhone import Smartphone
from superStore import SuperStore
from client import Client
from exceptions import ProductNotInStore, InvalidQuantity, ClientNotFoundError
from shirt_orders_analysis import *
import sys



def print_menu():
    MENU = """
    --- MENU ----
    1. Print all products
    2. Print all clients
    3. Add new product to the store
    4. Add new client to the store
    5. Remove product
    6. Remove client
    7. Print all products under price
    8. Print the most expensive product
    9. print smartphone list
    10. print laptop list
    11. print average phone price
    12. print largest laptop screen
    13. print common camera resolution
    14. print popular products
    15. print store shirt list
    16. create new order
    17. print all orders
    18. EXIT
    B. BONUS!
    """
    print(MENU)


def print_all_products(store):
    store.print_products()

def print_all_clients(store):
    store.print_clients()


def create_smartphone(store):
    p_id = int(input("insert smartphone id: "))
    p_brand = input("insert smartphone brand: ")
    p_model = input("insert smartphone model: ")
    p_year = int(input("insert smartphone year: "))
    p_price = float(input("insert smartphone price: "))
    p_cell_net = input("insert smartphone cell_net: ")
    p_num_cores = int(input("insert smartphone num cores: "))
    p_cam_res = float(input("insert smartphone cam res: "))
    smartphone = Smartphone(p_id, p_brand, p_model, p_year, p_price, p_cell_net, p_num_cores, p_cam_res)
    store += smartphone


def create_laptop(store):
    p_id = int(input("insert laptop id: "))
    p_brand = input("insert laptop brand: ")
    p_model = input("insert laptop model: ")
    p_year = int(input("insert laptop year: "))
    p_price = float(input("insert laptop price: "))
    p_CPU = input("insert laptop CPU: ")
    p_hard_disk = int(input("insert laptop hard disk: "))
    p_screen = float(input("insert laptop screen: "))
    laptop = Laptop(p_id, p_brand, p_model, p_year, p_price, p_CPU, p_hard_disk, p_screen)
    store += laptop


def create_product(store):
    while True:
        prod_type = input("enter 1 for laptop, 2 for smartphone: ")
        if prod_type == "1":
            create_laptop(store)
            break
        elif prod_type == "2":
            create_smartphone(store)
            break
        else:
            print("invalid product type")

def create_customer(store):
    c_id = int(input("insert client id: "))
    c_name = input("insert client name: ")
    c_email = input("insert client email:")
    c_address = input("insert client address:")
    c_number = int(input("insert client phone number: "))
    c_gender = input("insert client gender: ").upper()
    if c_gender not in ["M", "F"]:
        c_gender = "M"
    client = Client(c_id, c_name, c_email, c_address, c_number, c_gender)
    store.add_client(client)

def delete_product(store):
    p_id = int(input("enter product id: "))
    if store.remove_product(p_id):
        print(f"{p_id} deleted!")
    else:
        print(f"{p_id} not exist!")

def delete_customer(store):
    c_id = int(input("enter client id: "))
    if store.remove_client(c_id):
        print(f"{c_id} deleted!")
    else:
        print(f"{c_id} not exist!")

def print_product_under_price(store):
    price = float(input("insert a maximum price: "))
    result = store.get_all_by_price_under(price)
    print(f"---- All products under price: {price}")
    for product in result:
        print(product)

def print_most_expensive_product(store):
    product = store.get_most_expensive_product()
    print(f"The most expensive product is: {product}")

def print_phone_number_list(store):
    phones = store.get_all_phones()
    for phone in phones:
        print(phone)

def print_computer_list(store):
    laptops = store.get_all_laptops()
    for laptop in laptops:
        print(laptop)

def print_average_phone_price(store):
    avg = store.phone_average_price()
    print(f"average phone price: {avg}")

def print_the_biggest_screen(store):
    max_screen = store.get_max_screen()
    print(f"max screen size: {max_screen}")

def print_common_came(store):
    common_cam = store.get_common_cam()
    print(f"most common camera: {common_cam}")

def print_popular_prods(store):
    popular_prods = store.list_popular()
    for product in popular_prods:
        print(product)

def print_shirt_list(store):
    store.print_shirts()

def create_new_reservation(store):

    while True:
        try:
            product_id = int(input("please enter product id: "))
            if product_id not in store.products:
                raise ProductNotInStore("invalid product id")
            client_id = int(input("please enter client id: "))
            if client_id not in store.clients:
                raise ClientNotFoundError("invalid client id")
            quantity = int(input("please enter quantity: "))
            if quantity <= 0:
                raise ValueError("please enter quantity bigger than 0")
            store.add_order(client_id, product_id, quantity)
            break
        except ValueError as error:
            print(error)
        except ProductNotInStore as error:
            print(error)
        except ClientNotFoundError as error:
            print(error)
        except ShirtNotFoundError as error:
            print(error)


def print_all_orders(store):
    store.print_orders()


def bonus(analysis):
    try:
        order_path = input("enter orders.csv file path: ")
        analysis.bonus(order_path)
    except Exception as error:
        print(error)


def create_store(products_path, clients_path, orders_path, shirts_path):
    return SuperStore(products_path, clients_path, orders_path, shirts_path)


def create_analysis(store):
    return ShirtOrdersAnalysis(store)


def run(store, analysis):
    while True:
        print_menu()
        user_choice = input("What is your choice: ")
        try:
            if user_choice == "1":
                print_all_products(store)
            elif user_choice == "2":
                print_all_clients(store)

            elif user_choice == "3":
                create_product(store)
                #store.add_product(product)

            elif user_choice == "4":
                create_customer(store)

            elif user_choice == "5":
                delete_product(store)

            elif user_choice == "6":
                delete_customer(store)

            elif user_choice == "7":
                print_product_under_price(store)

            elif user_choice == "8":
                print_most_expensive_product(store)

            elif user_choice == "9":
                print_phone_number_list(store)

            elif user_choice == "10":
                print_computer_list(store)

            elif user_choice == "11":
                print_average_phone_price(store)

            elif user_choice == "12":
                print_the_biggest_screen(store)

            elif user_choice == "13":
                print_common_came(store)

            elif user_choice == "14":
                print_popular_prods(store)

            elif user_choice == "15":
                print_shirt_list(store)

            elif user_choice == "16":
                create_new_reservation(store)

            elif user_choice == "17":
                print_all_orders(store)

            elif user_choice == "18":
                print("by by")
                break

            elif user_choice.upper() == "B":
                bonus(analysis)
        except Exception as error:
            print(error)


def main():
    args = sys.argv
    # "products_supply.csv", "clients.csv", "orders.csv","shirts.csv"
    store = create_store(args[1], args[2], args[3], args[4])
    analysis = create_analysis(store)
    run(store, analysis)


if __name__ == "__main__":
    main()


