
    
def is_palindrome(word):

    words = ""
    for char in word:
        if char != " ":
            words = words + char.lower()
            
    reversed = " "
    i = len(words) -1 
    while i >= 0:
        revesred = reversed + words[i]
        i = i -1

    return words == revesred

wordinput = input ("Enter word")
if is_palindrome(wordinput):
    print(f"{wordinput} is a palindrome.")
else (f"{wordinput}"):