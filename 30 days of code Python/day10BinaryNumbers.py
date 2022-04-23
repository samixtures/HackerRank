#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    list = []
    while n > 0:
        remainder = n%2
        list.append(remainder)
        n = int(n/2)
    # print(list)
    counter = 0
    max_counter = 0
    for x in list:
        if x == 1:
            counter+=1
        elif x == 0:
            counter = 0
        if counter > max_counter:
                max_counter = counter
    print(max_counter)
        

# another way I redid it (redid.. is that a word?)

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
#     n = int(input().strip())

#     counter = 0
#     max = 0
#     temp = 0
#     x = n # 6
#     while x>0: # 1
#         temp = int(x%2) # 1
#         # print("temp is, ", temp)
#         if temp == 1:
#             counter+=1
#         elif temp == 0:
#             counter=0
#         if counter > max:
#             max = counter # 1
#         x = int(x/2) # 1
#     print(max)