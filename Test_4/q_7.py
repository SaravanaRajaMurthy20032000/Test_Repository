# Write a program "list_anagrams.py" to find anagrams in a given list of words. 
# Two words are called anagrams if one word can be formed by rearranging letters of another. 
# For example 'eat', 'ate' and 'tea' are anagrams.
# Assume the list given is ['eat', 'ate', 'done', 'tea', 'soup', 'node'] 
# then it should return [['eat','ate','tea], ['done','node'], ['soup']]

def list_anagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    result = []
    for key in anagrams:
        result.append(anagrams[key])
    return result

words = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
anagram_lists = list_anagrams(words)
print(anagram_lists)
