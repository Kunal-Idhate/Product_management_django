from home.models import Product

from faker import Faker

fake = Faker()

def seed():
    for i in range(0,10):
        Product.objects.create(
            shape = fake.word(),
            price = fake.random_number(digits=2),
            location = fake.address(),
            size = fake.random_number(digits=2),
        )