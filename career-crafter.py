# Sections
forename_section = True
surname_section = True
age_section = True
email_section = True
phone_section = True

# Main program
while forename_section:
    first_name = input("Enter your forename: ")
    if not first_name.isalpha():  # Letters only
        print("Invalid forename. \n")
    else:
        forename_section = False  # To break out of while loop

while surname_section:
    surname = input("Enter your surname: ")
    if not surname.isalpha():  # Letters only
        print("Invalid surname. \n")
    else:
        surname_section = False

while age_section:
    try:
        age = input("Enter your age (must be 19 or over): ")
        if not age.isnumeric():  # Numbers only
            raise Exception("Error: You have inserted something invalid.")
        if int(age) < 19:
            print("This age cannot be accepted. \n")
            break  # Break out to end program
        else:
            age_section = False
    except Exception as err:
        print(err, "\n")

if int(age) < 19:  # Code for rejected ages
    email_section = False  # Remaining sections will not be accessed
    phone_section = False
    print("Sorry, you cannot go further.")  # End of program for rejected ages

while email_section:
    email = input("Enter your email: ")
    if '@' not in email or '.' not in email:
        print("Invalid email. \n")
    else:
        email_section = False

while phone_section:
    phone_no = input("Enter your phone number: ")
    if phone_no[:2] == '07':
        if phone_no.isdigit() and len(phone_no) == 11:
            phone_section = False
        else:
            print('Invalid phone number.\n')
    elif phone_no[:3] == '+44':
        if phone_no[1:].isdigit() and len(phone_no) == 13:
            phone_section = False
        else:
            print('Invalid phone number.\n')
    else:  # For anything else
        print('Invalid phone number.\n')

if int(age) >= 19:  # Blocked by if condition to prevent NameError
    print("\nSummary:")
    print("Fullname:", first_name, surname)
    print("Age:", age)
    print("Email:", email)
    print("Phone:", phone_no)
