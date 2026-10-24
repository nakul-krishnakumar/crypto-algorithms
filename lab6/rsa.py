import math

def get_keys(p: int, q: int):
	phi = (p-1)*(q-1)

	# get public key
	e = 2
	for i in range(2, phi):
		if math.gcd(i, phi) == 1:
			e = i
			break

	# get private key
	# ed === 1 mod (phi(n))

	d = 1
	for d in range(e*phi):
		if (e*d) % phi == 1:
			break

	return e, d

def encrypt(msg: int, pub: int, n: int):
	return pow(msg, pub, n)

def decrypt(encyption: int, priv: int, n: int):
	return pow(encyption, priv, n)

def main():
	p = 3
	q = 11
	pub, priv = get_keys(p, q)

	enc = encrypt(msg=2, pub=pub, n=p*q)
	print("Enc: ", enc)

	dec = decrypt(encyption=enc, priv=priv, n=p*q)
	print("Dec: ", dec)

if __name__ == '__main__':
	main()