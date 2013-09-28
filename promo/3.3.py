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

def GenerateIMEI():
	with open("CHINA.txt","w") as outfile:
		#generate IMEIs with model number 123456
		currSerial = 1
		for i in range(20000):
			currSerialStr = str(currSerial)
			while len(currSerialStr) < 6:
				currSerialStr = "0" + currSerialStr
			currIMEI = "86123456" + currSerialStr
			currIMEI = currIMEI + str(GetCheckDigit(currIMEI)) + "\n"
			outfile.write(currIMEI)
			
			currSerial += 1
		
		#generate IMEIS with model number 234567
		currSerial = 1
		for i in range(30000):
			currSerialStr = str(currSerial)
			while len(currSerialStr) < 6:
				currSerialStr = "0" + currSerialStr
			currIMEI = "86234567" + currSerialStr
			currIMEI = currIMEI + str(GetCheckDigit(currIMEI)) + "\n"
			outfile.write(currIMEI)
			
			currSerial += 1

##main
GenerateIMEI()