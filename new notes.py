listofnames = ["Alice", "bob", "Charlie", "Darwin"]
file = open("Names. txt","r")
buffer = file.readlines()
print(buffer)
file.close()
