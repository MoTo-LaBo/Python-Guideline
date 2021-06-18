class MyError(Exception):

    def __str__(self):
        return "my error occurred"


if __name__ == "__main__":
    response = input("y/n?")
    try:
        if response != "y" and response != "n":
            raise MyError
    except MyError as e:
        print(e)  # e.__str__()