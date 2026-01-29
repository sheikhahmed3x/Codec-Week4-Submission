# My Approach & Technical Justification
**Author:** Sheikh Junayed Ahmed

## Why I Chose a Hybrid Toolset 🛠️
For this Week 4 submission, I decided to combine **custom Python scripting** with **industry-standard tools** (John the Ripper). This hybrid approach allows me to demonstrate two distinct skill sets:

1.  **Algorithmic Understanding (Python):** Writing the logic from scratch ensures I understand *how* the attacks work mathematically.
2.  **Operational Proficiency (John the Ripper):** Using established tools demonstrates that I can perform real-world audits efficiently.

## My Project Approach

### 1. Cryptography Algorithms Implementation
* **The Solution:** I implemented a **Hybrid approach**—using RSA to exchange the key and AES to encrypt the message. This mirrors how actual protocols like **TLS/SSL** work.

### 2. Password Cracking and Hashing Algorithms
* **Phase A: The Math (Python Script):** I wrote `password_security.py` to benchmark **SHA-256** vs. **Bcrypt**, proving the necessity of "Salting".
* **Phase B: The Real-World Attack (John the Ripper):**
    * I utilized **John the Ripper** to crack raw MD5 hashes.
    * **Evidence:** I have included screenshots (`john_output.png`) in this repository to verify the successful execution of these tools in a Linux environment.
