# Definition of singly-linked list.
# class ListNode:
#   def __init__(self, x):
#     self.val = x
#     self.next = None

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    hare = tortise = head
    while hare and hare.next:
      hare = hare.next.next
      tortise = tortise.next
      if tortise == hare:
        return True

    return False
    
    
