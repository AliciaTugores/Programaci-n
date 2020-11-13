#What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
#Write a function that will find all the anagrams of a word from a list. You will be given two inputs 
#a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. 
def anagrams (word, words):
    anagrams = []
    for anagram in words:
        if sorted(anagram) == sorted(word):
            anagrams.append(anagram)
    return anagrams