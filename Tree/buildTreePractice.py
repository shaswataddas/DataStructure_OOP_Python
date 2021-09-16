class TreeNode:
	def __init__(self,data):
		self.data = data
		self.children = []
		self.parent = None

	def addChild(self,child):
		child.parent = self
		self.children.append(child)

	def printTree(self):
		lv = self.getLevel()
		prefix = "   "*lv
		print(f"{prefix} |-- {self.data}")
		if self.children:
			for child in self.children:
				child.printTree()

	def getLevel(self):
		level = 0
		p = self.parent
		while p:
			level+=1
			p = p.parent
		return level

def buildTree():
	root = TreeNode("Nilupul (CEO)")

	cto = TreeNode("Chinmoy (CTO)")

	head = TreeNode("Gels (HR HEAD)")

	ih = TreeNode("Vishwa (Infrastructure Head)")

	ih.addChild(TreeNode("Dhaval (Cloud Manager)"))
	ih.addChild(TreeNode("Abhijit (App Manager)"))

	cto.addChild(ih)
	cto.addChild(TreeNode("Aamir (Application Manager)"))

	head.addChild(TreeNode("Peter (Recrutment Manager)"))
	head.addChild(TreeNode("Waqau (Policy Manager)"))

	root.addChild(cto)
	root.addChild(head)

	return root

if __name__ == "__main__":
	root = buildTree()
	root.printTree()



