# Enter your code here
import string

def main():
    print("Enter the message:")
    msg = input()  # take the message as input
    key = int(input("Enter key: "))  # take the key as input
    
    decrypted_msg = ""
    for char in msg:
        if char.islower():
            decrypted_char = chr((ord(char) - key - ord('a')) % 26 + ord('a'))
            decrypted_msg += decrypted_char
        elif char.isupper():
            decrypted_char = chr((ord(char) - key - ord('A')) % 26 + ord('A'))
            decrypted_msg += decrypted_char
        else:
            decrypted_msg += char
    
    print("Decrypted message:", decrypted_msg)

if __name__ == "__main__":
    main()

