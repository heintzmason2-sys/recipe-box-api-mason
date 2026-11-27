from werkzeug.security import generate_password_hash, check_password_hash

password = "test-password-123"

hash_value = generate_password_hash(password)

print("HASH:", hash_value)
print("correct?", check_password_hash(hash_value, "test-password-123"))
print("wrong?", check_password_hash(hash_value, "not-the-password"))
