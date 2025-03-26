import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #given: piles [], h = num, 
        #ask: min k speed to eat elem in piles,
        # so that ceil sum of elem/k = h
        #ex: 3/4(=1) + 6/4(=2) + 7/4(=2) + 11/4(=3) = 8 (k= 4 and is minimum to reach h hours)

        #question: neg elem? pile mins size? h = 0? elem = 0? k guarantee?

        #approach: bin search, l=1 (lowest speed) & r = max(piles) (highest speed, eat highest pile in 1 hour)
        # canEat func (mid): determine if input speed(mid) can finish all piles within h hours (valid)
        # mid = (l+r)//2
        # if not canEat (mean eating speed too low)-> l = mid + 1 (move to higher range)
        # else: (eating speed is good(valid))-> r = mid (lower range to find min speed)

        #O()

        def canEat(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile/speed)
            return time <= h

        l, r = 1, max(piles)

        while l<r:
            mid = (l+r)//2

            if not canEat(mid):
                l = mid +1
            else:
                r = mid

        return l
