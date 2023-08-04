import string
from random import choices


if __name__ == '__main__':
    # Generate a random string with 6 characters (a-z, A-Z, 0-9)
    flag: str = ''.join(choices(string.ascii_letters + string.digits, k=6))

    with open("config/flag.txt", "w") as f:
        f.write(flag)

    print("Flag generated!")
