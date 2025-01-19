
# ENCRYPTION AND DECRYPTION

#Encryption
inputstr = input("Enter the input string:")
key = int(input("Enter the key value:"))
encrypt_text = ""

for val in inputstr:
    ordinalval = ord(val)
    ordinalval += key
    if ordinalval > ord('z'):
        ordinalval = ord('a') + ordinalval - ord('z') -1
    codevalue = chr(ordinalval)
    encrypt_text += codevalue
print("Encrypted text:",encrypt_text)

#Decryption
outputstr = input("Eter the output string:")
key = int(input("Enter the key value:"))
decrypt_text = ""

for val in outputstr:
    ordinalval = ord(val)
    ordinalval -= key
    if ordinalval < ord('a'):
        ordinalval = ord('z') - ordinalval - ord('a') -1
    codevalue = chr(ordinalval)
    decrypt_text += codevalue
print("Decrypted text:",decrypt_text)
