import os

class Instrument():

    sound = 'Instrument sound'

    def __init__(self, dynamic) -> None:
        self.dynamic = dynamic

    def produce_sound(self):
        if self.dynamic == 'f':
            return self.sound.upper()
        else:
            return self.sound
    
    def change_dynamic(self, dynamic):
        self.dynamic = dynamic
    
    def __repr__(self) -> str:
        return 'Instrument'

class Guitar(Instrument):

    sound = 'dunklunklunk'
    heavy_sound = 'TWANG!'
    harmonics_sound = 'duuuuungh'

    def __init__(self, dynamic, style) -> None:
        super().__init__(dynamic)
        self.style = style

    def produce_sound(self):
        if self.style == 'harmonics':
            if self.dynamic == 'f':
                return self.harmonics_sound.upper()
            else:
                return self.harmonics_sound
        else:
            if self.dynamic == 'f':
                return self.heavy_sound
            else:
                return self.sound
            
    def change_style(self, style):
        self.style = style
    
    def __repr__(self) -> str:
        return 'Guitar'

class AcousticGuitar(Guitar):

    def __init__(self, dynamic, style) -> None:
        super().__init__(dynamic, style)

    def __repr__(self) -> str:
        return 'Acoustic Guitar'

class ElectricGuitar(Guitar):

    sound = 'wahwahwahwahwah!'

    def __init__(self, dynamic, style) -> None:
        super().__init__(dynamic, style)
    
    def produce_sound(self):
        if self.style == 'harmonics':
            if self.dynamic == 'f':
                return self.harmonics_sound.upper()
            else:
                return self.harmonics_sound
        else:
            if self.dynamic == 'f':
                return self.sound.upper()
            else:
                return self.sound
    
    def __repr__(self) -> str:
        return 'Electric Guitar'

class Piano(Instrument):

    sound = 'tinklinklinklink!'
    heavy_sound = 'BANGBANGBANGBANG!'

    def __init__(self, dynamic) -> None:
        super().__init__(dynamic)

    def produce_sound(self):
        if self.dynamic == 'f':
            return self.heavy_sound
        else:
            return self.sound

    def __repr__(self) -> str:
        return 'Piano'

class StringInstrument(Instrument):

    sound = 'screeeeeeeeech!'
    plucked_sound = 'pluckpluckpluck'
    
    def __init__(self, dynamic, style) -> None:
        super().__init__(dynamic)
        self.style = style

    def produce_sound(self):
        if self.style == 'pizzicato':
            if self.dynamic ==  'f':
                return self.plucked_sound.upper()
            else:
                return self.plucked_sound
        else:
            if self.dynamic == 'f':
                return self.sound.upper()
            else:
                return self.sound
            
    def change_style(self, style):
        self.style = style
    
    def __repr__(self) -> str:
        return 'Strings'

class Violin(StringInstrument):

    def __init__(self, dynamic, style) -> None:
        super().__init__(dynamic, style)

    def __repr__(self) -> str:
        return 'Violin'

class Cello(StringInstrument):

    def __init__(self, dynamic, style) -> None:
        super().__init__(dynamic, style)

    def __repr__(self) -> str:
        return 'Cello' 

class BrassInstrument(Instrument):

    sound = 'toot!'
    muted_sound = 'fffffffft!'

    def __init__(self, dynamic, style) -> None:
        super().__init__(dynamic)
        self.style = style

    def produce_sound(self):
        if self.style == 'mute':
            if self.dynamic == 'f':
                return self.muted_sound.upper()
            else:
                return self.muted_sound
        else:
            if self.dynamic == 'f':
                return self.sound.upper()
            else:
                return self.sound
            
    def change_style(self, style):
        self.style = style
    
    def __repr__(self) -> str:
        return 'Brass'
    
class Trumpet(BrassInstrument):

    def __init__(self, dynamic, style) -> None:
        super().__init__(dynamic, style)

    def __repr__(self) -> str:
        return 'Trumpet'

