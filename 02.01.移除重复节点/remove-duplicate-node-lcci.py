class Solution:
	def removeDuplicateNodes(self, head):			
		if not (head and head.next):
			return head
		s = set()
		s.add(head.val)
		p = head
		while p and p.next:
			next = p.next
			if next.val not in s:
				s.add(next.val)
				p = p.next
			else:
				p.next = next.next
		return head