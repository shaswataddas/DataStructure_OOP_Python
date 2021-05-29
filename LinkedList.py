class Node:
	def __init__(self,data=None,next=None):
		self.data=data
		self.next=next
class LinkedList:
	def __init__(self):
		self.head=None

	def insert_at_begining(self,data):
		node = Node(data,self.head)
		self.head = node

	def insert_at_end(self,data):
	 	if self.head==None:
	 		self.head = Node(data,None)
	 		return
	 	itr = self.head
	 	while itr.next:
	 		itr = itr.next
	 	itr.next = Node(data,None)
	 	
	def remove_at_index(self,index):
		if self.head==None:
			print('LinkList is Empty.')
			return
		if index < 0 or index > self.find_lenght()-1:
			print('Not Sufficient Elements.')
			return
		if index==0:
			self.head = self.head.next
			return
		itr = self.head
		while index-1:
			index -= 1
			itr = itr.next
		itr.next = itr.next.next

	def insert_at_index(self,index,data):
		if index>self.find_lenght() or index<0:
			print("Out of Index")
			return
		if index==0:
			self.head = Node(data,self.head)
			return
		itr = self.head
		while index-1:
			index -= 1
			itr = itr.next
		node = Node(data,itr.next)
		itr.next = node

	def show(self):
		if self.head==None:
			print('LinkedList is Empty.')
			return

		itr = self.head
		llstr = ''
		while itr:
			llstr += str(itr.data) + ' ==> '
			itr = itr.next
		print(llstr)

	def insert_values(self,data_list):
		self.head=None
		for data in data_list:
			self.insert_at_end(data)

	def find_lenght(self):
		count=0
		itr = self.head
		while itr:
			itr = itr.next
			count+=1
		return count

if __name__ == '__main__':
	print('\n\nCreate a LinkedList called : l1')
	l1 = LinkedList()
	l1.insert_at_begining(1)
	l1.insert_at_begining(2)
	l1.insert_at_begining(3)
	l1.insert_at_end(4)
	l1.insert_at_end(5)
	l1.insert_at_end(6)
	print('3 insert at begining(1,2,3) and 3 insert at end(4,5,6) performed.')
	print('Result LinkedList: ')
	l1.show()

	print('\n\ncreate a LinkedList called : l2')
	l2 = LinkedList()
	print('Inserting values from a list [20,40,60,80,100] :')
	l2.insert_values([20,40,60,80,100])
	print('\nResult LinkedList: ')
	l2.show()
	print('\nLength of the LinkList: '+str(l2.find_lenght()))
	print('\ninsert value at index 2 , value 25')
	l2.insert_at_index(2,25)
	l2.show()
	print('25 added')
	print('\nDelete value at index 3:')
	l2.remove_at_index(3)
	l2.show()
	print('60 removed.')