import os

if not os.path.exists('vehicle_dashboard.txt'):
    with open('vehicle_dashboard.txt', 'w') as file:
        file.write('Fleet Services,100,100,0')

# Function definitions:

def display_dashboard(l_indicator, speed, fuel, r_indicator):
    if len(str(fuel)) == 1:
        print('****************DASHBOARD****************')
        print('+---------+---------+---------+---------+')
        print('|   LI    |  Speed  |   Fuel  |    RI   |')
        print('+=========+=========+=========+=========+')
        print(f'|   {l_indicator}   |   {speed}    |    {fuel}    |   {r_indicator}   |')
        print('+---------+---------+---------+---------+')
    # Alternatives to prevent bigger value lengths ruining dashboard's shape:
    elif len(str(fuel)) == 2:
        print('****************DASHBOARD****************')
        print('+---------+---------+---------+---------+')
        print('|   LI    |  Speed  |   Fuel  |    RI   |')
        print('+=========+=========+=========+=========+')
        print(f'|   {l_indicator}   |   {speed}    |    {fuel}   |   {r_indicator}   |')
        print('+---------+---------+---------+---------+')
    else:
        print('****************DASHBOARD****************')
        print('+---------+---------+---------+---------+')
        print('|   LI    |  Speed  |   Fuel  |    RI   |')
        print('+=========+=========+=========+=========+')
        print(f'|   {l_indicator}   |   {speed}    |   {fuel}   |   {r_indicator}   |')
        print('+---------+---------+---------+---------+')

def display_locations(current_location):
    locations = ['Eden Project', 'Stonehenge', 'Cheddar Gorge']
    if current_location in locations:
        locations[locations.index(current_location)] = 'Fleet Services'
    return locations

def save_progress(location, fuel_volume, money, strikes):
    with open('vehicle_dashboard.txt', 'w') as file:
        file.write(f'{location},{fuel_volume},{money},{strikes}')

def reset_file():
    with open('vehicle_dashboard.txt', 'w') as file:
        file.write('Fleet Services,100,100,0')

# MAIN

with open('vehicle_dashboard.txt', 'r') as file:
    data = file.read().split(',')

driver_data = {
    'location' : data[0],
    'fuel_volume' : int(data[1]),
    'money' : int(data[2]),
    'strikes' : int(data[3])
}

current_location = driver_data['location']

is_stationary = True
driving = True

speeds_mins = { # Times taken for driving at certain speeds
    '5' : 1,
    '15' : 1,
    '25' : 3,
    '35' : 3,
    '45' : 3,
    '55' : 5,
    '65' : 5,
    '75' : 10,
    '85' : 15,
    '95' : 20,
    '105' : 30
}

print('****************DASHBOARD****************')
print('+---------+---------+---------+---------+')
print()
print('================ WELCOME ================')
print()
print('+---------+---------+---------+---------+')

