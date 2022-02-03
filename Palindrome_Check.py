def isPalindrome(s):
    rev = ''.join(reversed(s))
    if s == rev:
        return True
    return False

ans = isPalindrome("")

if (ans):
    print("Yes")
else:
    print("No")