<<<<<<< HEAD
def ispalindrome(word):
    words = ""
=======

    
def is_palindrome(word):

    words = " "
>>>>>>> d4b96b54d4fffa7ca996b76cf32849e19b013c7a
    for char in word:
        if char != " ":
            words += char.lower()

    reversedword = ""
    i = len(words) - 1
    while i >= 0:
        reversedword += words[i]
        i -= 1

    return words == reversedword

wordinput = input("Enter word: ")
if ispalindrome(wordinput):
    print(f"{wordinput} is a palindrome.")
else:
    print(f"{wordinput} is not a palindrome.")

    

wordinput = input ("Enter word")

if is_palindrome(wordinput):
    print(f"{wordinput} is a palindrome.")
else(f"{wordinput}"):
    for char in wordinput:
        g