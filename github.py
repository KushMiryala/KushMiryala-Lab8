
def encoder(num_list):
    encoded_password = ""
    for i in num_list:
        encoded_password += str((int(i) + 3) % 10)
    return encoded_password


def decode(encoded_password: str):
    decoded_password = ""
    for num in encoded_password:
        decoded_password += str((int(num) - 3) % 10)
    return decoded_password


print(encoder("00009962"))
print(decode("33332295"))

