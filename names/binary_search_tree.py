class BinarySearchTree:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	#region day1

	# Insert the given value into the tree
	def insert(self, incoming):
		# print(25,self.value)
		if not self.value:
			self.value = incoming
		else:
			if incoming < self.value:
				# print("left")
				if self.left == None:
					self.left = BinarySearchTree(incoming)
				else: 
					self.left.insert(incoming)
			elif incoming >= self.value:
				# print("right")
				if self.right == None:
					self.right = BinarySearchTree(incoming)
				else:
					self.right.insert(incoming)

	# Return True if the tree contains the value
	# False if it does not
	def contains(self, target):
		if self.value == target:
			# print(39, True, target, end="\n\n")
			return True

		elif target < self.value:
			if self.left:
				# print("left at", self.value, end=", ")
				return self.left.contains(target)
			else:
				# print(44, False, target, end=" End.\n\n")
				return False

		elif target > self.value:
			if self.right:
				# print("right at", self.value, end=", ")
				return self.right.contains(target)
			else:
				# print(52, False, target, end=" End.\n\n")
				return False
		# else:
		# 	print(56, False, target, end=" End.\n\n")
		# 	return False
		print("should never get here.")

	# Return the maximum value found in the tree
	def get_max(self):
		if not self.right:
			return self.value
		return self.right.get_max()

	# Call the function `cb` on the value of each node
	# You may use a recursive or iterative approach
	def for_each(self, cb):
		cb(self.value)
		if self.left:
			self.left.for_each(cb)
		if self.right:
			self.right.for_each(cb)
	#endregion day1

