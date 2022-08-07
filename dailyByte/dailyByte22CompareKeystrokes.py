# This question is asked by Amazon. 
# Given two strings s and t, which represents a sequence of 
# keystrokes, where # denotes a backspace, return whether 
# or not the sequences produce the same result.

# Ex: Given the following strings...

# s = "ABC#", t = "CD##AB", return true
# s = "como#pur#ter", t = "computer", return true
# s = "cof#dim#ng", t = "code", return false
s, t = "ABC#", "CD##AB"
s1, t1 = "como#pur#ter", "computer"
s2, t2 = "cof#dim#ng", "code"
def compare_keystrokes(s, t):
    s_list = []
    t_list = []
    for i in s:
        if i!="#":
            s_list.append(i)
        elif i == "#":
            s_list.pop(-1)
    for i in t:
        if i!="#":
            t_list.append(i)
        elif i == "#":
            t_list.pop(-1)
    print("s is", s_list)
    print("t is", t_list)
    if s_list == t_list:
        return True
    return False
# print(compare_keystrokes(s,t))
# print(compare_keystrokes(s1,t1))
# print(compare_keystrokes(s2,t2))
compare_keystrokes(s,t)
compare_keystrokes(s1,t1)
compare_keystrokes(s2,t2)