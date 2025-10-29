import re
email= input("Nhap email: ")
user_input = r'^\w+@\w+\.\w+$'
if re.match(user_input, email):
    print("Valid")
else:
    print("Invalid")