def ispalindrome(word):
    words = ""
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

    

