from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# 1. Generate a random key (256-bit for AES)
key = os.urandom(32)  # 32 bytes for AES-256
print(f"Encryption key (keep it safe): {key}")

# 2. The message to be encrypted
message = "This is a secret message".encode()

# 3. Pad the message to make it a multiple of the block size (16 bytes for AES)
padder = padding.PKCS7(128).padder()  # AES block size is 128 bits
padded_message = padder.update(message) + padder.finalize()

# 4. Encrypt the message using AES in ECB mode
cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
encryptor = cipher.encryptor()
encrypted_message = encryptor.update(padded_message) + encryptor.finalize()

print(f"Encrypted message: {encrypted_message}")

# 5. Decrypt the message
decryptor = cipher.decryptor()
decrypted_padded_message = decryptor.update(encrypted_message) + decryptor.finalize()

# 6. Remove padding from the decrypted message
unpadder = padding.PKCS7(128).unpadder()
decrypted_message = unpadder.update(decrypted_padded_message) + unpadder.finalize()

print(f"Decrypted message: {decrypted_message.decode()}")
