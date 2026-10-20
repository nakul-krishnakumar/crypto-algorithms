
def encrypt(keyword: str, plaintext: str):
	enc = ""
	for idx, ch in enumerate(plaintext):
		p = ord(ch) - ord('A')
		k = ord(keyword[idx]) - ord('A')
		e = chr(((p + k) % 26 ) + ord('A'))
		enc += e

	return enc

def decrypt(keyword: str, encryption: str):
	pt = ""
	for idx, ch in enumerate(encryption):
		e = ord(ch) - ord('A')
		k = ord(keyword[idx]) - ord('A')
		p = (e - k) % 26
		p = chr(p + ord('A'))
		pt += p

	return pt

def preprocess_keyword(keyword: str, plaintext: str):
	processed = keyword.upper()

	k, p = len(keyword), len(plaintext)
	if k == p:
		return processed
	elif k > p:
		return processed[0: p]
	
	tofill = p - k
	processed += plaintext[:tofill]
	return processed

def preprocess_plaintext(plaintext: str):
	plaintext = plaintext.upper().replace(' ', '')
	return plaintext

def main():
	keyword = "nakul"
	plaintext = "hello my name is nakul krishnakumar"

	plaintext = preprocess_plaintext(plaintext=plaintext)
	keyword = preprocess_keyword(keyword=keyword, plaintext=plaintext)

	enc = encrypt(keyword=keyword, plaintext=plaintext)
	print("Encrypted: ", enc)

	dec = decrypt(keyword=keyword, encryption=enc)
	print("Decryption: ", dec)

if __name__ == '__main__':
	main()
	
