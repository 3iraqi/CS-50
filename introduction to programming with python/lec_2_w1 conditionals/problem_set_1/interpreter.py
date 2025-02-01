
# 4- interpreter.py

x,y,z=input("Expression: ").strip().split(" ")

if y =='+':
    print(round(float(x)+float(z),1))
elif y == '-':
    print(round(float(x)-float(z),1))
elif y == '*':
    print(round(float(x)*float(z),1))
elif y == '/':
    print(round(float(x)/float(z),1))

