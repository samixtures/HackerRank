# This question is asked by Google. 
# Create a class CallCounter that tracks the number of calls a 
# client has made within the last 3 seconds. Your class should contain one method, ping(int t) that 
# receives the current timestamp (in milliseconds) of a new call being made and returns the number 
# of calls made within the last 3 seconds.
# Note: you may assume that the time associated with each subsequent 
# call to ping is strictly increasing.

# Ex: Given the following calls to ping…

# ping(1), return 1 (1 call within the last 3 seconds)
# ping(300), return 2 (2 calls within the last 3 seconds)
# ping(3000), return 3 (3 calls within the last 3 seconds)
# ping(3002), return 3 (3 calls within the last 3 seconds)
# ping(7000), return 1 (1 call within the last 3 seconds)

class CallCounter:
    def __init__(self):
        self.q = []
    def ping(self, t): #timestamp in miliseconds
        self.q.append(t)
        while t - self.q[0] >= 3000:
            self.q.pop(0)
        # if self.q:
        #     while (3000 - self.q[-1]) <= 0:
        #         self.q.pop(-1)
        # self.q.append(t)
        return len(self.q)
q = CallCounter()
print(q.ping(1))
print(q.ping(300))
print(q.ping(3000))
print(q.ping(3002))
print(q.ping(7000))
# print(q.ping(1))