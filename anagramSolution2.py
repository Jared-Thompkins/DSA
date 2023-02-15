"""
A good example problem for showing algorithms with different orders of magnitude is the classic anagram
detection problem
for strings. One string is an anagram of another if the second is simply a rearrangement of the first. For example,
'heart' and 'earth' are anagrams. The strings 'python' and 'typhon' are anagrams as well. For the sake of simplicity,
we will assume that the two strings in question are of equal length and that they are made up of symbols from the set of
26 lowercase alphabetic characters. Our goal is to write a boolean function that will take two strings and return
whether they are anagrams."""


def anagramSolution2(s1, s2):
    n = len(s1)
    if n != len(s2):
        return False

    list1 = list(s1)
    list2 = list(s2)

    for i in range(n):
        if list1[i] != list2[i]:
            return False
    return True
