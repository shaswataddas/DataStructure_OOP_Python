class BST:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
	
	def addChild(self,data):
		if data==self.data:
			return

		if self==None:
			return 

		if data < self.data:
			if self.left:
				self.left.addChild(data)
			else:
				self.left = BST(data)
		
		else:
			if self.right:
				self.right.addChild(data)
			else:
				self.right = BST(data)


	def inorder(self,lst=[]):
		if self.left:
			self.left.inorder(lst)
		# print(f"  {temp.data}  ")
		lst.append(self.data)
		if self.right:
			self.right.inorder(lst)
		return lst

	def preorder(self,lst=[]):
		lst.append(self.data)
		if self.left:
			self.left.preorder(lst)

		if self.right:
			self.right.preorder(lst)

		return lst

	def postorder(self,lst=[]):
		if self.left:
			self.left.postorder(lst)

		if self.right:
			self.right.postorder(lst)
		
		lst.append(self.data)
		return lst

def minValue(node):
    current = node

    while(current.left is not None):
        current = current.left
 
    return current.data

def maxValue(node):
	current = node

	while(current.right):
		current = current.right

	return current.data

def getsum(temp,totalsum = 0):
	if temp==None:
		return 0
	totalsum = temp.data+getsum(temp.left)+getsum(temp.right)
	return totalsum

def search(temp,sdata,isfound=False):
	if temp==None:
		return False
	elif temp.data==sdata:
		isfound = True
	else:
		if sdata<temp.data:
			isfound = search(temp.left,sdata)
		else:
			isfound = search(temp.right,sdata)
	return isfound




if __name__ == "__main__":
	lst = [17,4,20,1,9,18,23,13,19,34]

	root = BST(lst[0])
	for i in range(1,len(lst)):
		root.addChild(lst[i])

	print(f"Inorder Traversal - {root.inorder()}")
	print(f"Preorder Traversal - {root.preorder()}")
	print(f"Postorder Traversal - {root.postorder()}")

	print(f"Total Sum - {getsum(root)}")

	print(f"Minimum element in the tree - {minValue(root)}")	
	print(f"Maximum element in the tree - {maxValue(root)}")	

	# for i in lst:
	# 	if search(root,i):
	# 		print(f"{i} present in Tree.")
	# 	else:
	# 		print(f"{i} not present in Tree.")

