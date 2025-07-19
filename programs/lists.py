#creating the list
car_brands=['Volkswagen', 'Kia', 'Toyota', 'BMW', 'Mercedes-benz', 'Audi', 'Porsche', 'Ferrari', 'Lamborghini', 'Rolls-Royce', 'Bentley']
print (car_brands[0].title())

#changing the list
car_brands[0]='Hyundai'#It will change [0], not add!!!
print (car_brands)

#adding to the list
car_brands.append('Genesis')
print (car_brands)

#inserting to the list
car_brands.insert(2, 'Skoda')
print (car_brands)

#removing from the list
del car_brands[0]
#if you don't know the position, but know value you can use
car_brands.remove('Kia')
print (car_brands)

#you can also use removed value later
too_expensive='Rolls-Royce'
car_brands.remove(too_expensive)
print(car_brands)
print (f'{too_expensive} is too expensive')

#pop fucntion
last_owned=car_brands.pop()
first_owned=car_brands.pop(0)
print(f'My last owned car was {last_owned.title()}, \n\tand my first owned car was {first_owned.title()}.')

#sorting list temporarily
print(sorted(car_brands))

#reversing list
car_brands.reverse()
print (car_brands)

#sorting list permanently
car_brands.sort(reverse=True)
print(car_brands)

#calculating how many values in list
print(len(car_brands))