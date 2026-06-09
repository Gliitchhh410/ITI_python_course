userInput = input('Enter a string: ')
letters = 0
numbers = 0
for char in (userInput):
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        numbers += 1

print(f'Letters Count: {letters} \n Digits Count: {numbers}')