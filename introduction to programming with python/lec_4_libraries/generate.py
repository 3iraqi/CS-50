import random

dice=random.choice([1,2,3,4,5,6])
cards=["jack","queen","King"]
random.shuffle(cards)
print(cards)
print(random.randint(1,9))

print(dice)