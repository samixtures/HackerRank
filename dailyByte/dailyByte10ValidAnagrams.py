# This question is asked by Facebook. Given two strings s and t return whether or not s is an anagram of t.
# Note: An anagram is a word formed by reordering the letters of another word.

# Ex: Given the following strings...

# s = "cat", t = "tac", return true
# s = "listen", t = "silent", return true
# s = "program", t = "function", return false

#return True
s = "cat"
t = "tac"
#return True
s1 = "listen"
t1 = "silent"
#return False
s2 = "program"
t2 = "function"

def valid_anagram(s, t):
    s_map = {}
    t_map = {}
    print(f"The words are {s} and {t}")
    for x in s:
        if x in s_map:
            s_map[x] += 1
        else:
            s_map[x] = 0
    for x in t:
        if x in t_map:
            t_map[x] += 1
        else:
            t_map[x] = 0
    # print("s_map:",s_map)
    # print("t_map:",t_map)
    if s_map == t_map:
        return True
    else:
        return False

print(valid_anagram(s1,t1))