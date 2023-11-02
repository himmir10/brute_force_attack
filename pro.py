import zipfile
import itertools
import time

def try_password(zip_file, password):
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        return True
    except:
        return False

def brute_force_zip(zip_path, charset, max_length):
    zip_file = zipfile.ZipFile(zip_path)
    attempts = 0

    for password_length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=password_length):
            attempts += 1
            password = ''.join(guess)
            if try_password(zip_file, password):
                return (password, attempts)
    return (None, attempts)

if __name__ == '__main__':
    # Define the path to the ZIP file here
    zip_path = 'D:\Downloads\protected.zip'

    charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_'

    # Define the maximum length of the passwords to try
    max_length = 4  # Adjust this as needed

    start_time = time.time()
    print("Starting brute-force attack...")
    password, attempts = brute_force_zip(zip_path, charset, max_length)
    end_time = time.time()

    if password:
        print(f"Password found: {password}")
        print(f"Total attempts: {attempts}")
        print(f"Time taken: {end_time - start_time} seconds")
    else:
        print("Password not found. Try expanding your character set or increasing the maximum length.")
        print(f"Total attempts: {attempts}")
        print(f"Time taken: {end_time - start_time} seconds")
