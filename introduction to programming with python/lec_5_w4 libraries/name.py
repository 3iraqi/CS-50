import sys
# sys,argv  -> Argument Vector : is a magic variable that can get 
# all the words you write in command line before you hit enter.

try:
    print("hello, my name is",sys.argv[1])
except IndexError:
    print("oho who are you")