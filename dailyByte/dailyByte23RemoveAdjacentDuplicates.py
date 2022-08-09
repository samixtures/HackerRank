# This question is asked by Facebook. 
# Given a string s containing only lowercase letters, continuously 
# remove adjacent characters that are the same and return the result.

# Ex: Given the following strings...

# s = "abccba", return ""
# s = "foobar", return "fbar"
# s = "abccbefggfe", return "a"

s, s1, s2 = "abccba", "foobar", "abccbefggfe"

def remove_adjacent_duplicates(s):
    l = []
    count = 0
    for x in s:
        l.append(x)
    for i, x in enumerate(l):
        if i < len(l)-1:
            if l[i] == l[i+1]:
                while l[i+1] == l[i]:
                    l.pop(i+1)
                    print(i)
                    print(l)
                    count += 1
                l.pop(i)
        if i > 0:
            if l[i] == l[i-1]:
                while l[i-1] == l[i]:
                    l.pop(i-1)
                l.pop(i)
    print(l)
remove_adjacent_duplicates(s)