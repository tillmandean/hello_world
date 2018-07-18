names = ['Tillman', 'William', 'Caroline', 'Susan', 'Gary']
print(names)

print(names[0] + " " + names[-1])

introduction = "Hello my name is " + names[0]

print(introduction)


guests = ['Juergen Klopp', 'Carlo Rovelli', 'Benny Lewis']
print(guests)

print(guests[-1] + " can't make it to the dinner.")
guests[-1] = 'Richard Feynman'
print(guests)

print("I have three more spots at the dinner")
guests.insert(0, 'Roberto Firmino')
guests.insert(2, 'Harry Houdini')
guests.append('Tyler the Creator')
print(guests)

print('\nActually I only have two spots')

popped_guest1 = guests.pop(0)
popped_guest2 = guests.pop(1)
popped_guest3= guests.pop(2)
popped_guest4 = guests.pop(2)

print('Sorry ' + popped_guest1 + ", "+ popped_guest2 + ", " 
	+ popped_guest3 + ", and "+ popped_guest4 + ", I don't have room.")


print(sorted(guests))
print(guests)


print(names)
names.sort()
print(names)

names.sort(reverse = True)
print(names)

cars = ['Maserati', 'Porsche', 'Aston Martin' , 'BMW' , 'Audi']
print(cars)
cars.reverse()
print(cars)

length = len(cars)
print(length)