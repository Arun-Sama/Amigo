from main import min

"""print("File2 name = ", __name__)

if __name__ == "__main__":
    print("File2 is being run directly")
else:
    print("File2 is being imported")"""


def add():
    min()
    print("Addition")


def sub():
    print("Subtraction")


def main():
    add()
    sub()


main()
