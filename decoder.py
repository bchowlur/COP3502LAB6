# Name: Krit Dass


def decode(password):
    decoded_password = ""

    for n in password:
        n = int(n)
        n -= 3
        n %= 10

        decoded_password += str(n)

    return decoded_password
