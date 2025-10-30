def is_palindrome(word):
    words = ""
    for char in word:
        if char != " ":
            words += char.lower()

    reversed_word = ""
    i = len(words) - 1
    while i >= 0:
        reversed_word += words[i]
        i -= 1

    return words == reversed_word

wordinput = input("Enter word: ")
if is_palindrome(wordinput):
    print(f"{wordinput} is a palindrome.")
else:
    print(f"{wordinput} is not a palindrome.")