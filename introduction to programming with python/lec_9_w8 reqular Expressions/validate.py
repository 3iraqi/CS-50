email = input("what is your email? ").strip()

user_name, domain = email.split("@")

## first way
# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

## Second way
if user_name and "." in domain:
    print("Valid")
else:
    print("Invalid")