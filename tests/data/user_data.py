from faker import Faker
f = Faker('ru_RU')


class UsersData:
    def __init__(self):
        self.name = f.first_name()
        self.last_name = f.last_name()
        self.country = "Россия"
        self.address = f.address()
        self.city = f.city()
        self.state = f.region()
        self.postal_code = f.postcode()
        self.phone = f.phone_number()
        self.email = f.ascii_free_email()
