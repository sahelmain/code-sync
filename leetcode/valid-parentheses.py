class Solution(object):
    def isValid(self, s):
        bracketMap = {")":"(", "}":'{', ']':'['}
        for char in s:
            if char in bracketMap:
                stack.append(char)
            elif