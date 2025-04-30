# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #given: k sorted LL, in a arr(arr format) [[a,b,c],[d,e,f]]
        #ask: return 1 sorted LL, dup possible.
        #question: stucture for linked list class? neg val? empty ll? return linked list? returning what?
        #note: return a head node for the linked list

        #approach: 
        #use a minheap bc its a K problem
        #add in 1st elem of all linked list -> [112], along with lst_ind and node
        # val: record val
        # lst_ind: to break tie when it's the same val
        # node: to add in the res ll
        #then heap pop to add in res ll, as the smallest element
        #then add in next elem in 1st, 2nd ,.. so on
        #keep pop and add in heap until its empty

        dummy = ListNode(0)
        heap = []
        curr = dummy

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next