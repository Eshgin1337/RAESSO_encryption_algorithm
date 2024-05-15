from utils import *

def decrypt_with_ascii_shuffling(ciphertext_base64, key):
    # Decode the ciphertext from Base64 to bytes
    key_needs_truncate = False

    ciphertext_bytes = decode_base64(ciphertext_base64)

    # Convert ciphertext bytes to an array of bits
    ciphertext_array = [int(bit) for byte in ciphertext_bytes for bit in f"{byte:08b}"]

    if len(ciphertext_array) % 8 == 1:
        key_needs_truncate = True
        
    # Convert key to binary
    key_binary = text_to_binary(key)

    # Expand the key to match the length of the ciphertext array
    expanded_key = expand_key(key_binary, len(ciphertext_array))

    # Convert key binary to an array of bits
    key_array = [int(bit) for bit in expanded_key]

    # Perform XOR operation between ciphertext array and key array to retrieve the shuffled plaintext array
    shuffled_plaintext_array = [ciphertext_bit ^ key_bit for ciphertext_bit, key_bit in zip(ciphertext_array, key_array)]

    # Pad the recovered modified plaintext array with zeros to match the length of the ciphertext array
    recovered_modified_plaintext_array = binary_subtraction(shuffled_plaintext_array, key_array)
    recovered_useful_plaintext_array = pad_array(recovered_modified_plaintext_array, len(ciphertext_array))

    if key_needs_truncate:
        key_array.pop()

    # Reverse the shuffling process by iterating over the arrays in chunks of 8
    for i in range(0, len(recovered_useful_plaintext_array), 8):
        plaintext_chunk = recovered_useful_plaintext_array[i:i+8]
        key_chunk = key_array[i:i+8]

        # Count the number of zeros and ones in the key chunk (excluding the last element)
        zeros_count = key_chunk[:7].count(0)
        ones_count = key_chunk[:7].count(1)

        # Create a tuple with counts of zeros and ones (swapped since we're reversing the process)
        swap_indices_tuple = (ones_count, zeros_count)

        # Create a copy of plaintext_chunk to avoid modifying the original
        plaintext_chunk_copy = plaintext_chunk.copy()

        # Reverse the swapping of indices in the plaintext chunk based on the counts
        plaintext_chunk_copy[swap_indices_tuple[0]], plaintext_chunk_copy[swap_indices_tuple[1]] = plaintext_chunk_copy[swap_indices_tuple[1]], plaintext_chunk_copy[swap_indices_tuple[0]]
        recovered_useful_plaintext_array[i:i+8] = plaintext_chunk_copy

    # Convert the reversed plaintext array to a string of binary digits
    reversed_plaintext_binary = ''.join(map(str, recovered_useful_plaintext_array))

    # Convert the binary string to text by grouping every 8 bits and converting them to characters
    reversed_plaintext = binary_to_text(reversed_plaintext_binary)
    
    # Remove the random characters added during encryption to obtain the original plaintext
    original_plaintext = reversed_plaintext[len(key):]
    
    return original_plaintext

