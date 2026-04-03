# eCitizen Login - Python
def login():
    username_db = "adminKE"
    password_db = "254Secure"

    user_input = input("Enter Username: ")
    pass_input = input("Enter Password: ")

    if user_input == username_db and pass_input == password_db:
        print("Access Granted")
    else:
        print("Invalid Credentials")

if __name__ == "__main__":
    login()