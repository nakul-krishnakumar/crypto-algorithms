import numpy as np

def process_plaintext(plaintext: str):
	mat = []
	i = 0
	while i < len(plaintext):
		a = ord(plaintext[i]) - ord('A')
		if i + 1 < len(plaintext):
			b = ord(plaintext[i + 1]) - ord('A')
		else:
			b = ord('X') - ord('A')
		mat.append([a, b])
		i += 2
	return mat

def encrypt(key_mat: list[list[int]], plaintext: str):
	pt_vec = process_plaintext(plaintext=plaintext)

	# C = KM mod 26
	enc = ""
	for vec in pt_vec:
		e0 = (key_mat[0][0] * vec[0] +
		      key_mat[0][1] * vec[1]) % 26

		e1 = (key_mat[1][0] * vec[0] +
		      key_mat[1][1] * vec[1]) % 26

		enc += chr(e0 + ord('A')) + chr(e1 + ord('A'))
	return enc
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("Modular inverse does not exist")

def matrix_inverse_2x2(key):
    a, b = key[0]
    c, d = key[1]

    det = (a * d - b * c) % 26
    det_inv = mod_inverse(det, 26)

    return [
        [(det_inv * d) % 26, (det_inv * -b) % 26],
        [(det_inv * -c) % 26, (det_inv * a) % 26]
    ]

def decrypt(key_mat: list[list[int]], encryption: str):
    enc_vec = process_plaintext(encryption)
    key_inv = matrix_inverse_2x2(key_mat)

    pt = ""
    for vec in enc_vec:
        p0 = (key_inv[0][0] * vec[0] +
              key_inv[0][1] * vec[1]) % 26

        p1 = (key_inv[1][0] * vec[0] +
              key_inv[1][1] * vec[1]) % 26

        pt += chr(p0 + ord('A')) + chr(p1 + ord('A'))

    return pt

def main():
	key_mat = [[3, 3], [2, 5]]
	plaintext = "ATTACK"
	enc = encrypt(key_mat=key_mat, plaintext=plaintext)
	print("Enc: ", enc)

	dec = decrypt(key_mat=key_mat, encryption=enc)
	print("Dec: ", dec)

main()