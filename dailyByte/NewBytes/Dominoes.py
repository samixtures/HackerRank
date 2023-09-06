# You’re given a set of integers, dominoes, that represent 
# a set of domino tiles. The value of domino represents either 
# weight and its sign, positive or negative, represents the direction 
# it is falling: positive falls right and negative falls left. 
# When two dominoes collide, the larger domino destroys the smaller domino. 
# If two dominoes of the same size collide, both dominoes are destroyed. 
# After all the collisions, return the state of the dominoes.

# Ex: Given the following dominoes…

# dominoes = [3, -3], return [].
# Ex: Given the following dominoes…

# dominoes = [1, 2, -3, 2, -1], return [-3, 2] 
# (-3 destroys both dominoes to its left and the second two destroys the domino to the right of it).

def dominoes(s):
    positive = 0
    negative = 0
    ret = []
    for x in s:
        if x > 0:
            positive += x
        elif x < 0:
            negative -= x
        if positive > 0 and negative < 0:
            if (positive + negative) > 0:
                ret.append(positive)
            elif (positive + negative) < 0:
                ret.append(negative)
            positive = 0
            negative = 0
    print(ret)
dominoes([3, -3])
dominoes([1, 2, -3, 2, -1])