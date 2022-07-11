# This question is asked by Microsoft. 
# Given an array of strings, return the longest common prefix that is shared amongst all strings.
# Note: you may assume all strings only contain lowercase alphabetical characters.

# Ex: Given the following arrays...

# ["colorado", "color", "cold"], return "col"
# ["a", "b", "c"], return ""
# ["spot", "spotty", "spotted"], return "spot"
test =  ["colorado", "color", "cold"] #return col
print(len(test[0])-1)
i = 1
f = test[0]
same = True
pref = ""
while i < len(test):
    j = 0
    k = 0
    same = True
    while same:
        # if j >= len(test[i]) or j >= len(test[i-1]):
        #     break
        if test[i][j] == test[i-1][j] and j < len(test[i])-1:
            print(test[i][j])
            # print(j)
            pref += test[i][j]
            j+=1
        else:
            same = False
    i+=1
print(pref)
# def lcp(str):

# res = ""
# charIn = True
# first = str[1]
# if str1
# for x in str:
#     if x == first:
#         continue
#     for y in x:
#         if y == 

# for x in str:
#     if x == first:
#         continue
#     for y in range(len(str[x])-1):
#         if 
