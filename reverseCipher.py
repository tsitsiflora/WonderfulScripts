#this is a very weak method of encrypting messages and is not recommende to use in any case
message = str(input("Enter the message to encrypt: "))

def reverse_cipher(message):
    #lets try to strip off all spaces to make it a little more interesting, and lower case every letter
    message = message.replace(" ", "").lower()
    cipher = ""
    i = len(message) - 1
    while i >= 0:
        cipher += message[i]
        i = i - 1
    return cipher

cipher_message = reverse_cipher(message)
print("The cipher text is {0}".format(cipher_message))
