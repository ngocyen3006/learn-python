from runtimeFunction import timed


@timed
def make_word_list1():
    '''Reads lines from a file and builds a list using append.'''
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


@timed
def make_word_list2():
    '''Reads lines from a file and builds a list using list +.'''
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


t1 = make_word_list1()
print(len(t1))
print(t1[:10])

t2 = make_word_list2()
print(len(t2))
print(t2[:10])
