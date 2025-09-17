class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list) # mapping character count to each string

        for s in strs:
            count = [0] * 26 # a....z

            for c in s:
                count[ord(c)- ord("a")] +=1

            res[tuple(count)].append(s)

        return res.values()