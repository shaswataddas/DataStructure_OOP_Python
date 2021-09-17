class Graph:
	def __init__(self,edges):
		self.edges = edges
		self.nodes = {}

	def create_nodes(self):
		for sou,des,price in self.edges:
			if sou not in self.nodes:
				self.nodes[sou] = []
			self.nodes[sou].append([des,price])

	def availabe_city(self,s_key):
		print(f'Source - {s_key}')
		temp = []
		for city,price in self.nodes[s_key]:
			temp.append(city)
		print(f'Availabe city - {temp}')

	def get_total_price(self,source,destination):
		flag=0
		for city,price in self.nodes[source]:
			if(city == destination):
				print(f"From {source} to {destination} -> {price}")
				flag=1
		if flag==0:
			print("No bus is Availabe")

	def insert_value(self,parent,child,cost):
		if parent not in self.nodes:
			self.nodes[parent] = []
		self.nodes[parent].append([child,cost])

	def delete_value(self,parent,child):
		if parent not in self.nodes:
			print("No such city Present")
		else:
			index = -1
			for city,price in self.nodes[parent]:
				index+=1
				if(city==child):
					self.nodes[parent].pop(index)

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
	

	print("Availabe City From Darjeeling: ")
	g.availabe_city("Darjeeling")
	
	print('')
	print("Total cost to go to Malda From Darjeeling")
	g.get_total_price("Darjeeling","Malda")

	print('')
	print("Availabe City From Kolkata: ")
	g.availabe_city("Kolkata")
	
	print('')
	print("New Route Introduce from Kolkata to Darjeeling wiht cose 580:")
	g.insert_value("Kolkata","Darjeeling","580")
	
	print('')
	print("Availabe City From Kolkata: ")
	g.availabe_city("Kolkata")

	print('')
	print("Cost Kolkata to Darjeeling: ")
	g.get_total_price("Kolkata","Darjeeling")

	print('')
	print("Delete Route from Kolkata to Darjeeling")
	g.delete_value("Kolkata","Darjeeling")

	print('')
	print("Availabe City From Kolkata: ")
	g.availabe_city("Kolkata")
	
	print('')
	print("Cost Kolkata to Darjeeling: ")
	g.get_total_price("Kolkata","Darjeeling")
