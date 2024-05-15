from encrypt import encrypt_with_ascii_shuffling
from decrypt import decrypt_with_ascii_shuffling

def main():
    plaintext = "Hello, world!"
    key = "SecretKey"  # Encryption key
    
    # Encrypt plaintext with ASCII shuffling
    ciphertext = encrypt_with_ascii_shuffling(plaintext, key)
    print("Ciphertext:", ciphertext)
    
    # Prompt user to enter the decryption key
    decryption_key = input("Enter the decryption key: ")
    
    # Decrypt the ciphertext
    decrypted_plaintext = decrypt_with_ascii_shuffling(ciphertext, decryption_key)
    
    print("Decrypted plaintext:", decrypted_plaintext)

if __name__ == "__main__":
    main()
