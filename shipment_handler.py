import os

from datetime import date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

todays_date = date.today().strftime(DATETIME_STRING_FORMAT)

select_textfile_menu = True
view_textfile_menu = True

files = []

if not os.path.exists('shipments_initial.txt'):  # Creates file on first use
    with open('shipments_initial.txt', 'w') as file:
        file.write('2023-12-09 | Order placed | 1 | London | Electronics\n')
        file.write('2023-12-09 | Order accepted | 2 | Manchester | Electronics\n')
        file.write('2023-12-09 | Order shipped | 3 | Edinburgh | Electronics\n')
        file.write('2023-12-09 | Order delivered | 4 | Manchester | Electronics\n')
        file.write('2023-12-09 | Order placed | 5 | London | Electronics\n')
        file.write('2023-12-11 | Order accepted | 6 | London | Electronics\n')
        file.write('2023-12-11 | Order shipped | 7 | London | Electronics\n')
        file.write('2023-12-11 | Order delivered | 8 | Edinburgh | Electronics\n')
        file.write('2023-12-11 | Order placed | 9 | Manchester | Electronics\n')
        file.write('2023-12-11 | Order delivered | 10 | Manchester | Electronics\n')

if not os.path.exists('shipments_files.txt'):  # Saves files in use
    with open('shipments_files.txt', 'w') as file:
        file.write('shipments_initial.txt')
        file.write('\n')

with open('shipments_files.txt', 'r') as file:  # Adds the files for use during run of program
    for line in file:
        files.append(line.strip('\n'))

files = [shipment_file for shipment_file in files if os.path.exists(shipment_file)]
# In case files on shipments_files.txt do not exist in directory

if not 'shipments_initial.txt' in files and len(files) == 0:  # Special case upon an action outside of program
    files.append('shipments_initial.txt')
    with open('shipments_files.txt', 'w') as file:
        file.write('shipments_initial.txt')
        file.write('\n')

# Function definitions

def generate_shipments_file(file_name, num, location, type):
    with open(file_name, 'w') as file:
        for i in range(1, num+1):
            file.write(f'{todays_date} | Order placed | {i} | {location} | {type}\n')
    files.append(file_name)
    with open('shipments_files.txt', 'w') as file:
        for shipment_file in files:
            file.write(shipment_file)
            file.write('\n')

def update_shipment(shipment, trait, edition):
    if trait == 'location':
        shipment[3] = f' {edition} '
    if trait == 'order type':
        shipment[4] = f' {edition}'
    shipment[0] = todays_date
    updated_shipment = '|'.join(shipment)
    line_list.append(updated_shipment)
    del line_list[single_number-1]
    unfilter_list.append(updated_shipment)
    del unfilter_list[unfilter_list.index(curr_shipment)]
    with open(selected_file, 'w') as file:
        for order in unfilter_list:
            file.write(order)
            file.write('\n')

# === MAIN ===

print('Welcome to Shipment Handler')
print('View lists of shipments and analyse or edit them.')
print()

