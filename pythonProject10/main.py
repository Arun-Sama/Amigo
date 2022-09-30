"""print("File1 __name__ = ", __name__)

if __name__ == "__main__":
    print("File1 being is run directly ")
else:
    print("File1 is imported")"""


def min():
    print("Hello")


def max():
    print("world")


def main():
    max()
    min()


if __name__ == "__main__":
    main()
