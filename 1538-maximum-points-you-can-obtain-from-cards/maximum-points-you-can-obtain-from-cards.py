class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #given: 1 arr, k wind len. 
        # ask: max point from wind
        # ex: k = 3, wind can be: first or last 3 elem, first 2 and last 1, first 1 and last 3
        #questions: min len of arr, k min? empty arr, k =0? negtive elem?

        #approach: k len slidng wind, with a linked arr in mind (aka iter from -1, 0, 1 order)
        # add in curr_sum as curr_sum move from -k ind to 0
        # i>= 0 -> curr_sum -= cardPoints[i-k] (remove last elem from curr_sum)
        # curr_sum += cardPoints[i]
        # O(N) O(1)

        curr_sum = max_sum = 0

        #going from -k in arr to k, so going from last k elem to first k elem
        for i in range(-k, k):
            curr_sum += cardPoints[i]

            #this means we are reaching the first k elem, 
            #so we need to remove prev elem at -k and so on
            if i >= 0:
                curr_sum -= cardPoints[i-k]

            max_sum = max(max_sum, curr_sum)

        return max_sum