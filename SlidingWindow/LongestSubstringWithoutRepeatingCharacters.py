#TimeComplexity: O(n)
#SpaceComplexity: O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashset = set() # creating the hashset
        maximum = 0 # creating the maximum with 0

        start = 0 # creating the start with 0
        for end in range(len(s)): # run until the length of s if s[end] not in hashset then add the end value to hashset
            if s[end] not in hashset:
                hashset.add(s[end])
                maximum = max(maximum,end-start+1) # setting the maximum value by comparing between maximum and end value

            else: # if end ch in hashset
                while s[start]!=s[end]: # run until the start is not equal to end then remove the start value in hashset
                    hashset.remove(s[start])
                    start+=1 # incrementing by 1
                start+=1 # incrementing by 1

        return maximum # returning the maximum value
