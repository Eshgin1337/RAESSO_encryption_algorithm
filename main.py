from encrypt import encrypt_with_ascii_shuffling
from decrypt import decrypt_with_ascii_shuffling
import sys # Import sys to handle potential Base64 errors gracefully

def main():
    # Get dynamic input 
    try:
        plaintext = input("Enter the plaintext message to encrypt: ")
        key = input("Enter the secret key for encryption: ")

        if not key:
            print("Error: Encryption key cannot be empty.")
            return
        if not plaintext:
            print("Error: Plaintext cannot be empty.")
            return

    except EOFError:
        print("\nInput cancelled.")
        return
    # --------------------------

    print("\nEncrypting...")
    # Encrypt plaintext with ASCII shuffling
    # The encryption function prints the result internally in the provided code
    ciphertext = encrypt_with_ascii_shuffling(plaintext, key)

    print("\nAttempting Decryption...")
    try:
        decryption_key = input("Enter the secret key for decryption: ")
        if not decryption_key:
            print("Error: Decryption key cannot be empty.")
            return

    except EOFError:
        print("\nInput cancelled.")
        return

    # Decrypt the ciphertext
    try:
        # The decryption function should ideally return the result, not print it
        decrypted_plaintext = decrypt_with_ascii_shuffling(ciphertext, decryption_key)
        print("Decrypted plaintext result:", decrypted_plaintext)
    except Exception as e:
        # Catch potential errors during decryption (e.g., incorrect padding/Base64, logic errors)
        print(f"\nAn error occurred during decryption: {e}")
        print("This might be due to an incorrect key, corrupted ciphertext,")
        print("or issues in the decryption logic within 'decrypt.py'.")
        print("Please ensure 'decrypt.py' contains the correct decryption steps.")


if __name__ == "__main__":
    main()