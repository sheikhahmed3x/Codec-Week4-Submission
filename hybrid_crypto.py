from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Author: Sheikh Junayed Ahmed
# Project: Week 4 - Hybrid Encryption (RSA + AES)
# Institution: Amity University Bengaluru (AIIT)

print("--- Secure Communication System ---")
print("Project by: Sheikh Junayed Ahmed\n")

# 1. Generate RSA Keys
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# 2. Encryption
message = "Hello, my name is Sheikh Junayed Ahmed. I am from M.Sc. Cyber Security, Amity University Bengaluru.".encode("utf-8")
recipient_key = RSA.import_key(public_key)
session_key = get_random_bytes(16) 

# Encrypt Session Key (RSA)
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Encrypt Message (AES)
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(message)

print(f"Status: Message encrypted by Sheikh Junayed Ahmed")
print(f"Ciphertext: {ciphertext.hex()[:50]}...\n")

# 3. Decryption
private_rsa_key = RSA.import_key(private_key)
cipher_rsa = PKCS1_OAEP.new(private_rsa_key)
decrypted_session_key = cipher_rsa.decrypt(enc_session_key)

cipher_aes = AES.new(decrypted_session_key, AES.MODE_EAX, cipher_aes.nonce)
decrypted_data = cipher_aes.decrypt_and_verify(ciphertext, tag)

print(f"Decryption Successful!")
print(f"Decrypted Content: {decrypted_data.decode('utf-8')}")
