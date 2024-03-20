font_off = '\033[0m'

print("\nWelcome to Simple Scribe. Enter text, manipulating it in different styles and saving it in document.")
print("Type /quit to quit.")

document = []

while True:

    text = input(f"{font_off}\nEnter your text (Type /document to print current document, /clear to empty document, /undo to delete last text)\n")
    
    if text == "/quit":
        break

    if text == "/document":
        if len(document) > 0:  # If document is not empty
            current_document = "\n".join(document)
            print()  # Newline
            print(current_document)
        continue

    if text == "/clear":
        document.clear()
        continue

    if text == "/undo":
        if len(document) > 0:
            del document[-1]
        continue

    action = input("Enter your action for the text (upper, bold, underline, italics, replace, colour): ")
    
    if action == "/quit":
        break

    elif action.lower().strip() == "upper":
        upper_text = f"{font_off}{text.upper()}"  # Text not affected by other fonts
        document.append(upper_text)
        print(upper_text)
    
    elif action.lower().strip() == "bold":
        bold_text = f"{font_off}\033[1m{text}"
        document.append(bold_text)
        print(bold_text)
    
    elif action.lower().strip() == "underline":
        underline_text = f"{font_off}\033[4m{text}"
        document.append(underline_text)
        print(underline_text)
    
    elif action.lower().strip() == "italics":
        italics_text = f"{font_off}\033[3m{text}"
        document.append(italics_text)
        print(italics_text)

    elif action.lower().strip() == "replace":
        old_bit = input("Enter bit of your text that you want to replace (replaces every occurrence): ")
        if old_bit == "/quit":
            break
        new_bit = input("Enter text that you want it replaced by: ")
        if new_bit == "/quit":
            break
        replacement_text = f"{font_off}{text.replace(old_bit, new_bit)}"
        document.append(replacement_text)
        print(replacement_text)
    
    elif action.lower().strip() == "colour":
        colour = input("Select your colour (black, red, green, yellow, blue, magenta, cyan): ")
        if colour == "/quit":
            break
        colours = ["black", "red", "green", "yellow", "blue", "magenta", "cyan"]
        colour_edit = colour.lower().strip()
        if colour_edit in colours:
            colour_text = f"{font_off}\033[3{colours.index(colour_edit)}m{text}"
            document.append(colour_text)
            print(colour_text)
        else:
            print("Invalid colour")
    
    elif action == '':  # No action
        nothing_text = f"{font_off}{text}"
        document.append(nothing_text)
        print(nothing_text)
    
    else:
        print("Invalid option")