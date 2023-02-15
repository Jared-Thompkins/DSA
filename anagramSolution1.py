"""
A good example problem for showing algorithms with different orders of magnitude is the classic anagram
detection problem
for strings. One string is an anagram of another if the second is simply a rearrangement of the first. For example,
'heart' and 'earth' are anagrams. The strings 'python' and 'typhon' are anagrams as well. For the sake of simplicity,
we will assume that the two strings in question are of equal length and that they are made up of symbols from the set of
26 lowercase alphabetic characters. Our goal is to write a boolean function that will take two strings and return
whether they are anagrams."""


def anagramSolution(s1, s2):
    n = len(s1)
    s2_list = list(s2)

    for c1 in s1:
        for i in range(len(s2_list)):
            if c1 == s2_list[i]:
                s2_list[i] = None
                n -= 1
                break

    return n == 0


# O(n^2)
