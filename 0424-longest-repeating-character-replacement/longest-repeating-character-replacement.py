class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #given: str s = "ABAB", k = 2, ask, longest str with rep char with k repl
        #question: k = 0? k max? empty s? min s? min k? 

        #approach: sliding window, O(N) O(N)
        # window is valid if: curr wind len = k + most frq char num
        # ex: AABBB = 2(k) + 3 (BBB)

        # mp = {}
        # left, res, max_freq = 0, 0, 0

        # for right, char in enumerate(s):
        #     if char not in mp:
        #         mp[char] = 0
        #     mp[char] +=1

        #     max_freq = max(max_freq, mp[s[left]])

        #     if right - left + 1 > k + max_freq:
        #         mp[s[left]] -= 1
        #         left += 1
        #         if mp[s[left]] == 0: del mp[s[left]]

        #     res = max(res, right - left + 1)

        # return res

        mp = {}
        left = 0
        res = 0
        max_freq = 0
        
        for right, char in enumerate(s):
            mp[char] = mp.get(char, 0) + 1
            max_freq = max(max_freq, mp[char])
            
            # If the number of chars to replace exceeds k, shrink the window
            while (right - left + 1) - max_freq > k:
                mp[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            
        return res
