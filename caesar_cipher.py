#Python script to encrypt and decrypt plain text using Caesar Cipher


print("****** CAESAR CIPHER ENCRYPTION AND DECRYPTION ******\n\n")

#Method to encrypt text
def encrypt_text(txt, key):
    cipher = " "
    for letter in txt:
        if letter.isupper():
            index = (ord(letter) + key - ord('A'))%26+ord('A')
            cipher+= chr(index)

        elif letter.islower():
            index = (ord(letter) + key - ord('a'))%26+ord('a')
            cipher+= chr(index)

    print("Encrypted Text:"+cipher)


#Method to decrypt text
def decrypt_text(txt, key):
    plain = " "
    for letter in txt:
        if letter.isupper():
            index = (ord(letter) - key - ord('A'))%26+ord('A')
            plain+= chr(index)
        
        elif letter.islower():
            index = (ord(letter) - key - ord('a'))%26+ord('a')
            plain+= chr(index)
    print("Decrypted Text:"+plain)


option = input("What do you want to do(Encrypt/Decrypt): ")
if(option.lower() == "encrypt"):
    str = input("Enter your txt:")
    k = int(input("Enter key: "))
    encrypt_text(str, k)

elif(option.lower() == "decrypt"):
    str = input("Enter your txt:")
    k = int(input("Enter key: "))
    decrypt_text(str, k)

else:
    print('Wrong input \nAborting..........')


