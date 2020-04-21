title = "Alice in Wonderland"
title.split()
num_words = len(title)
print("This file has " + str(num_words) + " words.")

filename = "alice.txt"

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry that file cannot be found."
    print(msg)
