forename_section = True
surname_section = True
age_section = True
email_section = True
phone_section = True

while forename_section:
    first_name = input("Enter your forename: ")
    if not first_name.isalpha():
        print("Invalid forename. \n")
    else:
        forename_section = False

while surname_section:
    surname = input("Enter your surname: ")
    if not surname.isalpha():
        print("Invalid surname. \n")
    else:
        surname_section = False

while age_section:
    try:
        age = input("Enter your age (must be 19 or over): ")
        if not age.isnumeric():
            raise Exception("Error: You have inserted something invalid.")
        if int(age) < 19:
            print("This age cannot be accepted. \n")
            break
        else:
            age_section = False
    except Exception as err:
        print(err, "\n")

if int(age) < 19:
    email_section = False
    phone_section = False
    print("Sorry, you cannot go further.")

while email_section:
    email = input("Enter your email: ")
    if '@' not in email or '.' not in email:
        print("Invalid email. \n")
    else:
        email_section = False

while phone_section:
    phone_no = input("Enter your phone number: ")
    if len(phone_no) != 10 or not phone_no.isdigit():
        print("Invalid phone number. \n")
    else:
        phone_section = False

print("\nSummary:")
print("Fullname:", first_name, surname)
print("Age:", age)
print("Email:", email)
print("Phone:", phone_no)