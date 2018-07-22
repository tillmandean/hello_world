def greet_user(username):
    """Displays a simple greeting"""
    print("Hello " + username.title() + ", it's nice to see you!"
             + "\nWhat can I help you with today? ")

user = input("What is your name? ")
greet_user(user)
task = input()
print("Let me see what I can do...")


def footballer(name, position, nationality):
    print(name.title() + " is a " + nationality.title() + " " + position.upper() + ".")

name_footballer = input("What is the footballer's name? ")
position_footballer = input("What is the footballer's position? ")
nationality_footballer = input("What is the footballer's nationality? ")
#positional call
footballer(name_footballer, position_footballer, nationality_footballer)
#keyword call
footballer(name='marco reus', position='am', nationality='german')


#default values can be set
def languages_i_am_learning (coding_lang='python', lang='french'):
    print("I'm learning " + coding_lang.title() + " and " + lang.title() + ".")

languages_i_am_learning()
languages_i_am_learning(coding_lang='java', lang='german')


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

manager = get_formatted_name('lucien', 'favre')
print(manager)


def get_formatted_name(first_name, last_name, age=''):
    """Returns a dictionary of information about a person."""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

manager = get_formatted_name('lucien', 'favre', age=60)
print(manager)

def greet_family(names):
    """Print a simple greeting to each family member in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

family = ['tillman', 'caroline', 'william', 'gary', 'susan']
greet_family(family)

#arbitrary number of arguments can be collected in a tuple with an asterisk
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza witht the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('mushrooms', 'sausage', 'olives', 'pepperoni', 'no cheese')


#dictionary to contain an arbitrary number of key-value pairs can be created with a double asterisk
def build_profile(first, last, **userinfo):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in userinfo.items():
        profile[key] = value
    return profile

user_profile = build_profile('tillman', 'dean',
                             location='nashville', 
                             hair_color='brown', 
                             eye_color='brown',
                             age='17')
print(user_profile)

