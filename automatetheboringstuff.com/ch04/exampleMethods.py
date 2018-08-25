# Finding a value in a list with the "index()" method

greeings = ['hello', 'hi', 'howdy', 'heyas']
print(greeings.index('hello'))  # 0
print(greeings.index('heyas'))  # 3

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))  # 1, not return 3

animals = ['cat', 'dog', 'bat']

# Add value to lists with the "append()" and "insert()" method

animals.append('moose')
print(animals)    # ['cat', 'dog', 'bat', 'moose']

animals.insert(2, 'chicken')
print(animals)    # ['cat', 'dog', 'chicken', 'bat', 'moose']

# Removing values from lists with "remove()" and "del"

animals.remove('chicken')
print(animals)    # ['cat', 'dog', 'bat', 'moose']

animals.insert(3, 'cat')
animals.insert(5, 'cat')
print(animals)    # ['cat', 'dog', 'bat', 'cat', 'moose', 'cat']

animals.remove('cat')
print(animals)    # ['dog', 'bat', 'cat', 'moose', 'cat']

del animals[2]
print(animals)    # ['dog', 'bat', 'moose', 'cat']

# Sorting the values in a list with the "sort()" method

greeings.sort()
print(greeings)  # ['hello', 'heyas', 'hi', 'howdy']

number = [2, 5, 3.14, 1, -7]
number.sort()
print(number)    # [-7, 1, 2, 3.14, 5]

animals.insert(0, 'ant')
animals.append('badger')
animals.append('elephant')
print(animals)  # ['ant', 'dog', 'bat', 'moose', 'cat', 'badger', 'elephant']

animals.sort(reverse=True)
print(animals)  # ['moose', 'elephant', 'dog', 'cat', 'bat', 'badger', 'ant']

charSort = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
charSort.sort()
print(charSort)  # ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

alphabet = ['c', 'a', 'z', 'A', 'Z', 'B']
alphabet.sort(key=str.lower)
print(alphabet) # ['a', 'A', 'B', 'c', 'z', 'Z']
