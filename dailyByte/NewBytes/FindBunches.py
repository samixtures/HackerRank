# Given a string S that contains only lowercase letters, return a list containing the intervals of all the bunches. A bunch is a set of contiguous characters (larger than two) that are all the same. An interval that represents a bunch contains the starting index of the bunch and the ending index of the bunch.
# Note: The intervals returned should be in ascending order according to start indexes.
# Ex: Given the following string S...

# S = “aaabbbccc”, return [[0,2],[3,5],[6,8]].
# Ex: Given the following string S...

# S = “aaabbcddddd”, return [[0,2],[6,10]].

# Bunches are > 2 consecutive same characters

def bunches(s):
    ret = []
    start, end = 0, 1
    numberOfBunch = 1
    for i in range(0, len(s)):
        if end < len(s):
            if s[start] == s[end]:
                numberOfBunch += 1
                end += 1
            if end < len(s):      
                if s[start] != s[end]:
                    if numberOfBunch > 2:
                        ret.append([start, end-1])
                    start = end
                    end = end+1
                    numberOfBunch = 1
            else:
                if s[start] != s[end-1]:
                    if numberOfBunch > 2:
                        ret.append([start, end-1])
                    start = end
                    end = end+1
                    numberOfBunch = 1
    print(ret)

s1 = "aaabbbccc"
s2 = "aaabbcddddd"
s3 = "a"
bunches(s1)