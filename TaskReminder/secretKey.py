import secrets

# Generate a random 32-byte secret key
secret_key = secrets.token_hex(32)
print(secret_key)
