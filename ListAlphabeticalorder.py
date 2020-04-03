handle = open("facts.txt", "r")
words = handle.readlines()
handle.close()
words.sort()
print("Words in an alphabetical order:")
for i in words:
    print(i[:-1])
