#buffet
foods=('pasta', 'soup', 'meatballs', 'fish', 'burger')
print ("Here's our old menu:")
for food in foods:
    print(food)
new_foods=['pasta', 'soup', 'meatballs', 'fish', 'burger']
new_foods.append('steak')
new_foods.append('plov')

print ('\nOur new menu consists of:')
for new_food in new_foods:
    print(new_food)