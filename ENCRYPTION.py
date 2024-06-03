# Enter your code here
import string

def main():
    print("Enter the message:")
    msg = input()
    key = int(input("Enter key: "))
    
    encrypted_msg = ""
    for char in msg:
        if char.islower():
            encrypted_msg += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isupper():
            encrypted_msg += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            encrypted_msg += char
    
    print("Encrypted message:", encrypted_msg)

if __name__ == "__main__":
    main()

