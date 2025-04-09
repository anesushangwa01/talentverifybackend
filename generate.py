from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key.decode())  # Prints the 32-byte base64 URL-safe key
