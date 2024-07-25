def generate_subkeys(main_key, num_subkeys):
    """Generate subkeys by dividing the main key into parts."""
    subkeys = []
    key_length = len(main_key)
    segment_length = key_length // num_subkeys

    for i in range(num_subkeys):
        start = i * segment_length
        end = (i + 1) * segment_length if i < num_subkeys - 1 else key_length
        subkey = main_key[start:end]
        subkeys.append(subkey)
    return subkeys

def xor_encrypt_decrypt(data, key):
    """XOR encryption/decryption of data with the given key."""
    return bytearray(b ^ key[i % len(key)] for i, b in enumerate(data))

def process_file(input_file, output_file, key):
    """Encrypt the PNG file and embed the encrypted data into the same PNG file."""
    with open(input_file, 'rb') as file:
        data = bytearray(file.read())

    # Generate 17 subkeys from the main key
    subkeys = generate_subkeys(key, 17)

    # Encrypt the PNG data
    encrypted_data = data
    for subkey in subkeys:
        encrypted_data = xor_encrypt_decrypt(encrypted_data, subkey.encode())

    # Write the encrypted data to the output file
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

    print("File encrypted and embedded successfully.")

if __name__ == "__main__":
    # Define input and output file names
    input_file = 'FOTO.png'
    output_file = 'WKWK.png'
    key = "YangLainLombaMakanKerupuk,GWMalahMAENLAPTOP"

    process_file(input_file, output_file, key)
