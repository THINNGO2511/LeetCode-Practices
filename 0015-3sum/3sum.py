class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #given: i,j,k unique idx, and sum of i,j,k in nums == 0
        #questions: sorted? returning what, is zero val guaranteed in nums, guaratee sum =0? min length?
        #note: no dups
        #approach: 
        # 2 ptrs, first sort, then loop i=0 to len(nums)-2 -> O(n)
        # then use 2 sum while l < r loop -> O(n) again
        # -> O(n^2) O(n) (bc of return result, which is nested list)

        nums.sort() #O(nlogn)
        res = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i-1]:  #if meet dup, then skip (for i)
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r] #total sum of i,l and r

                if total < 0:
                    l += 1
                elif total > 0:
                    r -=1
                else: # total sum = 0
                    res.append([nums[i], nums[l], nums[r]]) #then add this to list

                    while l < r and nums[l] == nums[l+1]: #skipping dup on l after sum = 0
                        l += 1
                    while l < r and nums[r] == nums[r-1]: #skipping dup on r after sum = 0
                        r -= 1

                    l+=1; r-=1 #move on to next idx for both l and r after sum = 0

        return res

        # O(n^2) O(n)