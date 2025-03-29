# from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #given: nums arr, k num, ask: return kth largest elem in nums
        #qeustion: dup?neg elem? k<=0? guarantee ans? min size num?

        #approach: min-heap, O(nlogk) (loop n times with O(k) heap ops) O(k) (k size heap)
        #take in 1st k elem from nums, then heapify
        #then run for loop [k:], compare heap[o] with nums[i], if larger
        #then remove heap[o], add nums[i] to heap 
        #return heap[o]

        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]
        #O(nlogk) O(k)




