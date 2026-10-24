def encrypt(plaintext: str, keyword: str):
	enc = ""
	pad = len(keyword)
	plen = len(plaintext)

	order = [0]*pad # mapping from rank to col, use rank as key and get the col at that rank
	for idx, col in enumerate(keyword):
		order[int(col) - 1] = idx 

	for col in order:
		j = col
		while j < plen:
			enc += plaintext[j]
			j += pad
	return enc

def decrypt(encryption: str, keyword: str):
    n = len(encryption)
    cols = len(keyword)
    rows = (n + cols - 1) // cols

    order = [0] * cols
    for idx, col in enumerate(keyword):
        order[int(col) - 1] = idx

    # Calculate how many characters belong to each original column
    col_lengths = [rows if c < n % cols or n % cols == 0 else rows - 1
                   for c in range(cols)]

    # Handle the case where the final row is incomplete
    if n % cols != 0:
        col_lengths = [rows if c < n % cols else rows - 1 for c in range(cols)]

    # Split ciphertext into columns in key order
    columns = [""] * cols
    pos = 0
    for col in order:
        length = col_lengths[col]
        columns[col] = encryption[pos:pos + length]
        pos += length

    # Read row by row
    pt = ""
    for r in range(rows):
        for c in range(cols):
            if r < len(columns[c]):
                pt += columns[c][r]

    return pt


def main():
	plaintext = "ATTACKATDAWN"
	keyword = "3142"

	enc = encrypt(plaintext=plaintext, keyword=keyword)
	print("Encryption: ", enc)

	dec = decrypt(encryption=enc, keyword=keyword)
	print("Decryption: ", dec)

if __name__ == "__main__":
	main()