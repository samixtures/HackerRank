import file_two
print("File one __name__ is set to: {}" .format(__name__))

s = "hello"
#    01234
print("s[-5] is",s[-5])
print("slicing S bois", s[len(s):-5:-1])

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

#len = 5 
#-len = -5 -> -5 -1 = -6
#start at 5 and go to 4, 3, 2, 1, 0, 5?
#looks like if I put a value of len(s)-1 or
#greater for the start it, it starts at the
#last index regardless

#I'm not understanding why -6 for the stop
#works the way it does.

#If step is pos: default start
#and end are 0:len

#If step is neg: default start and
#end are len and -len-1
# start:stop:step

arr = [5, 3, 9, 6]
i = len(arr)-1
for e, x in enumerate(arr[::-1]):
    print(arr[e-4])

# 2 3 4 5 6 7 8 9 10 10
# 2 3 4 5 6 7 8 9 9 10
# 2 3 4 5 6 7 8 8 9 10
# 2 3 4 5 6 7 7 8 9 10
# 2 3 4 5 6 6 7 8 9 10
# 2 3 4 5 5 6 7 8 9 10
# 2 3 4 4 5 6 7 8 9 10
# 2 3 3 4 5 6 7 8 9 10
# 2 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 9 10

# 2 3 4 5 6 7 8 9 10 10 
# 2 3 4 5 6 7 8 9 9 10 
# 2 3 4 5 6 7 8 8 9 10 
# 2 3 4 5 6 7 7 8 9 10 
# 2 3 4 5 6 6 7 8 9 10 
# 2 3 4 5 5 6 7 8 9 10 
# 2 3 4 4 5 6 7 8 9 10 
# 2 3 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 10