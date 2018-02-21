from stack import Stack

def par_checker(symbol_string):
	"""
	Check whether parenthesis are balanced using stack.
	if '(' is encountered => push it to stack
	if ')' is encountered => pop from stack
	return true if stack is empty at the end
	otherwise return false
	"""	
	opening_braces = [ch for ch in "({["]
	closing_barces = [ch for ch in ")}]"]
	# create a mapping for opening and closing baraces
	match = {k:v for k, v in zip(opening_braces,closing_barces)}

	s = Stack()
	for symbol in symbol_string:
		
		if symbol in opening_braces: 
			s.push(symbol)

		elif symbol in closing_barces:
			if match[s.pop()] != symbol:
				return False

		else:
			continue

	return s.isEmpty()


if __name__ == '__main__':
	print(par_checker('((()))')) # True
	print(par_checker('(()')) # False
	print(par_checker('1+(2+3*(9-6))-3')) # True
	print(par_checker('1+(2+3*(9-6)-3')) # False
	print(par_checker('{{([][])}()}')) # True
	print(par_checker('[{()]')) # False
