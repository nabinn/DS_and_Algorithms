class Stack:
	"""
	Stack implementation using list.
	The end of the list is considered top.
	All operations listed below are O(1)
	"""
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)



if __name__ == '__main__':
	s=Stack()
	print(s.isEmpty())
	s.push(4)
	s.push('dog')
	print(s.peek())
	s.push(True)
	print(s.size())
	print(s.isEmpty())
	s.push(8.4)
	print(s.pop())
	print(s.pop())
	print(s.size())