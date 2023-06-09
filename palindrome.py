# 10. Write a program to palindrome or not.
# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = input("enter a string: ")
ans = isPalindrome(s)

if ans:
    print("Yes its palindrome")
else:
    print("No its not palindrome")
