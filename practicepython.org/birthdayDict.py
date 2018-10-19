# http://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

birthdays = {"May": "May 01",
             "June": "June 30",
             "August": "August 14",
             "September": "Sep 29"}

print("Welcome to the birthday dictionary. I know the birthdays of:")
print("\n".join(birthdays.keys()))
print("Who's birthday do you want to look up?")
name = input()
if name not in birthdays.keys():
    print("I do not have birthday information for {}.".format(name))
else:
    print("{}\'s birthday is {}.".format(name, birthdays[name]))
