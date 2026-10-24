from Crypto.Cipher import AES

def main():
	key = b"1234567890"
	plaintext = b"helloworldnakuln"
	cipher = AES.new(key=key, mode=AES.MODE_ECB)

	enc = cipher.encrypt(plaintext=plaintext)
	print("Enc: ", enc)

	dec = cipher.decrypt(plaintext=enc)
	print("Dec: ", dec)