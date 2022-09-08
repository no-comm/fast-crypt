from hashlib import md5
def encrypt(text: str, salt: str):
	s = text+str(md5(f"{text+salt}".encode()))
	return md5(f"{salt+f'{md5(text.encode())}'}".encode()).hexdigest()
print(encrypt("gg bro", "1245683294"))