first_value = '  FIRST challenge       '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
first_value=first_value.strip()
second_value=second_value.replace('-  ','')
second_value=second_value.replace('  -','')
second_value=second_value.capitalize()
third_value=third_value.replace(' ','')
third_value=third_value.capitalize()
third_value=third_value.replace('-',' ')

print(f'{first_value:>22}')
print(second_value)
print(f'{third_value:>30}')

print(fourth_value,fifth_value,sixth_value, sep='#')

# Second challenge


# Third challenge

"""
print(f'.{first_value:>26}.')
print(f'.{second_value:<5}.')
print(f'.{third_value:<5}.')"""

# Fourth challenge - use only the print() function (no f-strings)


# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.