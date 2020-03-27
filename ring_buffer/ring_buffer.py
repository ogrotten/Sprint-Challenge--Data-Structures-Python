from doubly_linked_list import DoublyLinkedList


class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = None
		self.storage = DoublyLinkedList()
		self.size = 0

	def append(self, item):
		# if size == cap
		# 	then overwrite oldest which is head
		# 	then increment current to next

		# else if size < cap
		# 	then add to tail
		# 	but NOW...
		# 	if size = cap
		#		then tail has no .next
		# 		then set tail.next to head
		if self.storage.length == self.capacity:
			self.current.value = item
			self.current = self.current.next
		else:
			self.storage.add_to_tail(item)
			if self.storage.length == 1:
				self.current = self.storage.head
			if self.storage.length == self.capacity:
				self.storage.tail.next = self.storage.head
		# print(27, self.storage.length, self.capacity)


	def get(self):
		# Note:  This is the only [] allowed
		list_buffer_contents = []

		# view = head
		# put the view contents in LBC
		# while view.next isn't head
		# 	put view.next contents in LBC
		#	view = view.next

		view = self.storage.head
		list_buffer_contents.append(view.value)
		# print(42, view.next.value)
		while view.next != self.storage.head:
			list_buffer_contents.append(view.next.value)
			view = view.next

		return list_buffer_contents

#region
# ----------------Stretch Goal-------------------

class ArrayRingBuffer:
	def __init__(self, capacity):
		pass

	def append(self, item):
		pass

	def get(self):
		pass
#endregion

f = RingBuffer(5) # capacity 5
f.append("a")
f.append("s")
f.append("d")
f.append("f")
f.append("g")
print(f.get())

f.append("0")
f.append("2")
f.append(4)
f.append(6)
print(f.get())
