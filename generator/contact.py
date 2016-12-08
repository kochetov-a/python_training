# -*- coding: utf-8 -*-

from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file="])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(prefix, maxlen):
    symbols = string.digits
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    symbols = string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) \
           + "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) \
           + ".".join([random.choice(symbols) for i in range(random.randrange(3))])

# Генерация тестовых данных
data_for_contact = [Contact(first_name="", last_name="")] + [
    Contact(first_name=random_string("first_name", 20), last_name=random_string("last_name", 20),
            second_name=random_string("second_name", 20), company_name=random_string("company_name", 20),
            home_phone=random_number("home_phone", 20), email=random_email(20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:  # Открываем файл на запись
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(data_for_contact))