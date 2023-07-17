import random


def generic_email():
    email = ("aleksandrkozlov11", str(random.randint(1000, 9999)), "@ya.ru")
    return email


def generic_password():
    return random.randint(100000, 999999)
