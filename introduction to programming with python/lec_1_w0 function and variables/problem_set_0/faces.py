
def main ():
    print( convert(input()))


def convert(x):
    return x.replace(":)","🙂").replace(":(","🙁")


if __name__ == "__main__":
    main()
