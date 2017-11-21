

class Node(object):
	def __init__(self, content, value, size):
		self.content = content
		self.value = value
		self.size = size
		self.bit = None
		self.parent = None

	def __gt__(self, other):
		if self.value != other.value:
			return self.value > other.value
		elif self.size != other.size:
			return self.size > other.size
		else:
			return self.content > other.content

	def __lt__(self, other):
		if self.value != other.value:
			return self.value < other.value
		elif self.size != other.size:
			return self.size < other.size
		else:
			return self.content < other.content

	def __str__(self):
		return "('{}', {})".format(self.content, self.value)

	def code(self):
		if self.parent and (self.parent.bit != None):
			return (self.parent.code() << 1) | self.bit
		else:
			return self.bit

class HList(list):
	def push(self, item):
		if not self or item > self[-1]:
			self.append(item)
		elif item < self[0]:
			self.insert(0, item)
		else:
			for i in xrange(len(self) - 1):
				if item > self[i] and item < self[i + 1]:
					self.insert(i + 1, item) 
					break

	def pop_pair(self):
		return (self.pop(0), self.pop(0))

	def __str__(self):
		s = ""
		for i in self:
			s += str(i)
		return "[" + s + "]"


s = "she sells seashells"
letters = [Node(letter, s.count(letter), 1) for letter in set(s)]

l = HList()
for letter in letters:
	l.push(letter)
print l


while len(l) > 1:
	a, b = l.pop_pair()
	a.bit = 0
	b.bit = 1
	n = Node("".join(sorted(a.content + b.content)), a.value + b.value, a.size + b.size)
	a.parent = n
	b.parent = n
	l.push(n)

print l

for letter in letters:
	print "'{}' {}".format(letter.content, bin(letter.code()))



