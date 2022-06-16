import random

def password_generator():
    UPPER = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
    LOWER = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
    NUMS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    CHARS = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"')

    string = UPPER + LOWER + NUMS + CHARS

    password = []

    for i in range(16):
        random_character = random.choice(string)
        password.append(random_character)

    password = "".join(password)
    return password

def run():
    password = password_generator()
    print("Your random secure password is: " + password)

if __name__ == "__main__":
    run()
    