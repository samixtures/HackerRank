# This question is asked by Google. Given two strings s and t, return 
# the minimum number of operations needed 
# to convert s into t where a single operation 
# consists of inserting a character, deleting a 
# character, or replacing a character.

# Ex: Given the following strings s and t…

# s = "cat", t = "bat", return 1.

# Ex: Given the following strings s and t…

# s = "beach", t = "batch", return 2.
# Delete the 'e' in "beach" and add a 't' to the resulting "bach".

s1, t1 = "cat", "bat"
s2, t2 = "batch", "beach"

"""
teeth
teeths
logically add a letter at the end but the program needs to know all of the letters
beforehand are the exact same...

flamingo
dinosaur
when they're the same amount of setters i think you can replace them all

bob
dinosaur
to get from bob to dinosaur we we can replace the first three letters and then
add letters until they're the same

blob
bob
hmmmm how does we do dees? if they're the same then keep going, until something is different
in the top one then remove it, but that can be problematic if we have something else huh

blorb
bob
same, different: remove l, same, different: remove r, same hmmm that still works

bankai
bank
same, same, same, same, different? nah that would be out of index error
hmm maybe we see which has less characters then no non on ono
hmmm if they're all the same except last two then we keep it all and delete the end obviously
but I feel like there are examples where this messes everything up hmm

"""