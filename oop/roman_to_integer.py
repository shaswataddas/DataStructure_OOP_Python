class Convert:
	def __init__(self,input_roma):
		self.input_roma=list(input_roma)
		self.length = len(input_roma)-1
		self.index=0
		self.dictionary = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
		self.result = 0

		while self.index<self.length-1:
			self.result += self.add(self.input_roma[self.index])
			self.index+=1
		print(self.index, self.length)	
		self.result += self.compare(self.index)

	def show(self):
		print(self.result)

	def add(self,char):
		#print(char)
		return self.dictionary[char]

	def compare(self,ind):
		if self.dictionary[self.input_roma[ind]]<self.dictionary[self.input_roma[ind+1]]:
			return self.dictionary[self.input_roma[ind+1]] - self.dictionary[self.input_roma[ind]]
		else:
			return self.dictionary[self.input_roma[ind+1]] + self.dictionary[self.input_roma[ind]]


value = input()
converter1 = Convert(value)
converter1.show() 


