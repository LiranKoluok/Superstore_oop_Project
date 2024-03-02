import numpy as np
import matplotlib.pyplot as plt
from superStore import SuperStore
from exceptions import ShirtNotFoundError, ClientNotFoundError, DivideByZero


class ShirtOrdersAnalysis:
    def __init__(self, store):
        self.store = store
        self.orders = None

    def read_orders(self,orders_path):
        self.orders = np.genfromtxt(orders_path,delimiter=",",dtype=np.int32, skip_header=1)

    def add_payment(self):
        cost = np.array([np.apply_along_axis(self.get_price, 1, self.orders)], dtype=np.int32).T
        self.orders = np.hstack((self.orders, cost))

    def get_price(self, row):
        product_id = row[2]
        quantity = row[3]
        product = self.store.get_shirt(product_id)
        if product is None:
            raise ShirtNotFoundError(f"shirt with id: {product_id} not found!")
        return product.price * quantity

    def get_max_price_order(self):
        max_price = np.amax(self.orders, axis=0)[4]
        order = self.orders[(np.where(self.orders[:,4] == max_price))][0]
        order_id, client_id, product_id, quantity, price = order
        client = self.store.get_client(client_id)
        if client is None:
            raise ClientNotFoundError(f"client id: {client_id} not found!")
        client_name = client.name

        product = self.store.get_shirt(product_id)
        if product is None:
            raise ShirtNotFoundError(f"product id: {product_id} not found!")
        product_name = product.product_name
        print(f"order id: {order_id}, client name: {client_name}, product_name: {product_name}, order price: {price}")

    def print_client_history(self, client_id):
        client = self.store.get_client(client_id)
        if client is None:
            raise ClientNotFoundError(f"client id: {client_id} not found!")
        client_name = client.name
        orders = self.orders[(np.where(self.orders[:, 1] == client_id))]
        count = orders.shape[0]
        total_paid = np.sum(orders[:,4], axis=0)

        print(f"client name: {client_name}, number of orders: {count}, total paid: {total_paid}")

    def print_orders_over_average(self):
        sum_prices = np.sum(self.orders[:,4], axis=0)
        num_orders = self.orders.shape[0]
        if num_orders == 0:
            raise DivideByZero("number of orders is 0! can not divide by 0.")
        average_price = sum_prices / num_orders
        orders_above_average = self.orders[np.where(self.orders[:,4] > average_price)]
        print(orders_above_average)

    def get_order_frequencies(self):
        users, counts = np.unique(self.orders[:,1], return_counts=True)
        freqs = {str(user): counts[i] for i, user in enumerate(users)}
        return freqs

    def display_graph(self, freqs):
        plt.xlabel("users")
        plt.ylabel("orders count")
        plt.title("number of orders per client")
        plt.bar(freqs.keys(), freqs.values())
        plt.show()

    def bonus(self, order_path):
        self.read_orders(order_path)
        self.add_payment()
        freqs = self.get_order_frequencies()
        self.display_graph(freqs)


def main():
    store = SuperStore("products_supply.csv", "clients.csv", "orders.csv", "shirts.csv")
    analysis = ShirtOrdersAnalysis(store)
    analysis.read_orders("orders.csv")
    analysis.add_payment()
    print(analysis.orders)

    analysis.get_max_price_order()
    analysis.print_client_history(59769)
    analysis.print_orders_over_average()

    freqs = analysis.get_order_frequencies()
    analysis.display_graph(freqs)


if __name__ == "__main__":
    main()