while select_textfile_menu:
    print('Please type in the .txt file you want to view. Currently available files:')
    print(*files, sep=', ', end='\n\n')
    print('Type /new to create new list of shipments. Type /exclude to remove a file from editing.')
    print('Type /quit to exit')
    textfile = input()
    selected_file = textfile + '.txt' if textfile[-4:] != '.txt' else textfile  # Read with and without .txt

    if textfile == '/quit':
        break

    if textfile == '/exclude':  # Removing file from list, does not remove from directory
        if len(files) == 1:
            print('\nYou cannot remove a file if there is only one available.')
            continue
        print('Type one from the following files that you want to exclude:')
        print(*files, sep=', ')
        excluded_file = input()
        mod_excluded_file = excluded_file + '.txt' if excluded_file[-4:] != '.txt' else excluded_file
        if not mod_excluded_file in files:
            print('\nSorry. Unrecognised file typed.')
            continue
        yes_or_no = input('This selected file will no longer be available for editing/analysing. Are you sure you want to do this? (Y/n): ')
        if yes_or_no == 'Y':
            files.remove(mod_excluded_file)
            with open('shipments_files.txt', 'w') as file:
                for shipment_file in files:
                    file.write(shipment_file)
                    file.write('\n')
            print('File removed.')
        print()
        continue

    if textfile == '/new':  # Creating new shipments file
        shipments_num = input('Please type the number of shipments in your new shipments file (max 50): ')
        if not shipments_num.isdigit():
            print('\nError: Invalid input. Type whole number.')
            continue
        elif int(shipments_num) > 50 or int(shipments_num) == 0:
            print('\nYou cannot have 0 or more than 50 shipments.')
            continue
        else:
            pass
        shipment_location = input('Type the location that you are sending the shipments to: ')
        shipment_type = input('Enter the type of the shipment products: ')
        file_name = input('Type in the name of your file: ')
        mod_file_name = file_name + '.txt' if file_name[-4:] != '.txt' else file_name  # Read with and without .txt
        if mod_file_name in files:
            print('\nFile already exists.')
            continue
        else:
            generate_shipments_file(mod_file_name, int(shipments_num), shipment_location, shipment_type)
            yes_or_no = input('File generated. Do you want to view this file? (Y/n): ')
            if yes_or_no == 'Y':
                selected_file = mod_file_name
            else:
                continue
    
    try:
        with open(selected_file, 'r') as file:  # Check if file exists
            if not selected_file in files:  # Check if file is being staged for editing
                print("\nSorry. You cannot use this file.")
            else:
                unfilter_list = [line.strip('\n') for line in file]
                line_list = unfilter_list.copy()
                print()

                for i, line in enumerate(line_list, 1):
                    print(f"Order {i}:", line)
                print(f"\nYou are viewing {selected_file}.")

                while view_textfile_menu:
                    print('Please select one of the following actions: (analyse, edit, filter, re-read, reset).')
                    print('Type /back to go back.')
                    print('Type /quit to exit.')
                    action = input()

                    if action == '/quit':
                        textfile = '/quit'
                        break
                    if action == '/back':
                        break

                    elif action == 'edit':
                        print('Type one from the following options:')
                        print('change order status')
                        print('update')
                        edit_action = input()
                        if edit_action != 'change order status' and edit_action != 'update':
                            print('Invalid option.\n')
                            continue
                        print()
                        for i, line in enumerate(line_list, 1):
                            print(f"Order {i}:", line)
                        print()
                        try:
                            single_number = int(input("Select the order you want to edit (leftmost number).\n"))
                            if single_number > len(line_list) or single_number <= 0:
                                print("Error: Number out of range\n")
                                continue
                            else:
                                pass
                        except ValueError:
                            print("Error: Invalid input\n")
                            continue
                        sub_list = line_list[single_number-1].split('|')
                        curr_shipment = line_list[single_number-1]
                        curr_status = sub_list[1][7:].strip()  # placed, accepted, shipped or delivered (without 'Order')
                        if edit_action == 'change order status':
                            status_list = ['placed', 'accepted', 'shipped', 'delivered']
                            if curr_status == 'delivered':
                                print('\nYou cannot change the status if the order has been delivered.')
                                continue
                            mod_status_list = status_list[status_list.index(curr_status)+1:]
                            # e.g [accepted, shipped, delivered] if curr_status == placed

                            yes_or_no = input(f'''Change status to '{mod_status_list[0]}'? (Y/n): ''')
                            if yes_or_no == 'Y':
                                sub_list[1] = f' Order {mod_status_list[0]} '
                                edition = '|'.join(sub_list)
                                line_list[single_number-1] = edition
                                unfilter_list[unfilter_list.index(curr_shipment)] = edition
                                with open(selected_file, 'w') as file:
                                    for order in unfilter_list:
                                        file.write(order)
                                        file.write('\n')
                                print('Successfully changed status')
                            else:
                                print('Status not changed')
                        elif edit_action == 'update':
                            if curr_status != 'placed':
                                print('\nYou can only update orders that are placed.')
                                continue
                            print('Type one from the following options to edit:')
                            print('location')
                            print('order type')
                            print("The date will also be changed (to today's date) and the order will be moved to the end.")
                            updated_option = input()
                            if updated_option != 'location' and updated_option != 'order type':
                                print('Invalid option.\n')
                                continue
                            edition = input(f'Type in your new {updated_option}: ')
                            update_shipment(sub_list, updated_option, edition)
                            print('Successfully updated order.')
                            
                    elif action == 'filter':
                        filter_list = []
                        filter_action = input('Please select your filter (date, order status, location, order type)\n')
                        if filter_action == 'date':
                            selected_date = input('Select the date (YYYY-MM-DD).\n')
                            print()
                            for line in line_list:
                                sub_list = line.split('|')
                                if sub_list[0].strip() == selected_date:
                                    filter_list.append(line)
                            if len(filter_list) == 0:
                                print('Sorry. None of the results match your date.\n')
                            else:
                                line_list = filter_list.copy()
                                for i, line in enumerate(line_list, 1):
                                    print(f'Order {i}:', line)
                                print("\nThe above list will be used for your edits/further filters. Type 'reset' to revert to original.\n")
                        elif filter_action == 'order status':
                            status = input('Select order status (placed, accepted, shipped, delivered)\n')
                            status_list = ['placed', 'accepted', 'shipped', 'delivered']
                            if status not in status_list:
                                print('Invalid status\n')
                            else:
                                print()
                                for line in line_list:
                                    sub_list = line.split('|')
                                    if status in sub_list[1].strip():
                                        filter_list.append(line)
                                if len(filter_list) == 0:
                                    print("Sorry. None of the results match your status.\n")
                                else:
                                    line_list = filter_list.copy()
                                    for i, line in enumerate(line_list, 1):
                                        print(f"Order {i}:", line)
                                    print("\nThe above list will be used for your edits/further filters. Type 'reset' to revert to original.\n")
                        elif filter_action == "location":
                            location = input("Select the location.\n")
                            print()
                            for line in line_list:
                                sub_list = line.split('|')
                                if sub_list[3].strip() == location:
                                    filter_list.append(line)
                            if len(filter_list) == 0:
                                print("Sorry. None of the results match your location.\n")
                            else:
                                line_list = filter_list.copy()
                                for i, line in enumerate(line_list, 1):
                                    print(f"Order {i}:", line)
                                print("\nThe above list will be used for your edits/further filters. Type 'reset' to revert to original.\n")
                        elif filter_action == "order type":
                            order_type = input("Select the order type.\n")
                            print()
                            for line in line_list:
                                sub_list = line.split('|')
                                if sub_list[4].strip() == order_type:
                                    filter_list.append(line)
                            if len(filter_list) == 0:
                                print("Sorry. None of the results match your order type.\n")
                            else:
                                line_list = filter_list.copy()
                                for i, line in enumerate(line_list, 1):
                                    print(f"Order {i}:", line)
                                print("\nThe above list will be used for your edits/further filters. Type 'reset' to revert to original.\n")
                        else:
                            print("Invalid option.\n") 
               
                    elif action == "analyse":  # Ability to read orders in a quality documentation
                        analyse_action = input("Please select group of orders you want to analyse (all, upto, single).\n")
                        if analyse_action == "all":
                            print()
                            for i, line in enumerate(line_list, 1):
                                sub_list = line.split('|')
                                print(f"Order {i}:")
                                print("Date:", sub_list[0].strip())
                                print("Order status:", sub_list[1].strip())
                                print("Order number:", sub_list[2].strip())
                                print("Location:", sub_list[3].strip())
                                print("Order type:", sub_list[4].strip())
                                print()
                        elif analyse_action == "upto":
                            try:
                                print()
                                for i, line in enumerate(line_list, 1):
                                    print(f"Order {i}:", line)
                                print()                                
                                upto_number = int(input("Select the first n orders you want to analyse.\n"))
                                if upto_number > len(line_list) or upto_number <= 0:
                                    print("Error: Number out of range\n")
                                else:
                                    print()
                                    for i, line in enumerate(line_list[:upto_number], 1):
                                        sub_list = line.split('|')
                                        print(f"Order {i}:")
                                        print("Date:", sub_list[0].strip())
                                        print("Order status:", sub_list[1].strip())
                                        print("Order number:", sub_list[2].strip())
                                        print("Location:", sub_list[3].strip())
                                        print("Order type:", sub_list[4].strip())
                                        print()
                            except ValueError:
                                print("Error: Invalid input\n")
                        elif analyse_action == "single":
                            try:
                                print()
                                for i, line in enumerate(line_list, 1):
                                    print(f"Order {i}:", line)
                                print()
                                single_number = int(input("Select the order you want to analyse (leftmost number).\n"))
                                if single_number > len(line_list) or single_number <= 0:
                                    print("Error: Number out of range\n")
                                else:
                                    print()
                                    sub_list = line_list[single_number-1].split('|')
                                    print(f"Order {single_number}:")
                                    print("Date:", sub_list[0].strip())
                                    print("Order status:", sub_list[1].strip())
                                    print("Order number:", sub_list[2].strip())
                                    print("Location:", sub_list[3].strip())
                                    print("Order type:", sub_list[4].strip())
                                    print()
                            except ValueError:
                                print("Error: Invalid input\n")
                        else:
                            print("Invalid option.\n")

                    elif action == "re-read": # Re-outputs list of shipments so that users remain in track with it
                        for i, line in enumerate(line_list, 1):
                            print(f"Order {i}:", line)
                        else:
                            print()
    
                    elif action == "reset":  # Removes used filters. Will not move updated orders from end.
                        line_list = unfilter_list.copy()
                        print('Reverted back to original list.')
                        for i, line in enumerate(line_list, 1):
                            print(f"Order {i}:", line)
                        else:
                            print()
                    else:
                        print("Invalid option.\n")

    except FileNotFoundError:
        print("\nError: File was not found. Make sure it is in directory of this file.")
    except Exception:
        print('\nYour selected file does not appear to be in the correct format.')
    finally:
        if textfile == '/quit':
            break