
# Today's Byte

# Welcome to your first of many daily bytes! We are starting with a strings problem and we strongly recommend you find the time each day to solve these problems. It is important to not just solve them in your head but actually whip out your favorite editor/IDE and write a function and use the test cases supplied in the question to check your work. Getting yourself to actually write down the solutions will go a long way to ensuring you are thinking through all the edge cases as well as any space/time complexities.

# This question is asked by Google. Given a string, reverse all of its characters and return the resulting string.

# Ex: Given the following strings...

# “Cat”, return “taC”
# “The Daily Byte”, return "etyB yliaD ehT”
# “civic”, return “civic”

str = "The Daily Byte"

def reverseStr(str):
    length = len(str)-1
    rev = ""
    counter = 0

    while length >= 0:
        rev += str[length]
        length -= 1
    return rev

print(reverseStr(str))