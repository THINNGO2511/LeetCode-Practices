# from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #or we can do heap
        heap = nums[:k] #if k = 4, take first 4 element (this seves as a window)
        heapq.heapify(heap)#heapify to sort, this is min-heap

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num) # Push the element and pop the smallest one
        
        return heap[0] # The root of the heap is the kth largest element

        #time: 0(nlogk)
        #space: 0(k) because we only have heap with k elements





