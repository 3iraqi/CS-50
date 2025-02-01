# 5- meal.py
"""
breakfast   - 07:00 , 08:00
lunch       - 12:00 , 13:00
dinner      - 18:00 , 19:00
"""
def main():
    time = convert(input("what time is it? "))

    if 7<= time  <= 8:
        print("breakfast time")
    elif 12<= time  <= 13:
        print("lunch time")
    elif 18<= time  <= 19:
        print("dinner time")


def convert(time):
    h,m = time.strip().split(':')
    converted_time = float(int(h) * 60 + int(m))/60  # convert to minutes
    return converted_time


if __name__ == "__main__":
    main()
