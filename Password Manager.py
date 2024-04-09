import sqlite3
from cryptography.fernet import Fernet
import os


class PasswordManager:
    def __init__(self, db_name='passwords.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                              (id INTEGER PRIMARY KEY,
                               website TEXT NOT NULL,
                               username TEXT NOT NULL,
                               password TEXT NOT NULL)''')
        self.conn.commit()

    def generate_key(self):
        if os.path.exists("key.key"):
            return open("key.key", "rb").read()
        else:
            key = Fernet.generate_key()
            with open("key.key", "wb") as key_file:
                key_file.write(key)
            return key

    def encrypt_password(self, password):
        key = self.generate_key()
        cipher_suite = Fernet(key)
        return cipher_suite.encrypt(password.encode())

    def decrypt_password(self, encrypted_password):
        key = self.generate_key()
        cipher_suite = Fernet(key)
        return cipher_suite.decrypt(encrypted_password).decode()

    def add_password(self, website, username, password):
        encrypted_password = self.encrypt_password(password)
        self.cursor.execute('''INSERT INTO passwords (website, username, password)
                               VALUES (?, ?, ?)''', (website, username, encrypted_password))
        self.conn.commit()

    def get_password(self, website):
        self.cursor.execute('''SELECT password FROM passwords WHERE website = ?''', (website,))
        encrypted_password = self.cursor.fetchone()
        if encrypted_password:
            return self.decrypt_password(encrypted_password[0])
        else:
            return None

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    password_manager = PasswordManager()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            password_manager.add_password(website, username, password)
            print("Password added successfully!")
        elif choice == '2':
            website = input("Enter website: ")
            password = password_manager.get_password(website)
            if password:
                print(f"Password for {website}: {password}")
            else:
                print("Password not found!")
        elif choice == '3':
            password_manager.close()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
