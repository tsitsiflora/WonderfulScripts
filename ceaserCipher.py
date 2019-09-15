#this is a weak method of encryption as well. Not recommended as hackers can easily,
#  without putting much effort, crack the cipher
# formular used: c = (x + n) mod 26

message = str(input("Enter message to encrypt: "))
n = int(input("Enter shift key: "))

def ceaser_cipher(message, n):
    cipher = ""
    for i in range(len(message)):
        char = message[i]
        
        # for spaces
        if char == " ":
            cipher += char
            
        # for upper case letters
        
        elif char.isupper():
            cipher += chr((ord(char) + n-65) % 26 + 65)
        
        # for lower case letters
        
        else:
            cipher += chr((ord(char) + n-97) % 26 + 97)
    return cipher

cipher_message = ceaser_cipher(message, n)
print("The encrypted message is: {0}".format(cipher_message))
        
