human_0 = {'age' : '17', 'height' : '5 foot 10', 'hair color' : 'brown'}
print(human_0['age'])
print(human_0)

human_0['eye color'] = 'brown'
print(human_0)

del human_0['hair color']
print(human_0)

favorite_footballteam = {
    'tillman' : 'liverpool',
    'wiliam' : 'ajax',
    'dad' : 'usa',
    'henry' : 'liverpool',
    }
print(favorite_footballteam)

for key, value in favorite_footballteam.items():
    print("\nKey: " + key.title())
    print("Value: " + value.title())

for name in favorite_footballteam.keys():
    print("\n" + name.title())

for name in sorted(favorite_footballteam.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("\nThe following football teams mentioned are: ")
for value in favorite_footballteam.values():
    print(value.title())

print("\nThe following football teams with repeats excluded mentioned are: ")
for value in set(favorite_footballteam.values()):
    print(value.title())


human_1 = {'age' : '19', 'height' : '5 foot 11', 'hair color' : 'brown'}
human_2 = {'age' : '12', 'height' : '5 foot 4', 'hair color' : 'brown'}
humans = [human_0, human_1, human_2]
for human in humans:
    print(human)

pizza = {
    'crust' : 'original',
    'toppings' : ['mushrooms', 'sausage', 'olives', 'pepperoni', 'no cheese'],
    }
print("You ordered a " + pizza['crust'] + "-crust pizza with:")
for topping in pizza['toppings']:
    print("\t" + topping)



