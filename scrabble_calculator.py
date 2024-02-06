MENU = '''Enter a word and the program will calculate its points in English Scrabble. (SPACE represents a blank.)
For bonuses enter /doubleletter, /tripleletter, /doubleword, /tripleword or /bonusword
Enter /quit to exit.
'''

letter_points_lookup = {
    'A' : 1,
    'B' : 3,
    'C' : 3,
    'D' : 2,
    'E' : 1,
    'F' : 4,
    'G' : 2,
    'H' : 4,
    'I' : 1,
    'J' : 8,
    'K' : 5,
    'L' : 1,
    'M' : 3,
    'N' : 1,
    'O' : 1,
    'P' : 3,
    'Q' : 10,
    'R' : 1,
    'S' : 1,
    'T' : 1,
    'U' : 1,
    'V' : 4,
    'W' : 4,
    'X' : 8,
    'Y' : 4,
    'Z' : 10,
    ' ' : 0   # Blank
}

bonuses = ['/doubleletter', '/tripleletter', '/doubleword', '/tripleword', '/bonusword']

word = input(MENU)

total = 0

while True:
    try:
        position = None
        word_bonuses = []
        dl_positions = []
        tl_positions = []

        while word in bonuses:  # Word can be /doubleletter, /tripleletter, etc.
            word_bonuses.append(word)
            word = input(f'{word_bonuses}: ')
            if not word:  # If empty string
                print('Please type in a word or bonus for your displayed bonus(es)')
                word = word_bonuses[-1]
                del word_bonuses[-1]  # Will be re-appended
        
        if word == '/quit':
            break

        for char in word.upper():  # Calculating points in letters
            if char not in letter_points_lookup:
                raise LookupError(f"Invalid character detected: {char}")
            total += letter_points_lookup[char]

        for bonus in word_bonuses:  # Check for /doubleletter or /tripleletter (extra inputs)
            if word == '/quit':
                break
            if bonus == '/doubleletter':
                position = input(f'Type in position number of {word.upper()} you want doubled: ')
                if position == '/quit':
                    break
                int_position = int(position) 
                dl_positions.append(int_position)
            if bonus == '/tripleletter':
                position = input(f'Type in position number of {word.upper()} you want tripled: ')
                if position == '/quit':
                    break
                int_position = int(position)                
                tl_positions.append(int_position)

        if word == '/quit' or position == '/quit':
            break

        if '/doubleletter' in word_bonuses:  # Checking for bonuses
            for pos in dl_positions:
                index_pos = pos - 1
                if index_pos < 0:
                    raise IndexError
                total += letter_points_lookup[word.upper()[index_pos]]  # IndexError also raised if index_pos > length
        if '/tripleletter' in word_bonuses:
            for pos in tl_positions:
                index_pos = pos - 1
                if index_pos < 0:
                    raise IndexError
                total += (letter_points_lookup[word.upper()[index_pos]] * 2)
        if '/doubleword' in word_bonuses:
            for i in range(word_bonuses.count('/doubleword')):
                total *= 2
        if '/tripleword' in word_bonuses:
            for i in range(word_bonuses.count('/tripleword')):
                total *= 3
        if '/bonusword' in word_bonuses:
            total += (50 * word_bonuses.count('/bonusword'))  # (+50 points for clearing seven letters off rack)
        
        print(total)

    except IndexError:
        print('Error: position out of range.')

    except ValueError:
        print('Error: you have typed something wrong.\nNext time type in a number.')

    except LookupError as err:
        print(err)

    finally:
        if word == '/quit' or position == '/quit':
            break
        print()
        total = 0
        word = input('')  # Type in next word