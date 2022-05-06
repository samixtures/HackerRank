class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # .lower()
        # if ! alnum then don't use it
        final = ""
        for x in s:
            if x.isalnum():
                final += x.lower()
        print(final)
        return final == final[::-1]
        # 