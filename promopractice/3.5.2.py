def HashKey(ThisCountry):
	mySum = 0
	for i in range(len(ThisCountry)):
		mySum = mySum + ord(ThisCountry[i])
	
	ans = mySum % 373 + 1
	return ans

def validateHash(line,uinput):
	if (line == "                                                  \n" or line == ""):
		return False
	for i in range(len(line)):
		if 48 <= ord(line[i]) <= 57: #check if place is digit
			readCountry = line[:i-1]
			break		
	return readCountry == uinput

def LookUpCountry():
	uinput = input("Country Name:")
	uHashDigit = HashKey(uinput)
	
	with open("NEWFILE2","r") as infile:
		infile.seek(uHashDigit * 50)
		line = infile.readline()
		
		found = False
		overflow = 0
		overflowCheck = 0
		
		while not found:
			if validateHash(line,uinput):
				print(line)
				found = True
			else:
				if (uHashDigit + overflow) > 373:
					overflow = overflow - 373
					infile.seek(0)
				
				if overflowCheck > 373:
					print("country not found in NEWFILE")
					quit()
				
				overflow += 1
				overflowCheck += 1
				line = infile.readline()
		
		#for i in range(373):
		#	if i == uHashDigit:
		#		line = infile.readline()
		#		
		#		found = False
		#		overflow = 0
		#		overflowCheck = 0
		#		
		#		while not found:
		#			if validateHash(line,uinput):
		#				print(line)
		#				found = True
		#			else:
		#				if (uHashDigit + overflow) > 373:
		#					overflow = overflow - 373
		#					infile.seek(0)
		#				
		#				if overflowCheck > 373:
		#					print("country not found in NEWFILE")
		#					quit()
		#					
		#				overflow = overflow + 1
		#				overflowCheck = overflowCheck + 1
		#			
		#			line = infile.readline()
		#		
		#		#print(i,infile.readline())
		#	else:
		#		infile.readline()
				
##main
LookUpCountry()