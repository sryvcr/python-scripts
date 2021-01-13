import random


def gen_password(length: int):
    """
        generate password with lower & upper letters, numbers and symbols
    """
    letters: str = "abcdefghijklmnopqrstuvwxyz"
    numbers: str = "1234567890"
    symbols: str = "!&^#*%$@"

    _all = letters + letters.upper() + numbers + symbols
    passwd_len = validate_password_length(length)

    password = "".join(random.sample(_all, passwd_len))
    print(f"you password is: {password}")

    return


def validate_password_length(length: int):
    """
        if length less than 12, set [length=12] default
    """
    if length < 12:
        length = 12
    return length


if __name__ == "__main__":
    passwd_len: int = int(input('please, enter number greater than 12 to set password length: '))
    gen_password(passwd_len)
