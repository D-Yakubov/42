class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def full_address(self):
        return f"{self.street}, {self.city}, {self.country}."


address = Address("Pokdil 35","Turtkul","Uzbekistan")
print(address.full_address())
