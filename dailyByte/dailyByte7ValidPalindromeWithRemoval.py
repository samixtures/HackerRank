# This question is asked by Facebook. 
# Given a string and the ability to delete at most one character, 
# return whether or not it can form a palindrome.
# Note: a palindrome is a sequence of characters that reads the 
# same forwards and backwards.

# Ex: Given the following strings...

# "abcba", return true
# "foobof", return true (remove the first 'o', the second 'o', or 'b')
# "abccab", return false

#THOUGHTS:
#Check how many characters they have that are the same
#count that number and if its difference is <= 1 then
#baboom shabam katruuuung presto. We win

#Gotta proly create a frequency map
# Wait I'm actually dumb
# dumb dumb dumb dumb dumb

test = "foobof" #foboof
rev = test[::-1]
# i = 0
# temp = test[:i] + test[(1+i):]
# revTemp = temp[::-1]
# print("Temp is:", temp)
# print("revTemp is:", revTemp)

def vpwr(test):
    i = 0
    for x in test:
        if test == rev:
            return True
        temp = test[:i] + test[(1+i):]
        revTemp = temp[::-1]
        print("Temp is:", temp)
        print("revTemp is:", revTemp)
        if temp == revTemp:
            return True
        i+=1
    return False
print(vpwr(test))


    

#iterate and check each character of both words
#if the program finds one of the letters isn't the same
#then increment count and skip that letter in reversed word
#if count is <= 1 then return True, else False

# def VPWR(str):
#     temp = str[::-1] #reversed str is now temp
#     count = 0
#     i = 0 #word forwards
#     j = 0 #word backwards
#     for x in str:
#         if str[i] == temp[j]:
#             print(str[i], temp[j])
#             i+=1
#             j+=1
#         elif str[i] != temp[j]:
#             i += 1
#             count += 1
#     return count

# print(VPWR(test))