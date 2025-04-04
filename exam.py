# dictionaries

import pprint  # pretty print

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])  # fat
print('size' in myCat)  # True
print(list(myCat.keys()))  # ['size', 'color', 'disposition']
print(list(myCat.values()))  # ['fat', 'gray', 'loud']
print(list(myCat.items()))
# [('size', 'fat'), ('color', 'gray'), ('disposition', 'loud')]

for k, v in myCat.items():
    print(k, v)  # size fat color gray disposition loud


# character count
message = 'lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1
pprint.pprint(count)
