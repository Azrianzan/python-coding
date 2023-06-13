# Create a password encryption & decryption program with base64
import base64

print("______                            _   ")
print("|___  /                          | |  ")
print("   / /  ___  ___ _ __ _   _ _ __ | |_ ")
print("  / /  / _ \/ __| '__| | | | '_ \| __|")
print("./ /__|  __/ (__| |  | |_| | |_) | |_ ")
print("\_____/\___|\___|_|   \__, | .__/ \__|")
print("                       __/ | |        ")
print("                      |___/|_|        ")

print("Welcome to Zecrypt")
print("You can encrypt and decrypt your password using base64 with this program")

chooseMethod = True

while chooseMethod == True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    selectedMethod = int(input("Enter the NUMBER of the feature you want to use (example: 1): "))

    if selectedMethod == 1:
        chooseMethod = False
        def encryption(pwEncrypt):
            encrypted = base64.b64encode(pwEncrypt)
            print(f"Your encrypted password is {encrypted}")
            print("You can copy the encypted password inside of ''")
            print("You can save the encrypted password anywhere on your computer")
            print("And a layman who doesn't know much about cybersecurity won't know your password")
            print("Even though they open your file that contains your password (encrypted).")
            print("When you need to see your password again just use the decryption feature")
            print("")
        password = input("Enter the password you want to encrypt: ")
        passwordBytes = password.encode()
        encryption(passwordBytes)
        chooseMethod = True

    elif selectedMethod == 2:
        chooseMethod = False
        def decryption(pwDecrypt):
            decrypted = base64.b64decode(pwDecrypt)
            decrypted_decode = decrypted.decode()
            print(f"Your decrypted password is {decrypted_decode}")
            print("You can now use the decrypted password to log into your account.")
            print("Keep your decrypted password safe.")
            print("If you need to encrypt your password just use the encryption method")
            print("")
        wantDecrypt = input("Enter your encrypted password: ")
        decryption(wantDecrypt)
        chooseMethod = True
    
    elif selectedMethod == 3:
        print("Thank you for using this program")
        chooseMethod = False

    else:
        print("")
        print("Please choose the number correctly")

# convert the input to the bytes format which is b'input'
# print(passwordBytes)
# you can put encode() function from base64 at the end so
# you don't need to think about the input & output parameters
# like when you put it on the front base.64.encode(input, output)

# you can also convert str from the input to bytes with utf-8
# passwordBytes = bytes(password, 'utf-8')
# the basic method to convert it to bytes is b'the_data'

# now you can type your password for your accont and it will
# be encrypted to base64
# next task : make a decryptor program with base 64