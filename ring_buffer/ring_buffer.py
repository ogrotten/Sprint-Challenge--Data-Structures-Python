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
		#


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

		# view = head
		# put the view contents in LBC
		# while view.next isn't head
		# 	put view.next contents in LBC
		#	view = view.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
