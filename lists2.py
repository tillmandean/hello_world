footballers = ['marco reus', 'roberto firmino', 'naby keita', 'christian pulisic', 'andy robertson']

for footballer in footballers:
	print(footballer.title() + ' is an incredible footballer.')

print('\n' + 'Up the mighty Reds and Heja BVB!' + '\n')

#slicing a list
print(footballers[1:4])
print(footballers[:4])
print(footballers[2:])

for footballer in footballers[:2]:
	print(footballer.title())


for value in range(1,6):
	print(value)


numbers = list(range(1, 11))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)

digits = [1, 202, 1002, 34, 66, -25]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension
squares_taketwo = [value**2 for value in range(1,11)]
print(squares_taketwo)

#copying lists; if you set directly equal, they point to the same point in memory and are the same list.
my_foods = ['spaghetti', 'brisket tacos', 'steak', 'lasagna']
williams_foods = my_foods[:]

print(my_foods)
print(williams_foods)

#tuples: immutable lists; use parantheses
dimensions = (200,50)
for item in dimensions:
	print(item)




