
from stack import Stack

def par_checker(symbol_string):
	"""
	Check whether parenthesis are balanced using stack.
	if '(' is encountered => push it to stack
	if ')' is encountered => pop from stack
	return true if stack is empty at the end
	otherwise return false
	"""	
	s = Stack()
	
	for symbol in symbol_string:
		if symbol == "(": 
			s.push(symbol)
		elif symbol == ")":
			s.pop()
		else:
			continue

	return s.isEmpty()




if __name__ == '__main__':

	print(par_checker('((()))')) # True
	print(par_checker('(()')) # False
	print(par_checker('1+(2+3*(9-6))-3')) # True
	print(par_checker('1+(2+3*(9-6)-3')) # False
