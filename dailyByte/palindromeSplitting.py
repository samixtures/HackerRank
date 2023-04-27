# This question is asked by Google. 
# Given a string s, return all possible partitions of 
# s such that each substring is a palindrome.

# Ex: Given the following string s…

# s = "abcba",
# return [
#     ["a","b","c","b","a"],
#     ["a","bcb","a"],
#     ["abcba"]
# ]

test = "abcba" # returns [["a","b","c","b","a"], ["a","bcb","a"], ["abcba"]]

def solution(s):
    """
    This is quite interesting. Take a string, split it into elements in a newly made list
    and those elements must be a palindrome.

    Let's first create a function that checks if a list is a palindrome yea?
    
    And let's create some test cases.
    """
    palTest1 = "tacocat" # True
    palTest2 = "robert" # False
    palTest3 = "Flamingo" # False
    palTest4 = "racecar" # True

    palTest1 = [x for x in palTest1]
    palTest2 = [x for x in palTest2]
    palTest3 = [x for x in palTest3]
    palTest4 = [x for x in palTest4]
    # We need to convert the test strings to lists where each character is an element in the string
    # to do that we can use list comprehension I think, butI kind of forgot how that works


    def isPalindrome(str):
        l, r = 0, len(str)-1
        