
def preprocess_keyword(keyword: str, pt_len: int):
	keyword = keyword.upper()
	processed = ""

	if pt_len < len(keyword):
		processed = keyword[0: pt_len]
		return processed

	elif pt_len == len(keyword):
		return keyword

	count = int(pt_len / len(keyword))
	rem = pt_len % len(keyword)
	
	processed = keyword * count
	processed += keyword[0: rem]
	return processed

def preprocess_plaintext(plaintext: str):
	plaintext = plaintext.upper().replace(' ', '')
	return plaintext

def encrypt(keyword: str, plaintext: str):
	enc = ""
	for idx, ch in enumerate(plaintext):
		p = ord(ch) - 65
		k = ord(keyword[idx]) - 65
		e = chr(( (p + k) % 26 ) + 65)
		enc += e
	return enc

def decrypt(keyword: str, encryption: str):
	pt = ""
	for idx, ch in enumerate(encryption):
		e = ord(ch) - ord('A')
		k = ord(keyword[idx]) - ord('A')
		p = e - k
		if p < 0:
			p += 26
		p = chr(p + ord('A'))
		pt += p

	return pt

def main():
	keyword = "nakul"
	plaintext = "hello my name is manasa manoj"

	plaintext = preprocess_plaintext(plaintext=plaintext)
	keyword = preprocess_keyword(keyword=keyword, pt_len=len(plaintext))

	enc = encrypt(keyword=keyword, plaintext=plaintext)
	print("Encryption: ", enc)

	dec = decrypt(keyword=keyword, encryption=enc)
	print("Decryption: ", dec)

if __name__ == '__main__':
	main()