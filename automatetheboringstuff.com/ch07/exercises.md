1. Use `re.compiler()` creates _Regex_ objects.
2. Raw strings are used so that backslashes do not have to be escaped.
3. The _search()_ method returns _Match_ objects.
4. The _group()_ method returns strings of the matched text.
5. (\d\d\d) is group 1, (\d\d\d-\d\d\d\d) is group 2, and (\d\d\d)-(\d\d\d-\d\d\d\d) is group 0.
6. Periods and parentheses can be escaped with a backslash: `\., \(, and \).`
7. If the regex has no groups, a list of strings is returned. If the regex has groups, a list of tuples of strings is returned.
8. `The |` character signifies matching “either, or” between two groups.
9. `The ?` character matches zero or one of the preceding group.
10. `The +` matches one or more and `the *` matches zero or more.
11. The {3} matches exactly three instances of the preceding group. The {3,5} matches between three and five instances.
12. The `\d, \w, and \s` shorthand character classes match a single digit, word, or space character.
13. The `\D, \W, and \S` shorthand character classes match a single character that is not a digit, word, or space character.
14. Passing `re.I` or `re.IGNORECASE` as the second argument to _re.compile()_ will make the matching case insensitive. 
15. `The .` matches any character except the newline character. If _re.DOTALL_ is passed as the second argument to re.compile(), then the dot will also match newline characters.
16. The `.*` performs a greedy match, and the `.*?` performs a nongreedy match.
17. `[a-z0-9]`
18. `X drummers, X pipers, five rings, X hens`
19. The _re.VERBOSE _argument allows you to add whitespace and comments to the string passed to re.compile().
20. `re.compile(r'^\d{1,3}(,\d{3})*$')`
21. `re.compile(r'[A-Z][a-z]*\sNakamoto')`
22. `re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)`
