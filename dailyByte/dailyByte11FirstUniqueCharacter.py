# This question is asked by Microsoft. 
# Given a string, return the index of its first unique character. 
# If a unique character does not exist, return -1.

# Ex: Given the following strings...

# "abcabd", return 2
# "thedailybyte", return 1
# "developer", return 0

test = "abcabd"
test1 = "thedailybyte"
test2 = "developer"
def first_unique_char(test):
    h = {}
    for x in test:
        if x in h:
            h[x] += 1
        else:
            h[x] = 0
    for i, x in enumerate(test):
        if h[x] == 0:
            print(x)
            return i
    return -1
print(first_unique_char(test))