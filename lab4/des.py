from Crypto.Cipher import DES

class DESCipher:
	def __init__(self, key: bytes):
		self.cipher = DES.new(key, DES.MODE_ECB)

	def encrypt(self, plaintext: bytes):
		return self.cipher.encrypt(plaintext)

	def decrypt(self, encryption: bytes):
		return self.cipher.decrypt(encryption)

class DoubleDESCipher:
	def __init__(self, key1: bytes, key2: bytes):
		self.cipher1 = DESCipher(key=key1)
		self.cipher2 = DESCipher(key=key2)

	def encrypt(self, plaintext: bytes):
		enc = self.cipher1.encrypt(plaintext=plaintext)
		enc = self.cipher2.encrypt(plaintext=enc)
		return enc

	def decrypt(self, encryption: bytes):
		dec = self.cipher2.decrypt(encryption=encryption)
		dec = self.cipher1.decrypt(encryption=dec)
		return dec


class TripleDESCipher:
	def __init__(self, key1: bytes, key2: bytes, key3: bytes):
		self.cipher1 = DESCipher(key=key1)
		self.cipher2 = DESCipher(key=key2)
		self.cipher3 = DESCipher(key=key3)

	def encrypt(self, plaintext: bytes):
		enc = self.cipher1.encrypt(plaintext=plaintext)
		enc = self.cipher2.decrypt(enc)
		enc = self.cipher3.encrypt(plaintext=enc)
		return enc

	def decrypt(self, encryption: bytes):
		dec = self.cipher3.decrypt(encryption=encryption)
		dec = self.cipher2.encrypt(plaintext=dec)
		dec = self.cipher1.decrypt(encryption=dec)
		return dec

def main():
	key1 = b"39439381"
	key2 = b"28476828"
	key3 = b"10395737"
	plaintext = b"nakulkrs"
	# cipher = DESCipher(key=key1)
	# cipher = DoubleDESCipher(key1=key1, key2=key2)
	cipher = TripleDESCipher(key1=key1, key2=key2, key3=key3)

	enc = cipher.encrypt(plaintext=plaintext)
	print("Enc: ", enc.hex().upper())

	dec = cipher.decrypt(encryption=enc)
	print("Dec: ", dec.decode())

if __name__ == "__main__":
	main()