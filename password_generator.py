import random

def password_generator(length):
    UPPER = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
    LOWER = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
    NUMS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    CHARS = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"')

    string = UPPER + LOWER + NUMS + CHARS

    password = []

    for i in range(length):
        random_character = random.choice(string)
        password.append(random_character)

    password = "".join(password)
    return password

def run():
    length = int(input("How long do you want your password to be? (minimun recommended: 15) "))
    password = password_generator(length)
    print("Your random secure password is: " + password)

if __name__ == "__main__":
    run()
    