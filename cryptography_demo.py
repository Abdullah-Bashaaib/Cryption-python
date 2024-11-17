from cryptography.fernet import Fernet

# 1. Generate an encryption key and save it
key = Fernet.generate_key()
cipher = Fernet(key)

# Save the key to a file (optional)
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print(f"Encryption key (keep it safe): {key}")

# 2. The message to be encrypted
message = "This is a secret message".encode()

# 3. Encrypt the message
encrypted_message = cipher.encrypt(message)
print(f"Encrypted message: {encrypted_message}")

# 4. Decrypt the message (to verify the program works)
decrypted_message = cipher.decrypt(encrypted_message).decode()
print(f"Decrypted message: {decrypted_message}")
