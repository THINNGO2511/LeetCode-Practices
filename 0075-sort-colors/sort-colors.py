class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # given: r:0 g:1 b:2, nums arr, ask to sort 012 order
        # questions: empty? missing val (0,1,2), 0s only? return what? in place?

        # approach: 3 ptrs (L, R, i), i = 0, L = 0, R = len - 1
        # explain: 
            # anything before L:0s
            # L to i - 1: 1s
            # i to R; unsorted
            # anything behind R = 2s

            # 0 0 0 1 1 2 0 1 2 2 2
            #       L   i     R

        # as i moves, swap i with L if [i] = 0s, and similar with R if [i] = 2s
        # and else if [i] = 1, i+=1 because L to i-1 is region for 1s
        # O(N) O(1)

        i, l, r =  0, 0, len(nums) - 1

        while i <= r:
            #in this case, swap l and i, then l and i +=1, bc before L is 0s region
            if nums[i] == 0: 
                nums[i], nums[l] = nums[l], nums[i]
                l+=1
                i+=1
            elif nums[i] == 2: #similarly, swap with r, but only r-=1, bc after swap, i can either hold 0s or 1s, if i+=1, we might miss that element
                nums[i], nums[r] = nums[r], nums[i]
                r-=1
            else:
                i+=1

        return nums