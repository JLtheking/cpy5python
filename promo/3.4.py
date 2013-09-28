class Stack():
	'''stack class'''
	
	def __init__(self):
		self.__list = []
	
	def push(self,element):
		self.__list.insert(0,element)
		
	def display(self):
		print("".join(self.__list))

def IMEI2HEX(quotient):
	quotient = int(quotient)
	convert = 0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'
	stack = Stack()
	
	while quotient > 15:
		rem = convert[quotient % 16]
		quotient = quotient // 16
		stack.push(str(rem))
	stack.push(str(convert[quotient]))
	stack.display()

def GetCheckDigit(IMEI):
	imeiSum = 0
	for i in range(14):
		if i % 2 == 0:#even
			imeiSum += int(IMEI[i])
		else: #odd
			tempSum =  2 * int(IMEI[i])
			if tempSum >= 10:
				tempSum = str(tempSum)
				imeiSum += int(tempSum[0]) + int(tempSum[1])
			else:
				imeiSum += tempSum
	
	checkDigit = imeiSum % 10
	if checkDigit == 0:
		return 0
	else:
		return 10 - checkDigit

def IsValidIMEI(IMEI):
	if len(IMEI) != 15: #length check
		return False
	try:
		int(IMEI)
	except: #check if IMEI is an integer
		return False
	if not GetCheckDigit(IMEI) == int(IMEI[14]):
		return False
	else:
		return True

##main
done = False
while not done:
	uinput = input("Input IMEI:")
	if uinput == "":
		done = True
	else:
		if not IsValidIMEI(uinput):
			print("invalid IMEI")
		else:
			IMEI2HEX(uinput)
