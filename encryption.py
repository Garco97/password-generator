from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open(".secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open(".secret.key", "rb").read()  

def encrypt_message(message):
    key = load_key()
    message = message.encode()
    f = Fernet(key)
    return f.encrypt(message)

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()