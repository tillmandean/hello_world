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