while True:
    print(f'You are at {current_location}')

    while is_stationary:
        print('1: Start driving')
        print('2: Check')
        print('3: Explore location')
        print('4: Turn off')
        selection = input()
        if selection == '1':
            print('Where to?')
            for i, location in enumerate(display_locations(current_location), 1):
                print(f'{i}: {location}')
            try:
                num = int(input())
                if num <= 0: raise IndexError
                location_to = display_locations(current_location)[num-1]
                break
            except ValueError:
                print('Error: output not a number')
            except IndexError:
                print('Error: invalid number')
        elif selection == '2':
            print('Fuel:', f"{driver_data['fuel_volume']} litres")
            print('Credits:', f"£{driver_data['money']}")
            print('License:', f"{driver_data['strikes']} strike(s)")
        elif selection == '3':
            if current_location == 'Fleet Services':
                print('1: Get petrol (cost: £15)')
                print('2: Get money')
                print('3: Back')
                selection = input()
                if selection == '1':
                    if driver_data['fuel_volume'] >= 100:
                        print('Fuel already at maximum')
                    else:
                        if driver_data['money'] < 15:
                            print('Not enough money')
                        else:
                            driver_data['fuel_volume'] = 100
                            driver_data['money'] -= 15
                            print('Fuel restored at maximum')
                elif selection == '2':
                    if driver_data['money'] >= 100:
                        print('Money already at maximum')
                    else:
                        driver_data['money'] = 100
                        print('Money restored at maximum')
                elif selection == '3':
                    continue
                else:
                    print('Invalid choice')
            if current_location == 'Eden Project':
                print('1: View the technological constructs (cost £15)')
                print('2: Back')
                selection = input()
                if selection == '1':
                    if driver_data['money'] < 15:
                        print('Not enough money')
                    else:
                        driver_data['money'] -= 15
                        print('Toured Eden Project')
                elif selection == '2':
                    continue
                else:
                    print('Invalid choice')
            if current_location == 'Stonehenge':
                print('1: View the pillars of stone (cost £15)')
                print('2: Back')
                selection = input()
                if selection == '1':
                    if driver_data['money'] < 15:
                        print('Not enough money')
                    else:
                        driver_data['money'] -= 15
                        print('Toured Stonehenge')
                elif selection == '2':
                    continue
                else:
                    print('Invalid choice')
            if current_location == 'Cheddar Gorge':
                print('1: Explore the dark caves (cost £15)')
                print('2: Back')
                selection = input()
                if selection == '1':
                    if driver_data['money'] < 15:
                        print('Not enough money')
                    else:
                        driver_data['money'] -= 15
                        print('Toured Cheddar Gorge')
                elif selection == '2':
                    continue
                else:
                    print('Invalid choice')
        elif selection == '4':
            save_progress(*driver_data.values())
            print('****************DASHBOARD****************')
            print('+---------+---------+---------+---------+')
            print()
            print('================ GOODBYE ================')
            print()
            print('+---------+---------+---------+---------+')
            exit()
        else:
            print('Invalid choice. Type corresponding number.')

    # Assigning variables before driving
    roads = ['slip road', 'motorway', 'overtake lane']
    min_sp_limits = [40, 60, 80]
    max_sp_limits = [70, 90, 100]
    pos = 1
    current_road = roads[pos]
    travelling_data = {
        'l_indicator' : 'Off',
        'speed' : 75,
        'fuel' : driver_data['fuel_volume'],
        'r_indicator' : 'Off'
    }
    if current_location == 'Fleet Services':
        distance_to = 30
    else:
        if location_to == 'Fleet Services':
            distance_to = 30
        else:
            distance_to = 70
    
    while driving:
        display_dashboard(*travelling_data.values())
        print(
            f'Driving to {location_to} on the {current_road}.',
            f'Min. speed limit: {min_sp_limits[pos]},',
            f'max. speed limit: {max_sp_limits[pos]}'
            )
        while distance_to > 0:
            print('Time to destination:', f'{distance_to} minutes')
            print('Select controls:')
            print('1: Left indicator')
            print('2: Right indicator')
            print('3: Accelerate')
            print('4: Decelerate')
            selection = input()
            if selection == '1':
                try:
                    pos = pos - 1
                    if pos < 0: raise IndexError
                    current_road = roads[pos]
                    travelling_data['l_indicator'] = 'On '  # Extra space to preserve dashboard's shape
                    travelling_data['r_indicator'] = 'Off'
                    display_dashboard(*travelling_data.values())
                    print(
                        f'Turning into {current_road}.',
                        f'Min. speed limit: {min_sp_limits[pos]},',
                        f'max. speed limit: {max_sp_limits[pos]}',
                        'BE IN THIS RANGE'
                    )
                except IndexError:
                    print('No left turn on slip road')
                    pos = pos + 1
            elif selection == '2':
                try:
                    pos = pos + 1
                    current_road = roads[pos]
                    travelling_data['l_indicator'] = 'Off'
                    travelling_data['r_indicator'] = ' On'
                    display_dashboard(*travelling_data.values())
                    print(
                        f'Turning into {current_road}.',
                        f'Min. speed limit: {min_sp_limits[pos]},',
                        f'max. speed limit: {max_sp_limits[pos]}',
                        'BE IN THIS RANGE'
                    )
                except IndexError:
                    print('No right turn on overtake lane')
                    pos = pos - 1
            elif selection == '3':
                travelling_data['fuel'] -= 10
                travelling_data['speed'] += 10
                distance_to -= speeds_mins[str(travelling_data['speed'])]
                travelling_data['l_indicator'] = 'Off'
                travelling_data['r_indicator'] = 'Off'
                if travelling_data['fuel'] <= 0:
                    print('NOOOOOOOO!!! Out of fuel.')
                    print('DRIVE ENDED')
                    reset_file()
                    exit()
                if travelling_data['speed'] < min_sp_limits[pos] or travelling_data['speed'] > max_sp_limits[pos]:
                    print('OOPS. Drove out of speed range')
                    print(f'£50 fine for doing {travelling_data["speed"]} in {min_sp_limits[pos]}-{max_sp_limits[pos]} zone')
                    driver_data['money'] -= 50
                    if driver_data['money'] < 0:
                        print('NOOOOOOOO!!! Out of money.')
                        print('DRIVE ENDED')
                        reset_file()
                        exit()
                    print(f'£{driver_data["money"]} left')
                    driver_data['strikes'] += 1
                    print(f'Strike {driver_data["strikes"]} of 3 received')
                    if driver_data['strikes'] >= 3:
                        print('OOOOOOOPS! Strike limit reached. Driving ban received.')
                        print('DRIVE ENDED')
                        reset_file()
                        exit()
                    if current_road == 'slip road': travelling_data['speed'] = 55
                    if current_road == 'motorway': travelling_data['speed'] = 75
                    if current_road == 'overtake lane': travelling_data['speed'] = 85
                    input('Press ENTER to continue')
                if distance_to <= 0: break
                display_dashboard(*travelling_data.values())
                print(
                    f'Driving to {location_to} on the {current_road}.',
                    f'Min. speed limit: {min_sp_limits[pos]},',
                    f'max. speed limit: {max_sp_limits[pos]}'
                    )
            elif selection == '4':
                travelling_data['fuel'] -= 5
                travelling_data['speed'] -= 10
                distance_to -= speeds_mins[str(travelling_data['speed'])]
                travelling_data['l_indicator'] = 'Off'
                travelling_data['r_indicator'] = 'Off'
                if travelling_data['fuel'] <= 0:
                    print('NOOOOOOOO!!! Out of fuel.')
                    print('DRIVE ENDED')
                    reset_file()
                    exit()
                if travelling_data['speed'] < min_sp_limits[pos] or travelling_data['speed'] > max_sp_limits[pos]:
                    print('OOPS. Drove out of speed range')
                    print(f'£50 fine for doing {travelling_data["speed"]} in {min_sp_limits[pos]}-{max_sp_limits[pos]} zone')
                    driver_data['money'] -= 50
                    if driver_data['money'] < 0:
                        print('NOOOOOOOO!!! Out of money.')
                        print('DRIVE ENDED')
                        reset_file()
                        exit()
                    print(f'£{driver_data["money"]} left')
                    driver_data['strikes'] += 1
                    print(f'Strike {driver_data["strikes"]} of 3 received')
                    if driver_data['strikes'] >= 3:
                        print('OOOOOOOPS! Strike limit reached. Driving ban received.')
                        print('DRIVE ENDED')
                        reset_file()
                        exit()
                    if current_road == 'slip road': travelling_data['speed'] = 55
                    if current_road == 'motorway': travelling_data['speed'] = 75
                    if current_road == 'overtake lane': travelling_data['speed'] = 85
                    input('Press ENTER to continue')
                if distance_to <= 0: break
                display_dashboard(*travelling_data.values())
                print(
                    f'Driving to {location_to} on the {current_road}.',
                    f'Min. speed limit: {min_sp_limits[pos]},',
                    f'max. speed limit: {max_sp_limits[pos]}'
                    )
            else:
                print('Invalid choice. Select corresponding number.')
        print('****************DASHBOARD****************')
        print('+---------+---------+---------+---------+')
        print()
        print('========== DESTINATION REACHED ==========')
        print()
        print('+---------+---------+---------+---------+')
        driver_data['location'] = location_to
        driver_data['fuel_volume'] = travelling_data['fuel']
        current_location = driver_data['location']
        save_progress(*driver_data.values())
        break
