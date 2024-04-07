from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_credit_card(card_number):
    encrypted_card_number = cipher_suite.encrypt(card_number.encode())
    return encrypted_card_number

def decrypt_credit_card(encrypted_card_number):
    decrypted_card_number = cipher_suite.decrypt(encrypted_card_number)
    return decrypted_card_number.decode()

# Encrypting credit card information
credit_card_number = "1234567812345678"  # Example credit card number
encrypted_card_number = encrypt_credit_card(credit_card_number)
print("Encrypted:", encrypted_card_number)

# Decrypting credit card information
decrypted_card_number = decrypt_credit_card(encrypted_card_number)
print("Decrypted:", decrypted_card_number)
