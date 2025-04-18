# RAESSO Encryption Algorithm

This repository contains the Python implementation of the RAESSO encryption algorithm, developed as undergraduate diploma work by Eshgin Hasanov ([Graduation Work](https://drive.google.com/file/d/1ynqu6OVNvrJ2hYxCULgArDHtzX_FC3QB/view)).

## Description

RAESSO is an experimental symmetric encryption algorithm designed as an academic exercise. It incorporates randomization by adding a random prefix to the plaintext and uses key-dependent shuffling of bits within 8-bit blocks during the encryption process. The algorithm involves binary conversions, custom binary addition, XOR operations, and outputs Base64 encoded ciphertext.

## Features

* Symmetric key encryption.
* Random prefix "salting" based on key length.
* Key-dependent bit shuffling within 8-bit chunks.
* Uses custom binary arithmetic functions (`utils.py`).
* Outputs Base64 encoded text.

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Eshgin1337/RAESSO_encryption_algorithm.git
    cd RAESSO_encryption_algorithm
    ```
2.  **Requirements:**
    * Python 3.x is required.
    * No external libraries are needed (uses only Python's standard libraries: `random`, `string`, `base64`).

## Usage

The `main.py` script provides an interactive command-line interface for demonstration:

1.  **Run the script:**
    Open your terminal, navigate to the project directory, and run:
    ```bash
    python main.py
    ```
2.  **Enter Input:**
    The script will interactively prompt you to enter the following:
    * The plaintext message you want to encrypt.
    * The secret key to use for encryption.
3.  **Encryption Output:**
    The script will then perform the encryption and print the resulting Base64 encoded ciphertext.
4.  **Decryption Attempt:**
    Finally, it will prompt you to enter the secret key again for decryption and attempt to decrypt the ciphertext.

