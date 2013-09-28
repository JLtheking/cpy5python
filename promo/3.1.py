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
	foo = input("Input IMEI:")
	if foo == "":
		done = True
	else:
		print(IsValidIMEI(foo))