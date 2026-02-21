# Password Robustness Tester (ANSSI Standard)

##  Overview
This Python-based utility evaluates password strength based on the **ANSSI (French National Cybersecurity Agency)** official recommendations (Deliberation n° 2022-131). 

In modern cybersecurity, length is often more critical than complexity alone. This tool provides a professional assessment by prioritizing **entropy** and **length**, ensuring users create passwords capable of resisting brute-force attacks.


##  Key Features
* **Secure Input**: Implements the `getpass` module to hide password entry in the terminal, preventing "shoulder surfing" risks.
* **ANSSI Alignment**: Specifically checks for the recommended **12-character minimum** and the presence of **4 distinct character types**.
* **Technical Feedback**: Provides a detailed breakdown of lowercase, uppercase, numeric, and special characters.
* **Clean & Professional Output**: Uses standard technical indicators (`[OK]`, `[TOO SHORT]`) without distracting emojis, suitable for corporate or academic environments.

##  Technical Criteria
The script validates passwords against the following categories:
1. **Length**: Total character count.
2. **Character Diversity**:
   - Lowercase (`a-z`)
   - Uppercase (`A-Z`)
   - Digits (`0-9`)
   - Special Characters (Punctuation and whitespaces)

##  Installation & Usage
1. Ensure Python 3.x is installed on your system.
2. Download `check_pwd.py`.
3. Run the script via your terminal:

```   python check_pwd.py   ```

## Output 
``` 
=== Password Robustness Tester (ANSSI Standard) ===

Enter the password to test: 
---------------------------------------------
TECHNICAL ANALYSIS:
 - Length: 14 characters [OK]
 - Diversity: 4/4 character types [OK]
---------------------------------------------
Verdict: STRONG
Note: Complies with ANSSI recommendations for standard user accounts.
---------------------------------------------
Do you want to test another password? (y/n):        ```
