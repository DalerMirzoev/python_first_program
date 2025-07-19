'''
name=input("What's your name? ")
lastname=input("What's your last name? ")
age=input('How old are you? ')
corname=name.strip()
corlname=lastname.strip()
corage=age.strip()
age=corage
#f strings or format strings help to shorten your final print function's argument
print(f'your name is:\n\t{corname.title()},\nyour last name is\n\t{corlname.title()},\nand you are \n\t{age} years old.')
'''

#simplified version of the same code
name=input("What's your name? ")
lastname=input("What's your last name? ")
age=input('How old are you? ')
name=name.strip().title()
lastname=lastname.strip().title()
age=age.strip()
print(f'your name is:\n\t{name},\nyour last name is:\n\t{lastname},\nand you are {age} years old.')