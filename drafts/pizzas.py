pizzas=['pepperoni', 'margarita', 'pineapple one']
friend_pizzas=pizzas[:]
pizzas.append('Hawai')
friend_pizzas.append('Bayern')
for friends_pizza in friend_pizzas:
    print(f"My friend's favorite pizza is: {friends_pizza.title()}")
print ("\nAnd my favorite pizza's are: ")
for pizza in pizzas:
    print(f'My favorite pizza is: {pizza.title()}')
print('\nWe really love pizza!')