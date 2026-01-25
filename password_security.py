import hashlib
import bcrypt
import time

# Author: Sheikh Junayed Ahmed
# Project: Week 4 - Password Security & Hashing Analysis
# Institution: Amity University Bengaluru (AIIT)

print("--- Password Security Audit ---")
print("Project by: Sheikh Junayed Ahmed\n")

# A sample password for the demonstration
user_password = "Sheikh_Week4_Secure_2026".encode('utf-8')

# --- Part A: Weak Hashing (SHA-256) ---
print("1. Generating Standard SHA-256 Hash...")
start = time.time()
sha256_hash = hashlib.sha256(user_password).hexdigest()
print(f"   [SHA-256] Hash: {sha256_hash}")
print(f"   Time taken: {time.time() - start:.6f} seconds (Too fast = Vulnerable)\n")

# --- Part B: Secure Hashing (Bcrypt with Salt) ---
print("2. Generating Secure Bcrypt Hash (Salted)...")
start = time.time()

# Generate a random salt (cost factor 12)
salt = bcrypt.gensalt(rounds=12) 
# Hash the password with the salt
bcrypt_hash = bcrypt.hashpw(user_password, salt)

end = time.time()

print(f"   [Bcrypt] Hash: {bcrypt_hash.decode()}")
print(f"   Time taken: {end - start:.4f} seconds (Slower = More Secure)")

# --- Part C: Verification ---
print("\n3. Verifying Password for Sheikh Junayed Ahmed...")
if bcrypt.checkpw(user_password, bcrypt_hash):
    print("   Result: SUCCESS. Password matches the secure hash.")
else:
    print("   Result: FAILURE. Password does not match.")
