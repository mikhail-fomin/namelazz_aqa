from random import randint, choice

from faker import Faker

class Generator:

    Faker.seed(randint(1, 999999999))
    faker = Faker("ru_RU")
    first_name = faker.first_name()
    last_name = faker.last_name()
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    date_of_birth = f"{randint(1,28)}{choice(months)}{randint(1960,2004)}"
    email = faker.email()
    password = faker.password()

    print(password)





