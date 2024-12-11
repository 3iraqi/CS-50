
def main():
    x=123
    y=-123
    z=1563847412
    # z=(2**(-32)) > -123
    num=reverse(z)
    print(num)

#NOTE : This is First Solution  42ms Beats 17.81% LeetCode
def reverse(x):
        reversed_x=int(str(x)[::-1])if x>0 else (int(str(-x)[::-1]))
        if reversed_x>((2**31)-1):
                return 0
        elif x<0:
            return -reverse(-x)
        else:
            return int(str(x)[::-1])


if __name__ == '__main__':
    main()