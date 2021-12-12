MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ': '/'}

# list out keys and values separately
key_list = list(MORSE_CODE_DICT.keys())
val_list = list(MORSE_CODE_DICT.values())

# print key with val 100


def encrypt(message):
    encrypted = ''
    for letter in message:
        encrypted += MORSE_CODE_DICT[letter]+' '

    return encrypted
def decrypt(message):
    decrypted = ''
    removed_space = message.split()
    for letter in removed_space:
        position = val_list.index(letter)
        decrypted += (key_list[position])
    return decrypted

while True:
    encrypt_or_decrypt = input('What do you want to do?type "e" to encrypt and "d" for decrypt')
    message = input('What is the message you want to convert').upper()
    if encrypt_or_decrypt == 'e':
        print(encrypt(message))
    elif encrypt_or_decrypt == 'd':
        print(decrypt(message))