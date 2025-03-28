# from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #sort sol (cheating)
        # nums.sort(reverse=True)
        # return nums[k-1]

        #bin search sol:
        # Set the boundaries for binary search, use min and max to define the range of possible values where the kth largest element might be
        # l, r = min(nums), max(nums)
        
        # while l <= r:
        #     mid = (l + r) // 2
        #     # Count how many elements are greater than or equal to 'mid'
        #     count = sum(x >= mid for x in nums)
        #     print(count)
            
        #     if count >= k:
        #         # If there are at least 'k' elements >= mid, the kth largest is >= mid
        #         l = mid + 1
        #     else:
        #         # If there are fewer than 'k' elements >= mid, reduce the upper boundary
        #         r = mid - 1
                
        # return r  # When l > r, 'r' will hold the value of the kth largest element
        #l and r are merely indicator of number to find on array, not setting physical search boundaries

        #time: O(nlogn)
        #space: 0(1)

        #or we can do heap
        heap = nums[:k] #if k = 4, take first 4 element (this seves as a window)
        heapq.heapify(heap)#heapify to sort, this is min-heap

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num) # Push the element and pop the smallest one
        
        return heap[0] # The root of the heap is the kth largest element

        #time: 0(nlogk)
        #space: 0(k) because we only have heap with k elements





