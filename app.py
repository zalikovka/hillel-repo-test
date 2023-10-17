
def breaking_function():
    1/0
    print("This is a function that does nothing")


def main():
    breaking_function()


if __name__ == "__main__":
    main()
