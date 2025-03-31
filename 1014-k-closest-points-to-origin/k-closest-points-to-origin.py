import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:    
        #given: 2D arr, wityh coord, and k num. Ask: return k closest (shortest) coord pairs to [0,0]
        #questions: k > len(pts)? any num in coord? returning what? k = 0?

        #approach: compute dist = x^2+y^2 to [0,0], then put in a heap [dist, x,y], and return k times min heap
        #O(NlogK) (loop thru the entire pts arr, with heapify ops (logK) every iteration) O(k)

        heap = [] #-> heap
        res = []
        for (x,y) in points: #iter thru pts
            dist = x**2 + y**2 #calc dist, no need to sqrt, bc it takes O(N^(1/2))
            heapq.heappush(heap, (dist, x, y)) #put trip pair (dis,x,y) to heapify in heap
        
        for _ in range(k): #only need to iter k times to get k pairs
            _, x, y = heapq.heappop(heap)
            res.append((x, y))

        return res