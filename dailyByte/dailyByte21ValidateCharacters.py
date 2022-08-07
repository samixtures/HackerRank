# This question is asked by Google. Given a string only containing the 
# following characters (, ), {, }, [, and ] return whether or not the 
# opening and closing characters are in a valid order.

# Ex: Given the following strings...

# "(){}[]", return true
# "(({[]}))", return true
# "{(})", return false

s = "(){}[]"
s1 = "(({[]}))"
s2 = "{(})"

def validate_characters(s):
    h = {'(':')', '{':'}', '[':']'}
    l = []
    for i in s:
        print("i is ", i)
        if i == '(' or i == '{' or i == '[':
            l.append(i)
        if len(l) > 0:
            if l[-1] in h:
                if h[l[-1]] == i:
                    print(h[l[-1]])
                    l.pop(-1)
            # if i == ')' or i == '}' or i == ']':
            #     l.pop(-1)
    print("List is ", l)
    if not l:
        return True
    return False
print(validate_characters(s))