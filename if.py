cars = ['audi', 'bmw', 'porsche', 'volkswagen']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


height = '6 foot 4 inches'
age = 25

if age == 25:
    print('He is 25')
if (age == 25) and (height == '6 foot 4 inches'):
    print('Welcome to Liverpool Football Club, Mr. Alisson Becker!')
else:
    print('Sorry sir you are going to have to go back to Rome.')

if (cars[-1] == 'volkswagen') or (cars[-1] == 'mercedes') or (cars[-1] == 'nissan'):
    print("That's one of the Dean's cars!")
if('porsche' in cars):
    print('Yes, I have a Porsche.')
if('aston martin' not in cars):
    print("I don't have an Aston Martin")


if age >= 21:
    print("You're old enough to drink.")
else:
    print("You're not old enough to drink yet.")

if age < 18:
    print("You can't vote.")
elif age >= 18 and age < 21:
    print("You can vote, but you can't drink.")
else:
    print("You can vote and drink.")


toppings = []
if toppings:
    for topping in toppings:
        print("Adding " + topping + ".")
    print("\n We finished making your pizza!")

else: 
    print("Are you sure you want a plain pizza?")


requested_toppings = ['mushrooms', 'sausage', 'no cheese', 'pepporoni', 'olives']
available_toppings = ['mushrooms', 'sausage', 'no cheese', 'pepporoni', 'cheese', 'peppers', 'pineapple']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")




