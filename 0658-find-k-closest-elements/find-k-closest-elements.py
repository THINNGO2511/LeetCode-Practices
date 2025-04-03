import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #given: arr, k, x. Ask: return k nums closest to x (which is in arr)
        #questions: return what? neg elm? k = 0? k > len(arr)? x = any num?

        #approach: iter arr, put into k size MAX heap, calc abs dist to x
        #use MAX heap bc we need largest elem of heap to be the k-th closest to arr
        #ex: if k=4, then the 4th closest elem to x in arr has to be in heap
        #O(NlogK) O(K)

        heap, res = [], []

        for num in arr: #iter thru nums
            dist = abs(num - x) #calc dist
            if len(heap) < k: #if heap size is not at k len yet
                heapq.heappush(heap, (-dist, num)) #max num, so use -dist, the larger dist, the small -dist is
            elif dist < -heap[0][0]: #-heap[0][0] is -(-dist) of least closest in heap, aka a closer dist than curr least closest to k
                heappushpop(heap, (-dist, num))

        for dist, num in heap: #getting only 2nd elem in heap to res
            res.append(num)
        res.sort() #sort to finalize res, this is O(klogk) (k size)

        return res
        #O(NlogK) O(K)