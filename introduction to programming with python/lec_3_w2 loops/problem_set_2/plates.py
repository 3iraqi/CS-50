from string import ascii_letters as aBc
from string import punctuation as pnc
from string import whitespace as spc
from string import digits as nums 


def main():
    plt = input("Plate: ")
    if is_valid(plt):
        print("Valid")
    else:
        print("Invalid")

#  all plates 
# All vanity plates must start with at least two letters.”
#  * plt[0] in abc and plt[1] in abc
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and
# a minimum of 2 characters.”
# * 2 <len(plt) <= 6
# “Numbers cannot be used in the middle of a plate; they must come at the end. 
# For example, AAA222 would be an acceptable … vanity plate; 
# AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# 
# “No periods, spaces, or punctuation marks are allowed.”
# * all(plt) not in spc and pnc
# 
#
#
def is_valid(s):
    global nums,spc,pnc,aBc
    
    if 2<len(s)<=6  and s[0] and s[1] in aBc and all(char not in spc and char not in pnc for char in s ):
        if any( char in  nums for char in s):
            chkr=[]
            collect=False
            for i in s:
                if i in nums:
                    collect=True
                if collect:
                    chkr.append(i)
            if  chkr[0]!='0' and all(char not in aBc for char in chkr):
                return True
            else:
                return False
        return True
    return False

if __name__ == "__main__":
    main()