1. `True` and `False` are two values of Boolean data type.
2. `and`, `or`, and `not` are the three Boolean operators.
3.

| Expression      | Value |
| --------------- | ----- |
| True or True    | True  |
| True or False   | True  |
| False or False  | False |
| True and True   | True  |
| True and False  | False |
| False and False | False |
| not True        | False |
| not False       | True  |

4.

```python
(5 > 4) and (3 == 5) # False
not (5> 4) # False
(5 > 4) or (3 == 5) # True
not ((5 > 4) or (3 == 5)) # False
(True and True) and (True == False) # False
(not False) or (not True) # True
```

5. Six comparison operators are `<, >, <=, >=, ==, !=`

6. `=` can be used to assign value to variable, `==` is used to compare two values.

7. A condition is an expression return either `True` or `False`. And we can use it in order to compare.

8. 

```python
spam = 0    #1
if spam == 10:  #2
    print('eggs')   #3
    if spam > 5:    #4
        print('bacon')  #5
    else:   #6
        print('ham')    #7
    print('spam')   #8
print('spam')   #9
```

One block from #2 to # 8

Second block from #4 to #5

Third block from #6 to #7

9. 

```python
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greeting!")
```

10. What can you press if your program is stuck in an infinite loop?
    `Ctrl + C`

11. `break` is used to stop a loop, and `continue` is used to immediately jumps back to the start of the loop and reevaluates the loop’s condition.

12. `range(10)`,`range(0, 10)`, `range(0, 10, 1)` both are from 0 to 9 with step = 1

13. 

```python
for i in range(1, 11):
    print(i)
```

```python
i = 1
while i < 11:
    print(i)
    i = i + 1
```

14. 

`spam.bacon()`
