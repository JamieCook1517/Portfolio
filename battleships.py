# This code does not work on WebAssembly platforms wasm32-emscripten and wasm32-wasi.

import os

import random

from asyncio import run, sleep

if not os.path.exists('battleships_files.txt'):
    with open('battleships_files.txt', 'w') as file:
        file.write('file1:\nfile2:\nfile3:\n')  # 'file1:file2:file3:' - string for no files saved

data = []

with open('battleships_files.txt', 'r') as file:
    for line in file:
        data.append(line.strip('\n'))

async def pause_message(message, sec):
    print(*message) if isinstance(message, tuple) else print(message)
    await sleep(sec)

in_game = True

co_ords = [
    'A1', 'A2', 'A3', 'A4', 'A5',
    'B1', 'B2', 'B3', 'B4', 'B5',
    'C1', 'C2', 'C3', 'C4', 'C5',
    'D1', 'D2', 'D3', 'D4', 'D5',
    'E1', 'E2', 'E3', 'E4', 'E5'
]
player_coordinates = co_ords.copy()
cpu_coordinates = co_ords.copy()
player_ship_coords = []
cpu_ship_coords = []

# MAIN

print()
print('=====BATTLESHIPS=====')
print()

while True:

    print('Select one from the following co-ordinates:', '\n',
        *co_ords[:5], '\n',
        *co_ords[5:10], '\n',
        *co_ords[10:15], '\n',
        *co_ords[15:20], '\n',
        *co_ords[20:],
        '\nType /load to continue saved game',
        '\nType /quit to exit'
        )

    selection = input()

    while True:
        if selection.upper() in co_ords:
            player_ship_coords.append(selection.upper())
            while selection != '/play':
                if selection.upper() not in co_ords:
                    print('\nPlease select a valid co-ordinate or command')
                print('Currently selected co-ordinates:', *player_ship_coords)
                print('Type in another co-ordinate to add (max. 5)')
                print(f'Or type /play to play {len(player_ship_coords)}v{len(player_ship_coords)}')
                selection = input()
                if selection.upper() in co_ords:
                    if selection.upper() in player_ship_coords:
                        print('\nAlready have this co-ordinate.')
                    else:
                        player_ship_coords.append(selection.upper())
                        if len(player_ship_coords) > 5:
                            print('\nYou cannot have more than 5 ships')
                            del player_ship_coords[-1]
                elif selection == '/quit':
                    exit()
                else:
                    pass
            cpu_ship_coords.extend(random.sample(co_ords,len(player_ship_coords)))
            print()
            print('='*77)
            print()
            game_begin_info = [
                'GAME BEGIN - ELIMINATE ENEMY SHIPS',
                ('CONFIRMED FRIENDLY SHIP CO-ORDINATES:', *player_ship_coords),
                ('Select from the following enemy co-ordinates to launch on:', '\n',
                    *co_ords[:5], '\n',
                    *co_ords[5:10], '\n',
                    *co_ords[10:15], '\n',
                    *co_ords[15:20], '\n',
                    *co_ords[20:], "(refers to opponent's grid, not yours)",
                    '\nType /save to save your game. Type /quit to exit.',
                    '\nOther commands: /status, /gridscan, /check'
                ),
                'WEAPONS HOT. READY TO LAUNCH'
            ]
            for element in game_begin_info:
                run(pause_message(element, 0.5))
            break
        elif selection == '/load':
            if ''.join(data) == 'file1:file2:file3:':  # No other information
                print('You currently have no games saved\nPlease select a co-ordinate or command')
                selection = input()
            else:
                while True:  # Load game
                    print('Select from the following files:')

                    # Displaying saved files:
                    print('FILE\t\tCO-ORDINATES')
                    for i, element in enumerate(data, 1):
                        if element != f'file{i}:':  # If line does not only contain fileN:
                            ships = element[element.index(':')+2:element.index(']')]  # Begin after [ to just before ]
                            ships_display = ships.replace("'", '')  # Remove quotation marks
                            print(f'{element[:element.index(':')]}\t\t{ships_display}')  # <filenum> <shipcoords>

                    print('Type /quit to exit')
                    file_select = input()
                    if file_select == 'file1' or file_select == '1':
                        index = 0
                        if data[0][-1] == ':': print('\nInvalid file choice')  # Empty file
                        else: break
                    elif file_select == 'file2' or file_select == '2':
                        index = 1
                        if data[1][-1] == ':': print('\nInvalid file choice')
                        else: break
                    elif file_select == 'file3' or file_select == '3':
                        index = 2
                        if data[2][-1] == ':': print('\nInvalid file choice')
                        else: break
                    elif file_select == '/quit':
                        exit()
                    else:
                        print('\nInvalid file choice')
                chosen_data = (data[index][data[index].index(':')+1:]).strip('\n')  # Remove fileN: and new line char
                erased_data = chosen_data.replace(' ', '').replace("'", '')  # Remove spaces and quotation marks
                split_data = erased_data.split(';')
                player_ship_coords = split_data[0].strip('[]').split(',') # Removing '[' and ']'
                player_coordinates = split_data[1].strip('[]').split(',')
                cpu_ship_coords = split_data[2].strip('[]').split(',')
                cpu_coordinates = split_data[3].strip('[]').split(',')
                print('Game loaded')
                print()
                print('='*77)
                print()
                game_load_info = [
                f'GAME RESUMED - ELIMINATE ENEMY SHIPS (REMAINING ENEMY SHIPS: {len(cpu_ship_coords)})',
                ('REMAINING FRIENDLY SHIP CO-ORDINATES:', *player_ship_coords),
                ('Select from the following enemy co-ordinates to launch on:', '\n',
                    *co_ords[:5], '\n',
                    *co_ords[5:10], '\n',
                    *co_ords[10:15], '\n',
                    *co_ords[15:20], '\n',
                    *co_ords[20:], "(refers to opponent's grid, not yours)",
                    '\nType /save to save your game. Type /quit to exit.',
                    '\nOther commands: /status, /gridscan, /check'
                ),
                'RETURN FIRE. BACK TO LAUNCHING'
                ]
                for element in game_load_info:
                    run(pause_message(element, 0.5))
                break
        elif selection == '/quit':
            exit()
        else:
            print('Invalid co-ordinate.\nPlease select a valid co-ordinate or command')
            selection = input()

    while in_game:

        launch_co_ord = input('Launch: ')
        if launch_co_ord.upper() in co_ords:
            if launch_co_ord.upper() in player_coordinates: 
                player_coordinates.remove(launch_co_ord.upper()) # For /gridscan
            if launch_co_ord.upper() in cpu_ship_coords:
                run(pause_message('HIT', 1))
                cpu_ship_coords.remove(launch_co_ord.upper())
                if len(cpu_ship_coords) == 0:
                    run(pause_message('ALL ENEMY SHIPS SUNK. VICTORY.', 3))
                    break
            else:
                run(pause_message('MISS', 1))
            cpu_launch = random.choice(cpu_coordinates)
            cpu_coordinates.remove(cpu_launch)
            run(pause_message('ENEMY LAUNCHES:', 1))
            run(pause_message(cpu_launch, 1))
            if cpu_launch in player_ship_coords:
                run(pause_message('HIT', 1))
                player_ship_coords.remove(cpu_launch)
                if len(player_ship_coords) == 0:
                    run(pause_message('ALL FRIENDLY SHIPS SUNK. GAME OVER.', 3))
                    break
            else:
                run(pause_message('MISS', 1))

        elif launch_co_ord == '/save':
            while True:
                print('Select file you want to save game on (file1, file2, file3)')
                print('Type /back to return to game')
                file_choice = input()
                if file_choice == 'file1' or file_choice == '1':
                    if data[0] != 'file1:':
                        print('File1 already has game data saved on. Do you want to overwrite it?')
                        yes_or_no = input('(Y/n): ')
                        if yes_or_no != 'Y':
                            print('File not saved')
                            continue
                    data[0] = f'file1:{player_ship_coords};{player_coordinates};{cpu_ship_coords};{cpu_coordinates}'
                    break
                elif file_choice == 'file2' or file_choice == '2':
                    if data[1] != 'file2:':
                        print('File2 already has game data saved on. Do you want to overwrite it?')
                        yes_or_no = input('(Y/n): ')
                        if yes_or_no != 'Y':
                            print('File not saved')
                            continue
                    data[1] = f'file2:{player_ship_coords};{player_coordinates};{cpu_ship_coords};{cpu_coordinates}'
                    break
                elif file_choice == 'file3' or file_choice == '3':
                    if data[2] != 'file3:':
                        print('File3 already has game data saved on. Do you want to overwrite it?')
                        yes_or_no = input('(Y/n): ')
                        if yes_or_no != 'Y':
                            print('File not saved')
                            continue
                    data[2] = f'file3:{player_ship_coords};{player_coordinates};{cpu_ship_coords};{cpu_coordinates}'
                    break
                elif file_choice == '/back':
                    break
                elif file_choice == '/quit':
                    print('Are you sure you want to quit? Any unsaved changes will be lost.')
                    yes_or_no = input('(Y/n): ')
                    if yes_or_no == 'Y': exit() # else continue file-choice loop
                else:
                    print('\nInvalid file choice')
            if file_choice == '/back':
                continue
            with open('battleships_files.txt', 'w') as file:
                for element in data:
                    file.write(f'{element}\n')
            print('File successfully overwritten')

        elif launch_co_ord == '/status':
            print('REMAINING FRIENDLY SHIPS CO-ORDINATES:', *player_ship_coords)
        elif launch_co_ord == '/gridscan':
            print('REMAINING UNUSED LAUNCH CO-ORDINATES:', *player_coordinates)
        elif launch_co_ord == '/check':
            print('PLAYER REMAINING SHIPS', len(player_ship_coords))
            print('CPU REMAINING SHIPS:', len(cpu_ship_coords))
        elif launch_co_ord == '/enemyinteldecrypt':  # Secret command
            print('ENEMY SHIPS CO-ORDINATES:', *cpu_ship_coords)
        elif launch_co_ord == '/quit':
            print('Are you sure you want to quit? Any unsaved changes will be lost.')
            yes_or_no = input('(Y/n): ')
            if yes_or_no == 'Y': exit() # else continue in_game loop
        else:
            print('\nInvalid co-ordinate.\nPlease select a valid co-ordinate or command')
        
    end_game_choice = input('Press ENTER to restart or type /quit to exit.\n')
    if end_game_choice == '/quit':
        break
    player_coordinates = co_ords.copy()
    cpu_coordinates = co_ords.copy()
    player_ship_coords.clear()
    cpu_ship_coords.clear()
