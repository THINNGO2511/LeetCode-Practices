class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Instead of swapping numbers all the time, we just "push" non-zero numbers to the front in one go,
        #and then fill the rest with zeros, cutting down the number of operations. (no swap) (same space and time complexity)

        #2 ptrs, using 1 ptr nxtNonZero idx to hold last 0 val to swap with i
        # then loop thru arr, if zero, skip
        #if not, then nxtNonZero += 1, and swap with the idx with zero val
        #keep swap and go till the end

        nxtNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0: #if 0 then skip, else incre and swap
                nums[i], nums[nxtNonZero] = nums[nxtNonZero], nums[i]
                nxtNonZero += 1

        #O(n) O(1)
