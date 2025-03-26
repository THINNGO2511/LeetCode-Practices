class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        #given: nums arr, k . Ask: return sum of k wind len but wind only has unique elem
        #question: empty arr? k = 0? min k? min len of nums? nums = [1] k = 1, can k > nums len, neg elem?

        #approach: fixed len slid wind, use set or hashmap to track memeber ship in wind
        #track max sum of wind
        # then move wind if len win > k or repetion
        # O(N) O(K)

        start = max_sum = curr_sum = 0
        mp = set()

        for i in range(len(nums)):
            while nums[i] in mp:
                curr_sum -= nums[start]
                mp.remove(nums[start])
                start += 1

            curr_sum += nums[i]
            mp.add(nums[i])

            if (i - start + 1) == k: #reach k len for slid win
                max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[start]
                mp.remove(nums[start])
                start += 1
        
        return max_sum