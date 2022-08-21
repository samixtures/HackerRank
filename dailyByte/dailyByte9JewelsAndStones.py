# This question is asked by Amazon. 
# Given a string representing your stones and another string 
# representing a list of jewels, return the number of stones that 
# you have that are also jewels.

# Ex: Given the following jewels and stones...

# jewels = "abc", stones = "ac", return 2
# jewels = "Af", stones = "AaaddfFf", return 3
# jewels = "AYOPD", stones = "ayopd", return 0

#So we need to count how many of each letter in the jewels list are in the stones list

#Let's create a frequency map 


j= "Af"
s = "AaaddfFf"
j1 = "abc"
s1 = "ac"
j2 = "AYOPD"
s2 = "ayopd"
#we should return 3 cuz fs and 1 A

def jAndS(j, s):
    freq = {}
    sum = 0
    for x in j:
        freq[x] = 0
    for x in s:
        if x in freq:
            freq[x] += 1
            sum += 1
    return sum
print(jAndS(j, s))