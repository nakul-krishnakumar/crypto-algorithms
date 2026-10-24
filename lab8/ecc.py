def add(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        slope = ((3 * x1 * x1 + a) * pow(2 * y1, -1, p)) % p
    else:
        slope = ((y2 - y1) * pow((x2 - x1) % p, -1, p)) % p

    x3 = (slope * slope - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return x3, y3


def multiply(k, P, a, p):
    result = None

    while k > 0:
        if k & 1:
            result = add(result, P, a, p)

        P = add(P, P, a, p)
        k >>= 1

    return result


def main():
    p = 17
    a = 2
    b = 2
    G = (5, 1)

    if (G[1] ** 2 - (G[0] ** 3 + a * G[0] + b)) % p != 0:
        raise ValueError("Base point is not on the curve")

    alice_private = int(input("Enter Alice's private key: "))
    bob_private = int(input("Enter Bob's private key: "))

    alice_public = multiply(alice_private, G, a, p)
    bob_public = multiply(bob_private, G, a, p)

    print("Alice's public key:", alice_public)
    print("Bob's public key:", bob_public)

    alice_shared = multiply(alice_private, bob_public, a, p)
    bob_shared = multiply(bob_private, alice_public, a, p)

    print("Alice's shared secret:", alice_shared)
    print("Bob's shared secret:", bob_shared)
    print("Keys match:", alice_shared == bob_shared)


if __name__ == "__main__":
    main()