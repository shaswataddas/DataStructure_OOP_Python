class BST:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def addChild(self,data):
		if data==self.data:
			return
		
		if data<self.data:
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
		lst.append(self.data)
		if self.right:
			self.right.inorder(lst)
		return lst

def findheight(node):
	if node is None:
		return -1

	else:

		lheight = findheight(node.left)
		rheight = findheight(node.right)

		return max(lheight,rheight)+1

def checkBal(node,isBal=True):
	if not isBal:
		return isBal
	
	if node is None:
		return -1

	else:
		leftsub = checkBal(node.left)
		rightsub = checkBal(node.right)
		
		diff = abs(findheight(leftsub) - findheight(rightsub))

		print(diff)





if __name__ == '__main__':
	arr = [20,10,30,15,5,25,35,50,55,60,26,27,28]
	root = BST(arr[0])
	for i in arr:
		root.addChild(i)

	print(f"Inorder - {root.inorder()}")

	print(f"Height - {findheight(root)}")

	checkBal(root)

