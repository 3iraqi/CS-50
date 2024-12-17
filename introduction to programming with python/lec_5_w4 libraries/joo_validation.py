userNamesAndPassword=[
        {"name": "Joo", "password": "123"},
        {"name": "Mohamed", "password": "456"},
        {"name": "Karim", "password": "789"},
        {"name": "Yara", "password": "012"},
        {"name": "Omnia", "password": "345"}
    ]
def main():
    userName= validate_userName()
    password=validate_password()
    
    print(f"Login Successful | User: {userName}")
    print(f"Password: {len(password)*'*'}")
    # if not userName or not password:
    #     print("Invalid User Name or Password")
    # else:
    #     print("Login Successful")
    ...

def validate_userName():
    # while True:
        try:
            userName= input("Enter User Name: ")
            if  not  any(userName == user["name"] for user in userNamesAndPassword ):
                raise ValueError("Invalid User Name")
        except ValueError:
            print("Invalid User Name | Try again")
        else:
            return userName

def validate_password():
    # while True:
        try:
            password =input("Enter User Password: ")
            if  not  any(password == user["password"] for user in userNamesAndPassword ):
                raise ValueError("Invalid User Password | Try again")
        except ValueError:
            print("Invalid User Name | Try again")
        else:
            return password
        
            
        
    
    
    
if __name__ == "__main__":
    main()