class Trombone(BrassInstrument):

    def __init__(self, dynamic, style) -> None:
        super().__init__(dynamic, style)

    def __repr__(self) -> str:
        return 'Trombone'

class DrumKit(Instrument):

    sound = 'baDumCrash!'
    heavy_sound = 'BASHCRASHBASHCRASH!'

    def __init__(self, dynamic) -> None:
        super().__init__(dynamic)
    
    def produce_sound(self):
        if self.dynamic == 'f':
            return self.heavy_sound
        else:
            return self.sound
        
    def __repr__(self) -> str:
        return 'DrumKit'    

class Saxophone(Instrument):

    sound = 'toodloodloot'

    def __init__(self, dynamic) -> None:
        super().__init__(dynamic)

    def __repr__(self) -> str:
        return 'Saxophone'

tag = '- Musical Instruments\n'

instruments = []

sections = []

# Function definitions

def play_sounds():
    print()
    output_sounds = [obj.produce_sound() for obj in instruments]
    print(*output_sounds)
    print()

def initialise_instrument(instrument):
    while True:
        if issubclass(instrument, Piano):
            break
        if issubclass(instrument, DrumKit):
            break
        if issubclass(instrument, Saxophone):
            break
        print('Select style:')
        print('1. Normal')
        if issubclass(instrument, StringInstrument):
            print('2. Pizzicato')
        elif issubclass(instrument, BrassInstrument):
            print('2. Mute')
        else: # Is subclass Guitar
            print('2. Harmonics')
        selection = input()
        if selection == '1':
            style = 'normal'
            break
        elif selection == '2':
            if issubclass(instrument, StringInstrument):
                style = 'pizzicato'
                break
            elif issubclass(instrument, BrassInstrument):
                style = 'mute'
                break
            else: # Is subclass Guitar
                style = 'harmonics'
                break
        elif selection == 'quit':
            exit()
        else:
            print('\nInvalid input.')
    while True:
        print('Select dynamic:')
        print('1. mf (medium-loud)\n2. f (loud)')
        selection = input()
        if selection == '1':
            dynamic = 'mf'
            break
        elif selection == '2':
            dynamic = 'f'
            break
        elif selection == 'quit':
            exit()
        else:
            print('\nInvalid input.')
    single_instrument = [obj for obj in instruments if isinstance(obj, instrument)] # Will contain 1 or 0 instruments
    if single_instrument:
        if issubclass(instrument, Piano) or issubclass(instrument, DrumKit) or issubclass(instrument, Saxophone):
            if single_instrument[0].dynamic == dynamic:
                print('Instrument already has selected settings.\n')
            else:
                single_instrument[0].change_dynamic(dynamic)
                play_sounds()
        else:
            if single_instrument[0].dynamic == dynamic and single_instrument[0].style == style:
                print('Instrument already has selected settings.\n')
            else:
                single_instrument[0].change_dynamic(dynamic)
                single_instrument[0].change_style(style)
                play_sounds()
    else: # If list does not contain instrument
        if issubclass(instrument, Piano) or issubclass(instrument, DrumKit) or issubclass(instrument, Saxophone):
            instruments.append(instrument(dynamic))
            play_sounds()
        else:
            instruments.append(instrument(dynamic, style))
            play_sounds()



# MAIN

