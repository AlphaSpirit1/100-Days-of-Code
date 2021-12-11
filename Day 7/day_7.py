alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    encoded = ''
    for letters in text:
        current = alphabet.index(letters)
        if shift + current <= 25:
            letter_position = shift + current
            letter = alphabet[letter_position]
            encoded += letter
        else:
            letter_position = shift + current - 26
            letter = alphabet[letter_position]
            encoded += letter
    print(encoded)


def decrypt(text, shift):
    decoded = ''
    for letters in text:
        current = alphabet.index(letters)
        letter_position = current - shift
        letter = alphabet[letter_position]
        decoded += letter

    print(decoded)


if direction == 'encode':
    encrypt(text=text, shift=shift)
else:
    decrypt(text=text, shift=shift)

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
