# Using only primitive types, implement a fixed-size hash map that associates string keys with arbitrary data object references (you don't need to copy the object). Your data structure should be optimized for algorithmic runtime and memory usage. You should not import any external libraries, and may not use primitive hash map or dictionary types in languages like Python or Ruby.

# The solution should be delivered in one class (or your language's equivalent) that provides the following functions:

# constructor(size): return an instance of the class with pre-allocated space for the given number of objects.
# boolean set(key, value): stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation.
# get(key): return the value associated with the given key, or null if no value is set.
# delete(key): delete the value associated with the given key, returning the value on success or null if the key has no value.
# float load(): return a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. Since the size of the dat structure is fixed, this should never be greater than 1.
# If your language provides a built-in hashing function for strings (ex. `hashCode` in Java or `__hash__` in Python) you are welcome to use that. If not, you are welcome to do something naive, or use something you find online with proper attribution.


class hash:
	def __init__(self, size = 1):
		self.size = size
		self.table = [[] for i in xrange(size)]
		self.load = 0.7
		self.numkeys = 0
		#return self

	def set(self, key, value):
		hashval = key.__hash__()
		hashval2 = hashval%self.size
		for i in xrange(len(self.table[hashval2])):
			if self.table[hashval2][i][0] == key:
				self.table[hashval2][i] = (key, value)		#overwrite if key exists already
				return
		self.table[hashval2].append((key, value))
		self.numkeys +=1
		if float(self.numkeys)/float(self.size)>self.load:
			self.resize()

	def resize(self):
		newsize = 2*self.size
		newtable = [[] for i in xrange(newsize)]
		for chain in self.table:
			for item in chain:
				newhash = item[0].__hash__()%(newsize)
				newtable[newhash].append(item)
		self.table = newtable
		self.size = newsize

	def get(self, key):
		hashval = key.__hash__()%self.size
		for item in self.table[hashval]:
			if key==item[0]:
				return item[1]
		return None		#if key not found

	def load(self):
		return float(self.numkeys)/float(self.size)

	def delete(self, key):
		hashval = key.__hash__()%self.size
		for item in self.table[hashval]:
			if key==item[0]:
				self.table[hashval].remove(item)
				self.numkeys-=1
				return item[1]
		return None		#if key not found

	def __str__(self):
		return "size:" + str(self.size) + "\ntable: " + str(self.table) + "\nnumber of keys: " + str(self.numkeys)





