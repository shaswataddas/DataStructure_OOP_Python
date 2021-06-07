class Convert:
	def __init__(self,input_integer):
		self.input_integer = input_integer
		self.dic={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
		self.index=0
		self.result=''
		while self.input_integer>0:
			print(self.input_integer,self.result)
			for i in self.dic:
				self.index+=1
				temp = self.check(self.input_integer,i)
				print(f'Inside - {i}, {temp}')
				if temp:
					self.result = self.result + self.dic[i]*temp
					self.input_integer -= i*temp
					print(f'{self.result} - {self.input_integer}')
					break
	def show(self):
		print(self.result)

	def check(self,input,i):
		temp = input//i
		if temp:
			return temp
		else:
			return 0


number = int(input())
cv1 = Convert(number)
cv1.show()