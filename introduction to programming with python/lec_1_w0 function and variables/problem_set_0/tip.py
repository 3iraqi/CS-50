def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    fd=float(d.strip("$"))
    return fd


def percent_to_float(p):
    fp=float(p.strip("%"))/100
    return fp

if __name__ == "__main__":
    main()
