class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #given: nums arr with upper half sorted and lesser at the back: 4560123, target num
        #ask: find tar in arr with O(logn) complexity -> only Bin Search
        #question: return what? (-1 if none, idx of tar if yes) guarantee ans? neg elem? neg tar? empty arr, dups? 

        #approach: bin search, with a twist:
        # if mid = tar -> return mid
        # if mid >= left, then subarr left is sorted 
        #-> if tar>=left & tar<mid (it's in btween left and mid) -> right = mid - 1;
        #-> else: (tar>mid): left = mid+1
        # else: (nums[mid] < nums[l]) then subarr on right is sorted
        # -> if tar >= mid & tar <= right (it's in btween mid and right) ->left = mid + 1
        #else: (tar<mid) -> right = mid -1

        # O(logN) O(1)

        l, r = 0, len(nums)-1

        while l<=r: #need to find tar, so = is fine
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]: #left subarr is sorted
                #check if tar is l<=tar<mid
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else: #not in left subarr range
                    l = mid + 1
            else: #right subarr is sorted
                #check if tar is mid<=tar<r
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else: # not in right subarr range
                    r = mid - 1
        
        return -1
