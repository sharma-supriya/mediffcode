s=input("enter the string:")
s=s.casefold()
reverse=(s[::-1])
if reverse==s:
    print("It is a palindrome string")
else:
    print("not a palindrome")
