class TreeNode:
	def __init__(self,data):
		self.data = data
		self.children = []
		self.parent = None

	def addChild(self,child):
		child.parent = self
		self.children.append(child)

	def print_tree(self):
		lv = self.get_level()
		prefix = "   "*lv
		print(f"{prefix}|--{self.data}")
		if self.children:
			for child in self.children:
				child.print_tree()
	def get_level(self):
		level = 0
		p = self.parent
		while p:
			level+=1
			p = p.parent

		return level


def build_product_tree():
	root = TreeNode("Company")

	it_com = TreeNode("IT Company")
	it_com.addChild(TreeNode("TCS"))
	it_com.addChild(TreeNode("CTS"))
	it_com.addChild(TreeNode("Infosys"))

	product_com = TreeNode("Product Company")
	product_com.addChild(TreeNode("DeltaX"))
	product_com.addChild(TreeNode("XYZ"))

	service_com = TreeNode("Service Company")
	service_com.addChild(TreeNode("Mck&Rice"))
	service_com.addChild(TreeNode("Maventic"))

	root.addChild(it_com)
	root.addChild(product_com)
	root.addChild(service_com)

	return root	


root = build_product_tree()
root.print_tree()


