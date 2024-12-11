
x=121
y=-121
z=10



def isPalindrome(x):
    if str(x)== str(x)[::-1]:
        return True
    return False 
print(isPalindrome(z))