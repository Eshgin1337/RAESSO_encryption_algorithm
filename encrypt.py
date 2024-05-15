from utils import *

def encrypt_with_ascii_shuffling(plaintext, key):
    # Generate a random string with the length of the key
    random_string = generate_random_string(len(key))

    plaintext_with_random = random_string + plaintext


    # Convert plaintext with random characters to binary
    plaintext_binary = text_to_binary(plaintext_with_random)
 
    key_binary = text_to_binary(key)

    # Expand the key to match the length of the plaintext
    expanded_key = expand_key(key_binary, len(plaintext_binary))


    # Convert plaintext and key to arrays of bits
    plaintext_array = [int(bit) for bit in plaintext_binary]
    key_array = [int(bit) for bit in expanded_key]
    
    # print(f"plaintext_before_shuffle : {plaintext_array}")
    
    # ALGO
    plaintext_modified = plaintext_array.copy()
    for i in range(0, len(plaintext_modified), 8):
        plaintext_chunk = plaintext_modified[i:i+8]
        key_chunk = key_array[i:i+8]

        zeros_count = key_chunk[:7].count(0)
        ones_count = key_chunk[:7].count(1)

        swap_indices_tuple = (ones_count, zeros_count)

        plaintext_chunk_copy = plaintext_chunk.copy()

        # Reverse the swapping of indices in the plaintext chunk based on the counts
        plaintext_chunk_copy[swap_indices_tuple[0]], plaintext_chunk_copy[swap_indices_tuple[1]] = plaintext_chunk_copy[swap_indices_tuple[1]], plaintext_chunk_copy[swap_indices_tuple[0]]
        plaintext_modified[i:i+8] = plaintext_chunk_copy


    plaintext_modified_after_add = binary_addition(plaintext_modified, key_array)

    if(len(plaintext_modified_after_add) % 8 == 1):
        key_array.append(key_array[0])

    encrypted_plaintext_array_after_XOR = [x ^ y for x, y in zip(plaintext_modified_after_add, key_array)]

    # Convert ciphertext array to bytes
    ciphertext_bytes = bytes(int(''.join(map(str, encrypted_plaintext_array_after_XOR[i:i+8])), 2) for i in range(0, len(encrypted_plaintext_array_after_XOR), 8))
    
    # Encode ciphertext bytes in Base64
    ciphertext_base64 = encode_base64(ciphertext_bytes)
    print("The encrypted text is: ", ciphertext_base64)
    return ciphertext_base64