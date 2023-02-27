# This question is asked by Google. 
# You are given a bag of coins, an initial energy of E, 
# and want to maximize your number of points (which starts at zero). 
# To gain a single point you can exchange coins[i] amount of energy 
# (i.e. if I have 100 energy and a coin that has a value 50 I can exchange 
# 50 energy to gain a point). If you do not have enough energy you can give away 
# a point in exchange for an increase in energy by coins[i] amount 
# (i.e. you give away a point and your energy is increased by the value of that coin: 
# energy += coins[i]). Return the maximum number of points you can gain.
# Note: Each coin may only be used once.

# Ex: Given the following coins and starting energy…

# coins = [100, 150, 200] and E = 150, return 1
# coins = [100,200,300,400] and E = 200, return 2
# coins = [300] and E = 200, return 0

coins1, e1 = [100, 150, 200], 150 # return 1
coins2, e2 = [100, 200, 300, 400], 200 # return 2
coins3, e3 = [300], 200 # return 3

"""
I'm not understanding why we would exchange a point for coins since we're trying to maximize points.

Solution:
coins list is ascending, so loop through and see how many times you can use your energy to buy
coins[0] and do e-=coins[0] accordingly until you can't buy coins[0] anymore.
"""

def solution(coins, e):
    ret = 0
    if coins[0]:
        while e >= coins[0]:
            e -= coins[0]
            ret += 1
    return ret
print(solution(coins1, e1))
print(solution(coins2, e2))
print(solution(coins3, e3))