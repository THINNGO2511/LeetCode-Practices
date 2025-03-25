class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #given: 1 string with rand char, ask: longest substr with no dups
        #questions: num? empty? special char? min len?

        #approach: slding wind, O(n) O(n)
        # - use a left pointer = 0, with a for loop (for right in enumerate(s)):
        # - use a set to check memebership
        # - as right idx iterate thru s, it adds in the set
        # - while char in set, move left, bc it's more than 1 freq for that char

        left, result = 0 ,0
        mp = set()

        for right, char in enumerate(s):
            #while statement to move left as long as char exists in mp
            while char in mp:
                mp.remove(s[left])
                left += 1

            mp.add(char)
            result = max(result, right - left + 1)

        return result