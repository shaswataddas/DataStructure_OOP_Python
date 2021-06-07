class Check:
	def __init__(self,input_par):
		self.input_par = list(input_par)
		self.i=1
		self.top = -1
		self.flag = 0
		self.stack = list()
		self.dic = {"("}
		for i in self.input_par:
			#print(i,self.stack)
			if self.adding(i):
				self.stack.append(i)
				self.top += 1
			else:
				self.removeing(i)
				if self.flag:
					break
	def show(self):
		print(self.input_par)

	def adding(self,char):
		if char in ("(","{","["):
			return True
	def removeing(self,char):
		#print(self.stack[self.top],char)
		#print("\n")
		#print(ord(self.stack[self.top]),ord(char))
		if abs(ord(self.stack[self.top])-ord(char))<5:
			#print("Done")
			self.stack.remove(self.stack[self.top])
			self.top-=1
			self.i+=1
		else:
			#print("Not Done")
			self.flag = 1
	def result(self):
		#print(self.flag,self.top)
		if self.flag==1 or self.top>0:
			print("InValid")
		else:
			print("valid")

c1 = Check("[{{()}}](){}")
c1.result()           # valid
