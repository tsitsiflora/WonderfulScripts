# Decrypting messages encrypted using the ceaser algorithm

cipher = str(input("Enter message to decrypt: "))
key_present = str(input("Do you have the key to decrypt: "))
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#use this if key is known
def ceaser_decryptor(cipher, n):
    
    message = ""
    for i in range(len(cipher)):
        char = cipher[i]
        
        # for spaces
        if char == " ":
            message += char
            
        # for upper case letters
        
        elif char.isupper():
            message += chr((ord(char) - n-65) % 26 + 65)
        
        # for lower case letters
        
        else:
            message += chr((ord(char) - n-97) % 26 + 97)
    return message


#when key is unknown
def ceaser_hacker(cipher): 
    cipher = cipher.upper() 
    # iterating the keys from 0 to 25
    
    for key in range(len(LETTERS)): #0
        message = ""
        
        for letter in cipher:       #x
            if letter in LETTERS:   #yes
                num = LETTERS.find(letter)  #1
                num = num - key # 1-0 = 1
                if num < 0: #no
                    num += len(LETTERS) #
                message += LETTERS[num] 
            else:
                message += letter #x
                
        print("Decrypting key #{0}: plain text: {1}".format(key, message))
    

def main():
    if key_present == "yes":
        n = int(input("Enter shift key: "))
        plain_text = ceaser_decryptor(cipher, n)
        print("The decrypted message is: {0}".format(plain_text))
    elif key_present == "no":
        plain_text = ceaser_hacker(cipher)
    else:
        print("Invalid input!")


if __name__ == "__main__":
    main() 
    
