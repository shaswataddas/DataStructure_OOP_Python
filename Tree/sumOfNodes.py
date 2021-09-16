class sumOfNodes:
	def __init__(self,data):
		self.data = data
		self.children = []
		self.parent = None

	def add_child(self,child):
		child.parent = self
		self.children.append(child)

	def print_tree(self):
		lv = self.get_level()*" "
		print(f"{lv}|-- {self.data}")
		if self.children:
			for child in self.children:
				child.print_tree()

	def get_sum(self,msum):
		if self.children:
			for child in self.children:
				msum = msum + self.data+child.get_sum(msum)
			return msum
		else:
			return 0


	def get_level(self):
		level = 0
		p = self.parent
		while p:
			level+=1
			p = p.parent
		return level

def build_tree():
	root = sumOfNodes(10)

	left = sumOfNodes(5)
	left.add_child(sumOfNodes(1))
	left.add_child(sumOfNodes(2))
	left.add_child(sumOfNodes(3))

	middle = sumOfNodes(15)
	middle.add_child(sumOfNodes(12))
	middle.add_child(sumOfNodes(13))
	middle.add_child(sumOfNodes(14))

	right = sumOfNodes(20)
	right.add_child(sumOfNodes(25))
	right.add_child(sumOfNodes(26))
	right.add_child(sumOfNodes(27))

	root.add_child(left)
	root.add_child(middle)
	root.add_child(right)

	return root

if __name__ == "__main__":
	root = build_tree();

	root.print_tree()
	mysum = root.get_sum(0)
	print(f"sum of all the node - {mysum}")