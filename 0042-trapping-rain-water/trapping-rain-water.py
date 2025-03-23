class Solution:
    def trap(self, height: List[int]) -> int:
        #given: nums arr, ask: most water trapped
        #question: empty? min val? neg val? min len of arr?

        #approach: 2 pointers
        # l and r, with l_max and r_max
        # if l_max < r_max: (this mean lowest max wall is on left side l_max)
        # res += l_max - l_curr
        # else: (this mean lowest wall is on right side r_max)
        # res += r_max - r_curr

        res, l, r = 0, 0, len(height) - 1
        l_max, r_max = 0, 0

        while l<r:
            l_curr = height[l]
            r_curr = height[r]

            l_max = max(l_curr, l_max)
            r_max = max(r_curr, r_max)

            if l_max < r_max: #(this mean lowest wall is on left side l_max)
                res += l_max - l_curr
                l += 1
            else:
                res += r_max - r_curr
                r -= 1
        
        return res

        #O(N) O(1)
