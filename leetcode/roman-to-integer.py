class Solution(object):
    def romanToInt(self, s):
        romanNum = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        sum = 0
        n = len(s)
        for i in range(n-1):
            currentValue = romanNum[s[i]]
            nextValue = romanNum[s[i+1]]
            if currentValue < nextValue:
                sum= sum - currentValue
            else:
                sum = sum + currentValue
        sum = sum + romanNum[s[n-1]]
        return sum