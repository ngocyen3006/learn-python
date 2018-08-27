# The setdefault() method

spam = {'name': 'Pooka', 'age': 5}
exp = spam.copy()

if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

print("-----------------------")

exp.setdefault('color', 'black')
print(exp)

print("-----------------------")

exp.setdefault('color', 'white')
print(exp)
