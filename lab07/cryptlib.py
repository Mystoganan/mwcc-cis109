def encrypt(message, shift):
    encrypted_message = ""

    for character in message:
        if character.isalpha():
            if character.isupper():
                base = ord("A")
            else:
                base = ord("a")

            position = ord(character) - base
            new_position = (position + shift) % 26
            new_character = chr(new_position + base)

            encrypted_message += new_character
        else:
            encrypted_message += character
    
    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""

    for character in message:
        if character.isalpha():
            if character.isupper():
                base = ord("A")
            else:
                base = ord("a")

            position = ord(character) - base
            new_position = (position - shift) % 26
            new_character = chr(new_position + base)

            decrypted_message += new_character
        else:
            decrypted_message += character

    return decrypted_message