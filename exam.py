# list

# flexible list
spam = [10, 20, 30]
print(spam[1:3])
spam[1:3] = [40, 50, 60]
print(spam)

#list methods
spam = [1, 2, 3, 4]
print(spam.index(2))  # returns 1

spam.append(5)
print(spam)  # returns [1, 2, 3, 4, 5]

spam.insert(0, 0)
print(spam)  # returns [0, 1, 2, 3, 4, 5]

spam.remove(5) # removes the first occurrence of 5 (not index 5 )
print(spam)  # returns [0, 1, 2, 3, 4]

del spam[0] # deletes the first element (index 0)
print(spam)  # returns [1, 2, 3, 4]

spam = [2, 5, 3, 14, -8, 0]
spam.sort() # sorts the list in ascending order
print(spam)  # returns [-8, 0, 2, 3, 5, 14]

spam.sort(reverse=True) # sorts the list in descending order
print(spam)  # returns [14, 5, 3, 2, 0, -8]

# The list is passed by reference, so the original list is modified.
def eggs(cheese:list):
    cheese.append('hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)  # returns [1, 2, 3, 'hello']

