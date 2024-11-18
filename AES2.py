def xor_bytes(data, key):
    return bytes(a ^ b for a, b in zip(data, key))

def pad(data):
    block_size = 16
    padding_length = block_size - (len(data) % block_size)
    return data + bytes([padding_length]) * padding_length

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def encrypt_block(plain_block, key):
    return xor_bytes(plain_block, key)

def decrypt_block(cipher_block, key):
    return xor_bytes(cipher_block, key)

def cbc_encrypt(plaintext, key, iv):
    plaintext = pad(plaintext)
    block_size = 16
    ciphertext = bytearray()
   
    previous_block = iv
    for i in range(0, len(plaintext), block_size):
        plain_block = plaintext[i:i+block_size]
        # If the last block is smaller than the block size, pad it with zeros
        if len(plain_block) < block_size:
            plain_block = plain_block.ljust(block_size, b'\x00')
       
        xor_block = xor_bytes(plain_block, previous_block)
        cipher_block = encrypt_block(xor_block, key)
        ciphertext.extend(cipher_block)
        previous_block = cipher_block
   
    return bytes(ciphertext)

def cbc_decrypt(ciphertext, key, iv):
    block_size = 16
    plaintext = bytearray()
   
    previous_block = iv
    for i in range(0, len(ciphertext), block_size):
        cipher_block = ciphertext[i:i+block_size]
        xor_block = decrypt_block(cipher_block, key)
        plain_block = xor_bytes(xor_block, previous_block)
        plaintext.extend(plain_block)
        previous_block = cipher_block
   
    return unpad(bytes(plaintext))

if __name__ == "__main__":
    key = b'secret_key_12345'
    iv = b'initial_vector_12'
    plaintext = b'hello, this is a secret message'
   
    print("Original Text:", plaintext)
   
    encrypted = cbc_encrypt(plaintext, key, iv)
    print("Encrypted Text:", encrypted)

    decrypted = cbc_decrypt(encrypted, key, iv)
    print("Decrypted Text:", decrypted)