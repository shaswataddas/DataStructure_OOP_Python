class HashTable:
	def __init__(self):
		self.MAX = 10
		self.arr = [[] for i in range(self.MAX)]

# Method to get hash value of a particular key
	def get_hash(self,key):
		h = 0
		for i in key:
			h += ord(i) 
		#print(h)
		return h%self.MAX

# add item into Hash Table
	def add_item(self,key,val):
		print('\nRequesting to add '+str(val))
		print('adding...')
		address = self.arr[self.get_hash(key)]
		count=-1
		for index,value in address:								# Collision
			count+=1
			if index == key:
				#print(index,value,count)
				#print(self.arr[self.get_hash(key)][count][1])
				self.arr[self.get_hash(key)][count][1]=val
				print(f'{val} added to Hash Table\n')
				return
		address.append([key,val])
		print(f'{val} added to Hash Table\n')
		# print(self.arr)

# Get item From Hash Table
	def get_item(self,key):
		print('\nValue present at '+str(key)+' is :')
		#print(self.arr[self.get_hash(key)])
		try:
			for i in self.arr[self.get_hash(key)]:				# For Collision
				if key==i[0]: 
					return i[1]
		except:
			print(self.arr[self.get_hash(key)][1])

# Erase Item from the Hash Table
	def erase_item(self,key):
		print('\nRequesting to Erase '+str(key))
		print('Eraseing...')
		temp = self.arr[self.get_hash(key)]
		# print(f"		Length: {len(temp)}")
		if len(temp)>1:											# Handeling Collision
			count=0
			for item_key,value in temp:
				if key==item_key:
					temp=self.arr[self.get_hash(key)].pop(count)
					break
				count+=1
				# print(f'Erased key : {key} and associated Value : {temp}\n')
		else:			
			self.arr[self.get_hash(key)]=[]
		print(f'Erased key : {key} and associated Value : {temp}\n')

if __name__=='__main__':
	hm1 = HashTable()
	#print(hm1.get_hash('hello world!'))
	hm1.add_item('march 6',20)
	hm1.add_item('march 6',15)					# Update a already present Value(key).
	hm1.add_item('match 15',37)
	hm1.add_item('march 5',10)
	print(hm1.get_item('march 6'))
	print(hm1.get_item('match 15'))
	print(hm1.get_item('march 5'))
	hm1.erase_item('march 5')
	hm1.erase_item('march 6')
	# print(hm1.get_item('march 6'))
	print(f"Current Hash Table : {hm1.arr}")