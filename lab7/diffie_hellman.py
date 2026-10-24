
def get_alice_public_key(q, g):
	a = 3
	return pow(g, a, q)

def get_bob_public_key(q, g):
	b = 5
	return pow(g, b, q)

def calc_alice_shared_secret(q, B):
	a = 3
	print("shared secret key: ", pow(B, a, q))

def main():
	q = 17 # prime number
	g = 5  # primitive root

	A = get_alice_public_key(q, g)
	B = get_bob_public_key(q, g)

	print("shared keys: ", A, ",", B)

	calc_alice_shared_secret(q, B)

if __name__ == "__main__":
	main()