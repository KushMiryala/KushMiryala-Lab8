
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

def main():
    encoded_password = ""
    while True:
        menu_selection = input(str("Please enter an option: "))
        if menu_selection == '1':
            password = input(str("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            encoded_password = encoder(password)
        elif menu_selection == '2':
            original_password = decode_password(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}")
        elif menu_selection == '3':
            break

if __name__ ==  "__main__":
    main()
