class Client:

    def __init__(self, client_id, name, email, address, phone_number, gender):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.gender = gender

    def print_me(self, p1):
        print("----", self.client_id, "----")
        print("name:", self.name)
        print("email:", self.email)
        print("address:", self.address)
        print("phone_number:", self.phone_number)
        print("gender:", self.gender)

    def __str__(self):
        return f"{self.client_id}, {self.name}, {self.email}, {self.address},  {self.phone_number}, {self.gender}"


    def __repr__(self):
        return str(self)

