psw = input("What is the master password? ")
def view():
    with open("password.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            if "|" in line:
                user, passw = line.split('|')
                print("user: ", user, "|password: ", passw)
            else:
                print("invalid")


def add():
    name = input("Account name: ")
    psw1 = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + '|' + psw1 + "\n")


while True:
    mode = input("Would you like to add new password or view existing ones (view, add) ,or q for quit")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
