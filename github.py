
def encoder(num_list):
    encoded_password = ""
    for i in num_list:
        encoded_digit = str((int(i) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

print(encoder("00009962"))

