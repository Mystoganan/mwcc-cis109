import argparse
from cryptlib import encrypt, decrypt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encrypt", action='store_true', required=False, help="Encrypt the message")
    parser.add_argument("-d", "--decrypt", action='store_true', required=False, help="Decrypt the message")
    parser.add_argument("-m", "--message", required=True, help="Message Being Encrypted/Decrypted")
    parser.add_argument("-s", "--shift", required=True, help="How much the message is being shifted")
    args = parser.parse_args()

    if args.encrypt and args.decrypt:
        print("You can't do both at the same time. Thats just typing. Try again")
        input("Press [Enter] to continue")
        return

    elif args.encrypt:
        encrypted_message = encrypt(args.message, int(args.shift))
        print(encrypted_message)
    elif args.decrypt():
        decrypted_message = decrypt(args.message, int(args.shift))
        print(decrypted_message)        

main()