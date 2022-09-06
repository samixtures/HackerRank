# This question is asked by Microsoft. 
# Given an array of strings, return the longest common prefix that is shared amongst all strings.
# Note: you may assume all strings only contain lowercase alphabetical characters.

# Ex: Given the following arrays...

# ["colorado", "color", "cold"], return "col"
# ["a", "b", "c"], return ""
# ["spot", "spotty", "spotted"], return "spot"

s = ["colorado", "color", "cold"]
s1 = ["a", "b", "c"]
s2 = ["spot", "spotty", "spotted"]

def LCP(s):
    l = []
    i = 0
    same = True
    first = s[0]
    #        01234567
    second = s[1]
    #         01234
    third = s[2]
    result = []
    while i < min(len(first), len(second)) and first[i] == second[i]:
        # print(first[i])
        l.append(first[i])
        i = i + 1
    i = 0
    while i < min(len(l), len(third)) and l[i] == third[i]:
        result.append(third[i])
        i = i + 1
    return(''.join(result))
print(LCP(s2))
    
