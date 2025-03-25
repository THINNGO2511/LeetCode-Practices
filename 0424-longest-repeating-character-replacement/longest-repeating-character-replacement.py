class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #given: str s = "ABAB", k = 2, ask, longest str with rep char with k repl
        #question: k = 0? k max? empty s? min s? min k? 

        #approach: sliding window, O(N) O(N)
        # window is valid if: curr wind len = k + most frq char num
        # ex: AABBB = 2(k) + 3 (BBB)
        # 

        mp = {}
        left, res, max_freq = 0, 0, 0

        for right, char in enumerate(s):
            if char not in mp: #adding char to mp
                mp[char] = 0
            mp[char] +=1

            max_freq = max(max_freq, mp[char]) #check if curr char has most frq

            #can be if or while
            # if curr wind len > k + most frq char: ex AAA + BBB > AA (k = 2) + BBB
            # then shrink wind by left += 1 and s[left]frq -= 1
            while (right - left + 1) > k + max_freq: 
                mp[s[left]] -= 1
                left += 1
                if mp[s[left]] == 0: del mp[s[left]]

            res = max(res, right - left + 1) #check max wind

        return res
