import string 
import getpass

def check_pwd():
    # Securely fetch password without echoing characters to the terminal
    password = getpass.getpass("\nEnter the password to test: ")
    
    # Statistical counters
    length = len(password)
    lower = sum(1 for c in password if c in string.ascii_lowercase)
    upper = sum(1 for c in password if c in string.ascii_uppercase)
    num = sum(1 for c in password if c in string.digits)
    # Includes punctuation and whitespace as per ANSSI recommendations
    special = sum(1 for c in password if c in string.punctuation or c == ' ')
    
    # Character diversity count
    types_count = 0
    if lower > 0: types_count += 1
    if upper > 0: types_count += 1
    if num > 0: types_count += 1
    if special > 0: types_count += 1

    # Robustness criteria based on ANSSI guidelines
    is_long_enough = length >= 12
    is_complex = types_count >= 4
    
    print("-" * 45)
    print("TECHNICAL ANALYSIS:")
    print(f" - Length: {length} characters " + ("[OK]" if is_long_enough else "[TOO SHORT]"))
    print(f" - Diversity: {types_count}/4 character types " + ("[OK]" if is_complex else "[INSUFFICIENT]"))
    print("-" * 45)

    # Scoring logic and verdict
    if is_long_enough and is_complex:
        score = "STRONG"
        remarks = "Complies with ANSSI recommendations for standard user accounts."
    elif length >= 14 and types_count >= 3:
        score = "ACCEPTABLE"
        remarks = "Length compensates for lower character diversity."
    elif length < 8:
        score = "DANGEROUS"
        remarks = "Critical risk. Easily breakable via brute-force attacks."
    else:
        score = "WEAK"
        remarks = "High risk. Increase length or diversity."

    print(f"Verdict: {score}")
    print(f"Note: {remarks}")
    print("-" * 45)

def main():
    print("=== Password Robustness Tester (ANSSI Standard) ===")
    while True:
        check_pwd()
        choice = input("Do you want to test another password? (y/n): ").lower()
        if choice != 'y':
            print("Program terminated.")
            break

if __name__ == "__main__":
    main()