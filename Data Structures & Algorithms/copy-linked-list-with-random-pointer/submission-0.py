"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy_dict={}
        curr=head
        while curr:
            copy_dict[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            copy=copy_dict[curr]
            copy.next=copy_dict.get(curr.next)
            copy.random=copy_dict.get(curr.random)
            curr=curr.next
        return copy_dict.get(head)
        

        