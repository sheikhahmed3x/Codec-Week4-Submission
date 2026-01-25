import hashlib
import time

# Author: Sheikh Junayed Ahmed
# Project: Week 4 - Python Brute-Force Cracker
# Objective: Demonstrate how weak hashes (MD5) are cracked using a dictionary attack.

print("--- Python Password Cracker ---")
print("Project by: Sheikh Junayed Ahmed\n")

# 1. The Target: An MD5 hash of the word "password"
# In a real scenario, this hash would be stolen from a database.
target_hash = "5f4dcc3b5aa765d61d8327deb882cf99" 
print(f"Target Hash to Crack: {target_hash}")

# 2. The Attack: A mini 'dictionary' of common passwords
# Real hackers use lists with millions of words (like rockyou.txt).
common_passwords = ["123456", "admin", "welcome", "password", "sheikh", "football"]

print("Starting Dictionary Attack...")
start_time = time.time()

found = False
for word in common_passwords:
    # Hash the current guess
    guess_hash = hashlib.md5(word.encode()).hexdigest()
    
    # Compare with target
    if guess_hash == target_hash:
        print(f"\n[SUCCESS] Password Cracked! The password is: '{word}'")
        found = True
        break
    else:
        print(f"[-] Tried: {word} (Hash: {guess_hash})")

end_time = time.time()

if not found:
    print("\n[FAILED] Password not found in dictionary.")

print(f"Attack Duration: {end_time - start_time:.5f} seconds")
