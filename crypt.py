from hashlib import md5
def encrypt(text: str, salt: str):
	return md5(f"{salt+text+salt}".encode()).hexdigest()
print(encrypt("gg bro", "1245683294"))