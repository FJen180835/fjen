# นี่คือตัวอย่างโปรแกรมสำหรับการเรียน OOP

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install fjen
```

### วิธีเล่น

เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python

from fjen import Student, SpecialStudent

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


```
พัฒนาโดย: ลุงวิศวกร สอนคำนวณ
FB: https://www.facebook.com/UncleEngineer
YouTube: https://www.youtube.com/UncleEngineer

ปล. ขออภัย version 0.1 ลุงใช้เวลาพัฒนาแค่คืนเดียว เลยไม่ได้สมบูรณ์จ้าาาา
ปล2. ใน Mac เล่นได้ แต่ฟังชั่นคีย์บอร์ดยังติดปัญหา ไฟล์ data.csv อยู่ใน /Users/ชื่อusername
ปล3. Windows จะเก็บไฟล์ data.csv ไว้ในโฟลเดอร์ที่ติดตั้ง Python เช่น C:\Python38\data.csv หรือ แนะนำให้สร้างไฟล์ test.py แล้วพิมพ์ว่า import pimsampas แล้วรัน ไฟล์ data.csv จะอยู่ในโฟลเดอร์เดียวกับที่เซฟ


| เพจ "ลุงวิศวกร สอนคำนวณ"  | https://www.facebook.com/UncleEngineer] |
