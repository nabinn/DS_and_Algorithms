from stack import Stack


def rev_string(mystr):
	"""performs string reverse using stack
	"""
	s = Stack()

	# push characters of string to stack
	for ch in mystr:
		s.push(ch)
	
	result=""
	# pop characters from stack and append to result
	while not s.isEmpty():
		result += s.pop()

	return result



if __name__ == '__main__':
	
	mystr="apple1235"
	print(f"reverse of {mystr} is {rev_string(mystr)}")