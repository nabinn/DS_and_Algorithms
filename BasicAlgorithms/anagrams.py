"""
Anagram Detection:

One string is an anagram of another if the second is simply a rearrangement 
of the first. For example, 'heart' and 'earth' are anagrams. 
The strings 'python' and 'typhon' are anagrams as well

"""


def anagrams(word1, word2):
	"""
	1.check if both strings are of equal length
	2.convert to lowercase
	3.convert one of the strings to list
	4.for each character in the other string: 	
		a. search for the character in the list
	   	b. if character is found set that character to None, otherwise return False 	
	   	c. if all the characters are found return True

	This has quadratic complexity O(n2)
	"""
	if len(word1) != len(word2):
		return False
	else:
		word1 = word1.lower()
		word2 = word2.lower()
	# convert the second string to list because strings are immutable in python
	lst2 = list(word2)

	pos1 = 0
	stillOK = True

	while pos1 < len(word1) and stillOK:
		pos2 = 0
		found = False
		while pos2 < len(lst2) and not found:
				if word1[pos1] == lst2[pos2]:
					found = True
				else:
					pos2 += 1
		if found:
			lst2[pos2] = None
		else:
			stillOK = False

		pos1 += 1

	return stillOK



def anagrams2(word1, word2):
	""" Sort and Compare:
	First sort both words and compare each letters.
	Even though we are looping once, the complexity is 
	dominated by sorting function which takes n log(n)

	Time complexity:  log linear / O(n log (n)) 
	"""
	if len(word1) != len(word2):
		return False
	else:
		lst1 = list(word1.lower())
		lst2 = list(word2.lower())
	# list.sort() sorts the list in-place as opposed to 
	# sorted(list) which returns a new sorted list without changing the original
	lst1.sort() 
	lst2.sort()

	match = True
	for idx in range(len(lst1)):
		if lst1[idx] !=lst2[idx]:
			match = False
	return match



def anagrams3(word1, word2):
	""" Count and Compare:
	In order to decide whether two strings are anagrams, we will first 
	count the number of times each character occurs. Since there are 26 
	possible characters, we can use a list of 26 counters, one for each 
	possible character. Each time we see a particular character, we will 
	increment the counter at that position. In the end, if the two lists 
	of counters are identical, the strings must be anagrams.

	Time complexity: linear / O(n)

	Although this solution was able to run in linear time, it could only do so 
	by using additional storage to keep the two lists of character counts. 
	In other words, this algorithm sacrificed space in order to gain time.
	"""
	if len(word1) != len(word2):
		return False
	else:
		word1 = word1.lower()
		word2 = word2.lower()

	# list storing counter for letters in the two words
	c1 = [0]*26
	c2 = [0]*26

	# python character to integer conversion and vice versa
	# ord('a') gives 97 
	# chr(97) gives 'a'
	
	for ch in word1:
		position = ord(ch) - ord('a')  
		c1[position] += 1
	
	for ch in word2:
		position = ord(ch) - ord('a')  
		c2[position] += 1

	match = True	
	for idx in range(len(c1)):
		if not c1[idx]==c2[idx]:
			match = False

	return match


if __name__ == '__main__':
	print(anagrams3("heart", "earth")) # True 
	print(anagrams3("python", "typhon")) # True
	print(anagrams3("heaot", "earth")) # False
	print(anagrams3("heaEt", "earthgdfdgd")) # False