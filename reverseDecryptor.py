# decrypting text encoded using the reverse algorithm

cipher = str(input("Enter the cipher text to decrypt: "))

def reverse_decryptor(cipher):
    
    message = ""
    i = len(cipher) - 1
    while i >= 0:
        message += cipher[i]
        i = i - 1
    return message


plain_text = reverse_decryptor(cipher)
print("The plain text is {0}".format(plain_text))
