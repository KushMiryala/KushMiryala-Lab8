
def encoder(num_list):
    encoded_password = ""
    for i in num_list:
        encoded_password += str((int(i) + 3) % 10)
    return encoded_password

def decode_password(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


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
