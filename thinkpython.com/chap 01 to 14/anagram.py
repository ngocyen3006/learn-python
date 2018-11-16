def is_anagram(word1, word2):
    '''Checks whether two words are anagrams
    word1: string or list
    word2: string or list
    returns: boolean
    '''
    return sorted(word1) == sorted(word2)


print(is_anagram("silent", "listen"))
print(is_anagram("strong", "power"))
