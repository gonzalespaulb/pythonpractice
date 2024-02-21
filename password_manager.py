from cryptography.fernet import Fernet

def make_a_file(): 
    with open("test.txt", 'w') as file:
        file.write("this is a text file!!")
        print("file has been made!")

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key) 

"""
pwd = "paugito"
test = fer.encrypt(pwd.encode()).decode()
test1 = fer.decrypt(test.encode()).decode()
"""

def view():
    with open("passwords.txt", "r") as f: 
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ",", "Password:", fer.decrypt(passw.encode()).decode())

def add(): 
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True: 
    mode = input("Add or view passwords? a: add / v: view / q: quit ").lower()

    if mode == "q": 
        break

    if mode == "v": 
        view()

    elif mode == "a": 
        add()

    else: 
        print("Invalid Mode")
        continue