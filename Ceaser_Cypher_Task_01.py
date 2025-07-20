def encrypt(text, s):
    result=""
    for i in range(len(text)):
        if text[i].isupper():
            result+=chr((ord(text[i])+s-65)%26+65)
        else:
            result+=chr((ord(text[i])+s-97)%26+97)
    return result
def main():
    string=input("Enter the string to encrypt: ")
    shift=int(input("Enter the shift value: "))
    encrypted_string=encrypt(string, shift)
    print("Encrypted:", encrypted_string)
    print("Decrypted:", encrypt(encrypted_string, -shift))
main()