
def form_matrix(keyword: str):
	char_mapping: dict[str, int] = {
		chr(i): 0 for i in range(ord('A'), ord('Z') + 1)
	}
	char_mapping['J'] = 1

	mat = [['' for _ in range(5)] for _ in range(5)]
	char_idx: dict[str, list[int]] = {}

	chars = keyword + ''.join(
		ch for ch in 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
		if ch not in keyword
	)

	for idx, ch in enumerate(chars):
		if ch == 'J':
			ch = 'I'

		if char_mapping[ch]:
			continue

		i, j = divmod(len(char_idx), 5)
		mat[i][j] = ch
		char_idx[ch] = [i, j]
		char_mapping[ch] = 1

		if ch == 'I':
			char_mapping['J'] = 1

	char_idx['J'] = char_idx['I']
	return mat, char_idx


def preprocess_keyword(keyword: str):
	keyword = keyword.upper().replace('J', 'I')
	return ''.join(dict.fromkeys(
		ch for ch in keyword if ch.isalpha() and 'A' <= ch <= 'Z'
	))


def preprocess_plaintext(plaintext: str):
	plaintext = ''.join(
		ch for ch in plaintext.upper().replace('J', 'I')
		if 'A' <= ch <= 'Z'
	)

	processed = []
	i = 0

	while i < len(plaintext):
		a = plaintext[i]

		if i + 1 >= len(plaintext):
			processed.extend([a, 'X'])
			i += 1
		elif plaintext[i] == plaintext[i + 1]:
			filler = 'X' if a != 'X' else 'Q'
			processed.extend([a, filler])
			i += 1
		else:
			processed.extend([a, plaintext[i + 1]])
			i += 2

	return ''.join(processed)


def form_pairs(plaintext: str):
	return [
		plaintext[i:i + 2]
		for i in range(0, len(plaintext), 2)
	]


def encrypt(keyword: str, plaintext: str):
	keyword = preprocess_keyword(keyword)
	plaintext = preprocess_plaintext(plaintext)

	mat, char_idx = form_matrix(keyword)
	print("Matrix:")
	for row in mat:
		print(' '.join(row))

	encrypted = []

	for a, b in form_pairs(plaintext):
		a_i, a_j = char_idx[a]
		b_i, b_j = char_idx[b]

		if a_i == b_i:
			encrypted.extend([
				mat[a_i][(a_j + 1) % 5],
				mat[b_i][(b_j + 1) % 5]
			])
		elif a_j == b_j:
			encrypted.extend([
				mat[(a_i + 1) % 5][a_j],
				mat[(b_i + 1) % 5][b_j]
			])
		else:
			encrypted.extend([
				mat[a_i][b_j],
				mat[b_i][a_j]
			])

	return ''.join(encrypted)


def decrypt(keyword: str, encryption: str):
	keyword = preprocess_keyword(keyword)
	encryption = ''.join(
		ch for ch in encryption.upper().replace('J', 'I')
		if 'A' <= ch <= 'Z'
	)

	if len(encryption) % 2 != 0:
		raise ValueError("Ciphertext length must be even.")

	mat, char_idx = form_matrix(keyword)
	decrypted = []

	for a, b in form_pairs(encryption):
		a_i, a_j = char_idx[a]
		b_i, b_j = char_idx[b]

		if a_i == b_i:
			decrypted.extend([
				mat[a_i][(a_j - 1) % 5],
				mat[b_i][(b_j - 1) % 5]
			])
		elif a_j == b_j:
			decrypted.extend([
				mat[(a_i - 1) % 5][a_j],
				mat[(b_i - 1) % 5][b_j]
			])
		else:
			decrypted.extend([
				mat[a_i][b_j],
				mat[b_i][a_j]
			])

	return ''.join(decrypted)

def postprocess_plaintext(plaintext: str):
    result = []

    for i, ch in enumerate(plaintext):
        if (
            ch == 'X'
            and i > 0
            and i < len(plaintext) - 1
            and plaintext[i - 1] == plaintext[i + 1]
        ):
            continue

        result.append(ch)

    if result and result[-1] == 'X':
        result.pop()

    return ''.join(result)

def main():
	# keyword = input("Enter keyword: ")
	# plaintext = input("Enter plaintext: ")
	keyword = "nakul"
	plaintext = "indiranagar"

	enc = encrypt(keyword, plaintext)
	print("Playfair Cipher Encryption:", enc)

	dec = decrypt(keyword, enc)
	dec = postprocess_plaintext(dec)
	print("Playfair Cipher Decryption:", dec)

	expected = preprocess_plaintext(plaintext)
	print(
		"Decryption matches processed plaintext!"
		if expected == dec
		else "Decryption mismatch!"
	)


if __name__ == "__main__":
	main()
