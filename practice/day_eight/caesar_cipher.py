from art import logo


def caesar(text, shift, direction):
    message = ""
    if shift > 26:
        shift = shift % 26 
    for char in text:
        if char not in alphabet:
            message += char
        else: 
            position = alphabet.index(char)
            if direction == 'encode':
                new_pos = position + shift
                if new_pos > 25:
                    new_pos -= 26
            elif direction == 'decode':
                new_pos = position - shift
                if new_pos < 0:
                    new_pos += 26
            message += alphabet[new_pos]
    return message


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

restart = "yes"

while restart != "no":
    print(logo)
    start = input("Type \'encode\' in ecrypt, type \'decode\' to decrypt: ")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: "))

    result = caesar(text=text, shift=shift, direction=start)
    print(f"Message is: {result}")

    restart = input("Type \'yes\' if you want to go again. Otherwise type \'no\': ").lower()