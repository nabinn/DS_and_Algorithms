def gcd(m, n):
	""" finding gcd using euclid's method:
		Euclid’s Algorithm states that the greatest common divisor of
		two integers m and n is n if n divides m evenly. However, if
		n does not divide m evenly, then the answer is the greatest common
		divisor of n and the remainder of m divided by n.
		-----------------------
		GCD(A,0) = A
		GCD(0,B) = B
		If A = B⋅Q + R and B≠0 then GCD(A,B) = GCD(B,R)
		where Q is an integer, R is an integer between 0 and B-1
	"""
	if m == 0:
		return n
	if n == 0:
		return m
	return gcd(n, m % n)


class Fraction:
	def __init__(self, num, den):
		self.num = num
		self.den = den

	def show(self):
		print(f"{self.num} / {self.den}")

	def __str__(self):
		return f"{self.num} / {self.den}"

	# overriding the addition method
	def __add__(self, other):
		new_num = self.num * other.den + self.den * other.num
		new_den = self.den * other.den
		# use gcd to reduce the fraction to its lowest terms
		common = gcd(new_num, new_den)
		return Fraction(new_num // common, new_den // common)

	def __sub__(self, other):
		new_num = self.num * other.den - self.den * other.num
		new_den = self.den * other.den
		# use gcd to reduce the fraction to its lowest terms
		common = gcd(new_num, new_den)
		return Fraction(new_num // common, new_den // common)

	def __mul__(self, other):
		new_num = self.num * other.num
		new_den = self.den * other.den
		common = gcd(new_num, new_den)
		return Fraction(new_num // common, new_den // common)

	def __truediv__(self, other):
		new_num = self.num * other.den
		new_den = self.den * other.num
		common = gcd(new_num, new_den)
		return Fraction(new_num / common, new_den / common)

	def __floordiv__(self, other):
		new_num = self.num * other.den
		new_den = self.den * other.num
		common = gcd(new_num, new_den)
		return Fraction(new_num // common, new_den // common)

	def __lt__(self, other):
		return self.num * other.den < other.num * self.den

	def __gt__(self, other):
		return self.num * other.den > other.num * self.den

	def __eq__(self, other):
		return self.num * other.den == other.num * self.den


if __name__ == "__main__":
	f1 = Fraction(1, 2)
	f2 = Fraction(1, 4)

	print(f1, ",", f2)  # __str__
	print("f1 + f2 => ", f1 + f2)  # __add__
	print("f1 - f2 => ", f1 - f2)  # __sub__
	print("f1 / f2 => ", f1 / f2)  # __truediv__
	print("f1 // f2 => ", f1 // f2)  # __floordiv__
	print("f1 == f2 =>", f1 == f2)  # __eq__
	print("f1 > f2 => ", f1 > f2)  # __lt__
	print("f1 < f2 => ", f1 < f2)  # __gt__
	print("f1 * f2 => ", f1 * f2)  # __mul__
