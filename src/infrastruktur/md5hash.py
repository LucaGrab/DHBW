import hashlib

def generate_md5_hash(password):
    """Generates MD5 hash for the given password."""
    return hashlib.md5(password.encode()).hexdigest()

def test_password(md5_hash):
    """Tests passwords of varying lengths and compares their MD5 hash with the given hash."""
    password_length = 1
    while True:
        for i in range(10 ** password_length):
            password = str(i).zfill(password_length)
            if generate_md5_hash(password) == md5_hash:
                return password
        password_length += 1

def main():
    # Das gesuchte MD5-Hash
    md5_hash = "81dc9bdb52d04dc20036dbd8313ed055"  # Beispiel-MD5-Hash für das Passwort "password"

    found_password = test_password(md5_hash)
    if found_password:
        print("Das Passwort ist:", found_password)
    else:
        print("Kein passendes Passwort gefunden.")

if __name__ == "__main__":
    main()
