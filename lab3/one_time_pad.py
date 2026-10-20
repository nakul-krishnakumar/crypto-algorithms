
def encrypt(keyword: str, plaintext: str):
	enc = ""
	for idx, ch in enumerate(plaintext):
		p = ord(ch) - ord('A')
		k = ord(keyword[idx]) - ord('A')

		e = chr(((p + k) % 26) + ord('A'))
		enc += e
	return enc

def decrypt(keyword: str, encyption: str):
	pt = ""
	for idx, ch in enumerate(encyption):
		e = ord(ch) - ord('A')
		k = ord(keyword[idx]) - ord('A')

		p = chr( ((e - k) % 26) + ord('A'))
		pt += p
	return pt


def main():
	keyword = "NAKUL"
	plaintext = "HELLOMYNAMEISNAKULKRISHNAKUMAR"

	enc = encrypt(keyword=keyword, plaintext=plaintext)
	print("Encryption: ", enc)

	dec = decrypt(keyword=keyword, encyption=enc)
	print("Decryption: ", dec)