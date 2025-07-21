from PIL import Image
from random import randint

def encrypt(input_path,output_path,key):
    image=Image.open(input_path)
    pixels=image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r,g,b=pixels[i,j]
            r=(r+key)%256 #mathematical operation
            g=(g+key)%256
            b=(b+key)%256
            pixels[i,j]=(r,b,g) #swapping
    image.save(output_path)

def decrypt(input_path,output_path,key):
    image=Image.open(input_path)
    pixels=image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r,g,b=pixels[i,j]
            pixels[i,j]=((r-key)%256,(g-key)%256,(b-key)%256) #swapping back
    image.save(output_path)

def main():
    input_path = input("Enter the path of the image to encrypt: ")
    output_path = input("Enter the path to save the encrypted image: ")
    key = randint(0, 255)  # Random key for encryption
    print(f"Using key: {key}")
    
    encrypt(input_path, output_path, key)
    print("Image encrypted successfully.")
    
    decrypted_output_path = input("Enter the path to save the decrypted image: ")
    decrypt(output_path, decrypted_output_path, key)
    print("Image decrypted successfully.")
main()