# This question is asked by Amazon. Given two strings representing sentences, 
# return the words that are not common to both strings 
# (i.e. the words that only appear in one of the sentences). 
# You may assume that each sentence is a sequence of words (without punctuation) 
# correctly separated using space characters.

# Ex: given the following strings...

# sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
# sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
# sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]

s1, s2 = "the quick", "brown fox" # ["the", "quick", "brown", "fox"]
s3, s4 = "the tortoise beat the haire", "the tortoise lost to the haire" # return ["beat", "to", "lost"]
s5, s6 = "copper coffee pot", "hot coffee pot" # return ["copper", "hot"]

res = []
temp = ""
for i, x in enumerate(s1):
    if x == " ":
        res.append(temp)
        temp = ""
    if i == len(s1)-1:
        temp += x
        res.append(temp)
        temp = ""
    else:
        temp += x
print(res)