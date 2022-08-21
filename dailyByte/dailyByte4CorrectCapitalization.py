# This question is asked by Google. 
# Given a string, return whether or not it uses capitalization correctly. 
# A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, 
# or only the first letter is capitalized.

# Ex: Given the following strings...

# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true

#Hmm.. first of all we need to figure out how to check if a character is capitalized or not
#We can create a hashmap with all capital letter values and check if a value is in them,
#Memory: Creating the hashMap will be O(1) memory since it will only take 27 letters
#Time: We loop through the string and check if their values are in the hashmap. Looping through is 
#O(N) time and checking if it's in the hashMap should take O(1) time so should be O(N) time and O(N) memory
#ACTUALLY we use hashset here not hashmap


# Might be easier to figure out if it's falseeeeee


#VARIABLE
def func(test):
    m = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    #It's false if the first letter is lowercase and
    #there's an uppercase letter somewhere
    #heLlo
    counter = 0
    leng = len(test)
    if test[0] not in m:
        for x in test:
            if x in m:
                return False

    #It's false if first letter is upercase and
    # all other letters are capitalized except 1
    #SAmI or UsA or WASSuP
    #
    if test[0] in m:
        for x in test:
            if x in m:
                counter+=1
        if counter > 1 and counter != leng:
            return False

    #Otherwise it's True... right?
    return True

    

test = "USA" #true
test1 = "hIya" #false
test2 = "Calvin" #true
test3 = "compUter" #false
test4 = "coding" #true
print(func(test4))