class Solution(object):
    def isPalindrome(self, s):
        s2 = ""
        for i in range(len(s)):
            if s[i].isalnum():
                s2+=s[i].lower()
        return s2==s2[::-1]