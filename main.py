import os
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import random
import string

def get_filename(filepath):
    return os.path.basename(filepath)

def generate_random_letters(length=4):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_filename():
    random_part = generate_random_letters()
    return f"d3xp4-{random_part}.ink"

def encrypt_file(password, filepath):
    # Генерация ключа на основе пароля  
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'salt_', 
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)

    # Чтение и шифрование файла
    with open(filepath, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    
    # Генерируем новое имя файла
    new_filename = generate_filename()
    
    # Сохраняем в корневой папке проекта
    encrypted_filepath = os.path.join(os.path.dirname(__file__), new_filename)
    
    with open(encrypted_filepath, 'wb') as file:
        file.write(encrypted_data)
        
    return encrypted_filepath

def main():
    password = "12qwaszx3edc44"
    filepath = "/Users/user/Documents/GitHub/safe/porno.txt"
    
    filename = get_filename(filepath)
    print(f"Шифруется файл: {filename}")
    
    try:
        encrypted_file = encrypt_file(password, filepath)
        print(f"Файл успешно зашифрован: {encrypted_file}")
    except Exception as e:
        print(f"Ошибка при шифровании: {str(e)}")

    filename = generate_filename()
    print(f"Сгенерированное имя файла: {filename}")

if __name__ == "__main__":
    main()