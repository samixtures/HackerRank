# This question is asked by Apple. Given two binary strings 
# (strings containing only 1s and 0s) return their sum 
# (also as a binary string).
# Note: neither binary string will contain leading 0s unless the string itself is 0

# Ex: Given the following binary strings...

# "100" + "1", return "101"
# "11" + "1", return "100"
# "1" + "0", return  "1"


#RULES:
"""
  0 
+ 0
_____
  0

  1
+ 1
  1
_____
 11
"""

# 100 + 1 

# should we just convert do decimal, add it, then convert back to binary?
# or we could do something like %10, add that with the added value, and if it's
# greater than 1 then we make the new string's first binary value 0, and continue 
# or something like that 

#  100
# +  1
# ______


# 100 % 10 = 0
# 1 % 10 = 1
# 0 + 1 = 1
