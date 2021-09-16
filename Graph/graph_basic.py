class Graph:
	def __init__(self,edges):
		self.edges = edges
		self.nodes = {}

	def create_nodes(self):
		for sou,des,price in self.edges:
			if sou not in self.nodes:
				self.nodes[sou] = []
			self.nodes[sou].append([des,price])

	def search_city(self,s_key):
		print(f'Source - {s_key}')
		temp = []
		for city,price in self.nodes[s_key]:
			temp.append(city)
		print(f'Availabe city - {temp}')

	def get_total_price(self,source,destination):
		for city,price in self.nodes[source]:
			if(city == destination):
				print(f"From {source} to {destination} -> {price}")

if __name__ == '__main__':
	routers = [
		("Kolkata","Malda","320"),
		("Siliguri","Malda","180"),
		("Darjeeling","Malda","280"),
		("Darjeeling","Kolkata","500"),
		("Darjeeling","Siliguri","200"),
		("Kolkata","Siliguri","450"),
		("Siliguri","Malda","150")
	]

	g = Graph(routers)
	g.create_nodes()
	g.search_city("Darjeeling")
	g.get_total_price("Darjeeling","Malda")
