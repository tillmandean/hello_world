with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

print('')

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))




filename = 'pi_million_digits.txt'

with open(filename) as big_file:
    lines = big_file.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


# 'w' is for writing mode... 'a' is for appending mode
file = 'programmming.txt'
with open(file, 'w') as file_object:
    file_object.write("I love programmming.")


#try-except blocks to prevent program from crashing
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)
