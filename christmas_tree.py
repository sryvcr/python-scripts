def make_branches():
    for branch in range(1,20,2):
        print(('*'*branch).center(20))


def make_stem():
    for _ in range(3):
        print(('| |').center(20))


def make_foot():
    print(('\=====/').center(20))


if __name__ == "__main__":
    make_branches()
    make_stem()
    make_foot()
