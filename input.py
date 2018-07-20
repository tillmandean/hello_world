age = input("What is your age? ")
print("You are " + str(age) + " years old")

name_of_user = input("What is your name? ")
print("Hello " + name_of_user)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

start_num = 1
while start_num <= 10:
    print(start_num)
    start_num += 1

prompt = "\nTell me somthing, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


prompt_2 = "\nEnter a city that you have visited "
prompt_2 += "\nEnter 'quit' to end the program."

while True:
    message = input(prompt_2)
    if message == 'quit':
        break
    else:
        print("Really, I'd love to go there")


#continue executes the rest of the code in the loop
while True:
    message = input(prompt_2)
    if message == 'quit':
        continue
    else:
        print("Really, I'd love to go there")

unconfirmed_users = ['tillman', 'william', 'caroline']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


positions = ['CM', 'CB', 'CB', "RB", 'LB', "CM", "CDM", "CAM", "LW", "RW", "ST", "CDM"]
while 'CDM' in positions:
    positions.remove('CDM')

print(positions)

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("What football team do you support? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " supports " + response + ".")


