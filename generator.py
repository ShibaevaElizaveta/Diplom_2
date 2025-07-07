from faker import Faker

fake = Faker()

def generate_user_data():
    return {
        "email": fake.email(),
        "password": fake.password(length=10, special_chars=False),
        "name": fake.first_name()
    }

def generate_incorrect_user_data():
    return {
        "email": fake.email(),
        "password": fake.password(length=5, special_chars=False),
        "name": fake.first_name()
    }