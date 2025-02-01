# 2- bank.py

x=input("Greeting: ").lower().strip()

if "hello" in x:
    out=0
elif x[0]=='h':
    out =20
else:
    out=100
print(f"${out}")
