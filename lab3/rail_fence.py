
"""
G _ _ _ _ _ _ _ G _ _ _ _
- E _ _ _ _ _ R _ E _ _
- - E _ _ _ 0 _ _ _ E
_ _ _ K _ F _ _ _ _ _ K
_ _ _ _ S _ _ _ _ _ _ _ S
"""

def encrypt(plaintext: str, num_rails: int):
	plen = len(plaintext)
	enc = ["" for _ in range(num_rails)]

	i = 0
	direction = 1
	rail = 0
	while i < plen:
		enc[rail] += plaintext[i]

		if num_rails - rail == 1:
			direction = -1
		elif rail == 0:
			direction = 1
		rail += direction

		i += 1
	
	return "".join(enc)

def decrypt(encryption: str, num_rails: int):
    n = len(encryption)

    if num_rails <= 1:
        return encryption

    # Step 1: Recreate the zigzag pattern
    pattern = []
    rail = 0
    direction = 1

    for i in range(n):
        pattern.append(rail)

        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1

        rail += direction

    # Step 2: Fill each rail with ciphertext characters
    rails = ["" for _ in range(num_rails)]
    idx = 0

    for r in range(num_rails):
        count = pattern.count(r)
        rails[r] = encryption[idx:idx + count]
        idx += count

    # Step 3: Read characters following the zigzag pattern
    positions = [0] * num_rails
    plaintext = ""

    for r in pattern:
        plaintext += rails[r][positions[r]]
        positions[r] += 1

    return plaintext

def main():
	plaintext = "GEEKSFORGEEKS"
	num_rails = 3

	enc = encrypt(plaintext=plaintext, num_rails=num_rails)
	print("Encryption: ", enc)

	dec = decrypt(encryption=enc, num_rails=num_rails)
	print("Decryption: ", dec)

if __name__ == "__main__":
	main()