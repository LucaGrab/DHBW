import hashlib

def generate_md5_hash(password):
    """Generates MD5 hash for the given password."""
    return hashlib.md5(password.encode()).hexdigest()

def test_password(md5_hash, password_file):
    """Tests passwords from a file and compares their MD5 hash with the given hash."""
    with open(password_file, 'r', encoding='utf-8') as file:
        for line in file:
            password = line.strip()
            if generate_md5_hash(password) == md5_hash:
                return password
    return None

def main():
    md5_hash = "7c6a180b36896a0a8c02787eeafb0e4c"  # Beispiel-MD5-Hash
    password_file = "passwords.txt"  # Beispiel-Dateiname mit Passwörtern

    found_password = test_password(md5_hash, password_file)
    if found_password:
        print("Das Passwort ist:", found_password)
    else:
        print("Kein passendes Passwort gefunden.")

if __name__ == "__main__":
    main()
