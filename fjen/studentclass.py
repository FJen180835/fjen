#studentclass.py
class Student: #ใน class ทุกอย่างสามารถเข้าถึงกันหมดในทุก def
	def __init__(self,name): #self คือคำพิเศษใช้แทนตัวมันเอง
		self.name = name
		self.exp = 0
		self.lesson = 0
		#Call function
		# self.AddEXP(10)

	def Hello(self):
		print('สวัสดีจ้า ผมชื่อ {}'.format(self.name))

	def Coding(self):
		print('{}: กำลังเขียนโปรแกรม..'.format(self.name))
		self.exp += 5
		self.lesson += 1

	def ShowEXP(self):
		print(' - {} มีประสบการณ์ {} EXP'.format(self.name,self.exp))
		print(' - เรียนไป {} ครั้งแล้ว'.format(self.lesson))

	def AddEXP(self,score):
		self.exp += score #self.exp = self.exp + score
		self.lesson += 1

class SpecialScore():
	def __int__(self):
		self.score = 500


class SpecialStudent(Student):
		"""docstring for SpecialStudent"""
		def __init__(self,name,father):
			super().__init__(name)
			self.father = father
			mafia = ['ITu','Biden']
			if father in mafia:
				self.exp += 100

		def AddEXP(self,score):
			self.exp += (score *3) #self.exp = self.exp + score
			self.lesson += 1               

		def AskEXP(self,score = 10):
			print('ครู!! ขอคะแนนพิเศษให้ผมหน่อยสิสัก 10 ESP'.format(score))
			self.AddEXP(score)



if __name__ == '__main__':
	
	print('============== 1 Jan 2021===========')
	student0 = SpecialStudent('Mark','ITu')
	student0.ShowEXP()
	student0.AskEXP()

	student1 = Student('Albert') #เอา student1 ไปแทน self
	print(student1.name)
	student1.Hello()

	student2 = Student('Jenny') 
	print(student2.name)
	student2.Hello()

	print('============== 2 Jan 2021===========')
	print('----ใครอยากเรียน coding บ้าง?---(10xp)-----')
	student1.AddEXP(10)

	print('============== 3 Jan 2021===========')
	student1.name = 'Albert Eistien'
	print('ตอนนี้ exp ของแต่ละคนได้เท่าไรกันแล้ว?')

	print(student1.name,student1.exp)
	print(student2.name,student2.exp)

	print('============== 4 Jan 2021===========')
	for i in range(5):
		student2.Coding()

	student1.ShowEXP()
	student2.ShowEXP()


