

from helpers import alphabet_position, rotate_character                         

def encrypt(text, rot):

    encrypt_text = ""
    for char in text:
        letter = rotate_character(char, rot)                                    
        encrypt_text = encrypt_text + letter                                    
    return encrypt_text


def main():
    text = input("What message would you like to encrypt?  ")                   
    rot = int(input("Rotate by: "))                                                         

    print(encrypt(text, rot))                                                  

if __name__ == '__main__':
    main()