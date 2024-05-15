import random
import string
import base64

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def text_to_binary(text):
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    return binary_text

def binary_to_text(binary_text):
    text = ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))
    return text

def pad_array(array, length):
    padding_length = length - len(array)
    return [0] * padding_length + array

def expand_key(key, length):
    repeated_key = (key * (length // len(key) + 1))[:length]
    return repeated_key


def swap_indices(array, indices):
    array[indices[0]], array[indices[1]] = array[indices[1]], array[indices[0]]

def encode_base64(data):
    encoded_data = base64.b64encode(data).decode('utf-8')
    return encoded_data

def decode_base64(encoded_data):
    decoded_data = base64.b64decode(encoded_data)
    return decoded_data

def binary_addition(array1, array2):
    result = []
    length = max(len(array1), len(array2))
    carry = 0

    # Pad the arrays with leading zeros to ensure they have the same length
    while len(array1) < length:
        array1.insert(0, 0)
    while len(array2) < length:
        array2.insert(0, 0)

    # Perform binary addition
    for i in range(length - 1, -1, -1):
        bit_sum = array1[i] + array2[i] + carry
        bit = bit_sum % 2
        carry = bit_sum // 2
        result.insert(0, bit)

    # Add the remaining carry, if any
    if carry > 0:
        result.insert(0, carry)

    return result

def binary_subtraction(a, b):
    result = []
    borrow = 0
    
    # Ensure both binary arrays have the same length by padding the shorter one with leading zeros
    max_length = max(len(a), len(b))
    a = [0] * (max_length - len(a)) + a
    b = [0] * (max_length - len(b)) + b
    
    for bit_a, bit_b in zip(reversed(a), reversed(b)):
        difference = bit_a - bit_b - borrow
        if difference < 0:
            difference += 2
            borrow = 1
        else:
            borrow = 0
        result.insert(0, difference)
    
    # Trim leading zeros from the result if any
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    
    return result