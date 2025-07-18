'''
x = float(input('What is X? '))
y = float(input('What is Y? '))

z = round(x+y) #it will round the answer to the closest integer

#now I will use :, to separate each 3 numbers with ,
print(f'{z:,}')
'''

x = float(input('What is X? '))
y = float(input('What is Y? '))

z = round(x/y, 2) #we can decide to which number whe round
#we can get the exact same result by print(f'{z:.2f}')

print(z)