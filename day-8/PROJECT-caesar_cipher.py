from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']*2

def caesar(direction, text, shift):
    if direction == 'decode':
        shift *= -1
    new_data = ""
    for character in text:
        new_char = character
        if character.lower() in alphabet:
            is_uppercase = True if 65 <= ord(character) <= 90 else False
            
            position = alphabet.index(character.lower())
            new_position = position + shift
            new_char = alphabet[new_position]
            new_char = new_char.upper() if is_uppercase else new_char

        new_data += new_char
    print("The result is: %s" % new_data)

print(logo)

run_program = True
while run_program:
    direction = input("Type 'encode' to encode, type 'decode' to decode: ")
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    shift = shift % len(alphabet)
    print(shift)
    caesar(direction=direction, text=text,shift=shift)
    run_program = True if (input("Do you want to run the program again? Type 'Yes' or 'No': ").lower() == "yes") else False 