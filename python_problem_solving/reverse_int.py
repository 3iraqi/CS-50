
def main():
    x=123
    y=-123
    # z=(2**(-32)) > -123
    num=reverse(y)
    print(num)

def reverse(x):
    if x<0:
            return -reverse(-x)
    else:
            return int(str(x)[::-1])


if __name__ == '__main__':
    main()