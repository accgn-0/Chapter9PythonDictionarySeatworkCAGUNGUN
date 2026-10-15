print('===== Record Keeping App =====')
print('a. Add Data')
print('b. Delete Data')
print('c. End')

inputs = input('Select a letter from the list: ')
try:
    if inputs == 'a':
        print('Select action: ', inputs)
        for input in inputs:
            name = input('Enter a key: ')
            print('name')
            value = input('Enter value: ')
            print('value')
except:
    if input == 'c':
        print('Thank You. Program will now End')
        exit()
    exit()

print('===== Key does not exist =====')
