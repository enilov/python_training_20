from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["num of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n =5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", middlename="",
                    homephone="3333", mobilephone="5555" ,workphone="1111", secondaryphone="2222",
                    email="1@mail.ru",email2="2@mail.ru",email3="3@mail.ru", address="addrr",) ] + \
           [
               Contact(firstname=random_string("firstname", 10),
                     lastname=random_string("lastname", 20),
                     middlename=random_string("middlename", 20),
                       homephone="3333", mobilephone="5555" ,workphone="1111", secondaryphone="2222",
                       email="1@mail.ru",email2="2@mail.ru",email3="3@mail.ru", address="addrr",)
               for name in range(n)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))