from pathlib import Path

# check key
def get_fernet():
    key_path = Path('.key.txt')

    if not key_path.exists():
        key = Fernet.generate_key()
        key_path.write_bytes(key)
    else:
        key = key_path.read_bytes()
        if key == b'':
            key = Fernet.generate_key()
            key_path.write_bytes(key)

    return Fernet(key)

