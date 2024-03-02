class Order:

    def __init__(self, order_id, client_id, product_id, quantity):
        self.order_id = order_id
        self.product_id = product_id
        self.client_id = client_id
        self.quantity = quantity

    def __str__(self):
        return f"order id: {self.order_id}, product id: {self.product_id}, client id: {self.client_id}, quantity: {self.quantity}"

    def __repr__(self):
        return str(self)