while True:
    print('Select from the following instrument groups to play/alter (type number):')
    print('1. Strings\n2. Brass\n3. Guitar\n4. Other')
    print('Type \'stop\' to stop an instrument playing. Type \'position\' to change an instrument\'s position.')
    print('Type \'view\' to view the sound sections of your draft. Type \'add\' to add sound section to your draft.')
    print('Type \'save\' to save your draft. Type \'open\' to load an existing draft.')
    print('Type \'quit\' to exit.')
    selection = input()
    if selection == '1':
        while True:
            print('Select string instrument:\t\t\t(P) = instrument currently playing')
            print(f'''1. Violin {'(P)' if 'Violin' in [str(obj) for obj in instruments] else ''}''')
            print(f'''2. Cello {'(P)' if 'Cello' in [str(obj) for obj in instruments] else ''}''')
            selection = input()
            if selection == '1':
                initialise_instrument(Violin)
                break
            elif selection == '2':
                initialise_instrument(Cello)
                break
            elif selection == 'quit' or selection == '\'quit\'':
                exit()
            else:
                print('\nInvalid input.')
    elif selection == '2':
        while True:
            print('Select brass instrument:\t\t\t(P) = instrument currently playing')
            print(f'''1. Trumpet {'(P)' if 'Trumpet' in [str(obj) for obj in instruments] else ''}''')
            print(f'''2. Trombone {'(P)' if 'Trombone' in [str(obj) for obj in instruments] else ''}''')
            selection = input()
            if selection == '1':
                initialise_instrument(Trumpet)
                break
            elif selection == '2':
                initialise_instrument(Trombone)
                break
            elif selection == 'quit' or selection == '\'quit\'':
                exit()
            else:
                print('\nInvalid input.')
    elif selection == '3':
        while True:
            print('Select guitar:\t\t\t\t\t(P) = instrument currently playing')
            print(f'''1. Acoustic Guitar {'(P)' if 'Acoustic Guitar' in [str(obj) for obj in instruments] else ''}''')
            print(f'''2. Electric Guitar {'(P)' if 'Electric Guitar' in [str(obj) for obj in instruments] else ''}''')
            selection = input()
            if selection == '1':
                initialise_instrument(AcousticGuitar)
                break
            elif selection == '2':
                initialise_instrument(ElectricGuitar)
                break
            elif selection == 'quit' or selection == '\'quit\'':
                exit()
            else:
                print('\nInvalid input.')
    elif selection == '4':
        while True:
            print('Select instrument:\t\t\t\t(P) = instrument currently playing')
            print(f'''1. Piano {'(P)' if 'Piano' in [str(obj) for obj in instruments] else ''}''')
            print(f'''2. Drum Kit {'(P)' if 'DrumKit' in [str(obj) for obj in instruments] else ''}''')
            print(f'''3. Saxophone {'(P)' if 'Saxophone' in [str(obj) for obj in instruments] else ''}''')
            selection = input()
            if selection == '1':
                initialise_instrument(Piano)
                break
            elif selection == '2':
                initialise_instrument(DrumKit)
                break
            elif selection == '3':
                initialise_instrument(Saxophone)
                break
            elif selection == 'quit' or selection == '\'quit\'':
                exit()
            else:
                print('\nInvalid input.')
    
    elif selection == 'view' or selection == '\'view\'':
        if not sections:  # If there are no sections saved
            print('You currently have no sections saved.\n')
        else:
            print()
            for section in sections: print(*section)
            print()
            while True:
                print('Type \'delete\' to remove section')
                print('Type \'back\' to go back')
                selection = input()
                if selection == 'quit' or selection == '\'quit\'':
                    exit()
                elif selection == 'back' or selection == '\'back\'':
                    play_sounds()
                    break
                elif selection == 'delete' or selection == '\'delete\'':
                    print()
                    for i, section in enumerate(sections, 1): print(f'{i}:', *section)
                    print()
                    while True:
                        try:
                            print('Select number corresponding to the section you want to be deleted.')
                            selection = input()
                            if selection == 'quit' or selection == '\'quit\'': exit()
                            if not selection.isdigit(): raise ValueError
                            if selection == '0' or int(selection) > len(sections): raise IndexError
                            index = int(selection) - 1
                            del sections[index]
                            print('Removed section')
                            if not sections:
                                print('\nNo remaining sections. Returning to main menu.')
                                input('Press ENTER to continue')
                                play_sounds()
                                break
                            else:
                                print()
                                for section in sections: print(*section)
                                print()
                                break
                        except IndexError: print('\nNumber out of range')
                        except ValueError: print('\nPlease type in a whole number')
                    if not sections: break
                else:
                    print('\nInvalid input.')

    elif selection == 'add' or selection == '\'add\'':
        if not instruments:
            print('You currently have no instruments playing.\n')
        else:
            output_sounds = [obj.produce_sound() for obj in instruments]
            sections.append(output_sounds)
            print('\nSound section added to draft.\n')

    elif selection == 'save' or selection == '\'save\'':
        if not sections:  # If there are no sections saved
            print('You currently have no sections saved.\n')
        else:
            print()
            for section in sections: print(*section)
            print()
            while True:
                file_name = input('Type name of your draft: ') + '.txt'
                if os.path.exists(file_name):
                    yes_or_no = input('Textfile already exists. Do you want to replace it? (Y/n): ')
                    if yes_or_no != 'Y':
                        print('File not saved.')
                        play_sounds()
                        break
                with open(file_name, 'w') as file:
                    file.write(f'{file_name[:-4]} {tag}')
                    for section in sections:
                        file.write(str(section))
                        file.write('\n')
                input('File saved in current directory. Press ENTER to continue.')
                play_sounds()
                break

    elif selection == 'open' or selection == '\'open\'':
        while True:
            file_name = input('Type file name of draft you want to load. Do NOT include .txt: ') + '.txt'
            if not os.path.exists(file_name):
                print('Textfile does not exist.\n')
                break
            else:
                with open(file_name, 'r') as file:
                    if not file.readlines()[0].endswith(tag):
                        print('Textfile in wrong format.\n')
                        break
                    else:
                        yes_or_no = input('Sound sections on current draft will be removed once opened draft is loaded. Do you wish to proceed? (Y/n): ')
                        if yes_or_no != 'Y':
                            print('File not opened.')
                            play_sounds()
                            break
                        sections.clear()
                        file.seek(0)
                        for line in file:
                            if line.endswith(tag):
                                pass
                            else:
                                section = line.strip('[]\n')
                                replace_marks = section.replace('\'', '')
                                replace_spaces = replace_marks.replace(' ', '')
                                split = replace_spaces.split(',')
                                sections.append(split)
                        print('Loaded draft. Type \'view\' to view it.\n')
                        break 
                
    elif selection == 'stop' or selection == '\'stop\'':
        if not instruments:  # If list does not contain instruments
            print('You currently have no instruments playing.\n')
        else:
            print()
            for i, obj in enumerate(instruments, 1):
                print(f'{i}:', obj, end='   ')
            print()
            print()
            while True:
                try:
                    print('Type number corresponding to instrument you want to stop.')
                    selection = input()
                    if selection == 'quit' or selection == '\'quit\'': exit()
                    if not selection.isdigit(): raise ValueError
                    if selection == '0' or int(selection) > len(instruments): raise IndexError
                    index = int(selection) - 1
                    del instruments[index]
                    print('Removed instrument')
                    play_sounds()
                    break
                except IndexError: print('\nNumber out of range')
                except ValueError: print('\nPlease type in a whole number')

    elif selection == 'position' or selection == '\'position\'':
        if not instruments:  # If list does not contain instruments
            print('You currently have no instruments playing.\n')
        else:
            print()
            for i, obj in enumerate(instruments, 1):
                print(f'{i}:', obj, end='   ')
            print()
            print()
            while True:
                try:
                    print('Type number corresponding to instrument you want to change position.')
                    selection = input()
                    if selection == 'quit' or selection == '\'quit\'': exit()
                    if not selection.isdigit(): raise ValueError
                    if selection == '0' or int(selection) > len(instruments): raise IndexError
                    index1 = int(selection) - 1
                    print('Type number of position you want instrument at.')
                    selection = input()
                    if selection == 'quit' or selection == '\'quit\'': exit()
                    if not selection.isdigit(): raise ValueError
                    if selection == '0' or int(selection) > len(instruments): raise IndexError
                    index2 = int(selection) - 1
                    instruments.insert(index2, instruments.pop(index1))
                    print('Position changed')
                    play_sounds()
                    break
                except IndexError: print('\nNumber out of range')
                except ValueError: print('\nPlease type in a whole number')

    elif selection == 'quit' or selection == '\'quit\'':
        break
    else:
        print('\nInvalid input. Please type in a number.')