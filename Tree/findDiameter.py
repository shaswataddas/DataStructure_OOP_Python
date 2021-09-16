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

def maxDepth(node):
    if node is None:
        return -1 ;
 
    else :
 
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1


# def findDia(temp):
# 	if temp is None:
# 		return 0

# 	leftdia = findDia(temp.left)
# 	rightdia = findDia(temp.right)

# 	lheight = maxDepth(temp.left)
# 	rheight = maxDepth(temp.right)

# 	# print(leftdia,rightdia,lheight+rheight)

# 	return max(leftdia,rightdia,lheight+rheight+2)

def findDia(temp):
	if temp is None:
		lst=[-1,0]
		return lst

	leftpair = findDia(temp.left)
	leftdia = leftpair[1]
	leftheight = leftpair[0]
	rightpair = findDia(temp.right)
	rightdia = rightpair[1]
	rightheight = rightpair[0]

	res=[0,0]

	res[0] = max(leftheight,rightheight)+1

	res[1] = max(leftdia,rightdia,leftheight+rightheight+2)

	return res



if __name__ == '__main__':
	arr = [20,10,30,15,5,25,35,50,55,60,26,27,28]
	root = BST(arr[0])
	for i in arr:
		root.addChild(i)

	print(f"Inorder - {root.inorder()}")

	print(f"Height - {maxDepth(root)}")

	print(f"Maximum Diameter - {findDia(root)}")
