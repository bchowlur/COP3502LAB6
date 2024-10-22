# Name: Bharath Chowlur

def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encoded_password += str(new_digit)
    return encoded_password

def decode(encoded_password):
    pass
