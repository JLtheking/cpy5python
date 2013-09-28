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
Others = 0
US = 0
Europe = 0
UK = 0
China = 0
India = 0

with open("IMEIS.txt","r") as infile:
	line = infile.readline()
	while line != "":
		if not IsValidIMEI:
			print(line + " is not a valid IMEI")
		else:
			rbi = line[:2]
			if rbi == "01" or rbi == "30":
				US += 1
			elif rbi == "33" or rbi == "45" or 49 <= int(rbi) <= 54:
				Europe += 1
			elif rbi == "35" or rbi == "44" or rbi == "98":
				UK += 1
			elif rbi == "86":
				China += 1
			elif rbi == "91":
				India += 1
			else:
				Others += 1
			#determine origin of mobile device, and increase the counter of the respective distribution
		
		line = infile.readline()		
print("Others:         {0:>2}%".format(Others))
print("United States:  {0:>2}%".format(US))
print("Europe:         {0:>2}%".format(Europe))
print("United Kingdom: {0:>2}%".format(UK))
print("China:          {0:>2}%".format(China))
print("India:          {0:>2}%".format(India))

