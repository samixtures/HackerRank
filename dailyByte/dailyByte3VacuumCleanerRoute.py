# This question is asked by Amazon. 
# Given a string representing the sequence of moves a robot vacuum makes, 
# return whether or not it will return to its original position. 
# The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

# Ex: Given the following strings...

# "LR", return true
# "URURD", return false
# "RUULLDRD", return true
#
#HMM check if Rs and Ls are the same, and if Us and Ds are the same
test = "LR"
test2 = "URURD"
test3 = "RUULLDRD"

ls, rs, us, ds = 0, 0, 0, 0

for x in test:
    if x == "L":
        ls += 1
    elif x == "R":
        rs += 1
    elif x == "U":
        us += 1
    elif x == "D":
        ds += 1
    
if ls == rs and us == ds:
    print("True")
else:
    print("False")