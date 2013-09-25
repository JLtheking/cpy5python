def HashKey(ThisCountry):
	mySum = 0
	for i in range(len(ThisCountry)):
		mySum = mySum + ord(ThisCountry[i])
	
	ans = mySum % 373 + 1
	return ans


def CreateCountry():
	with open("COUNTRIES.txt","r") as infile:
		line = infile.readline()
		countryArr = []
		
		while line != "":
			for i in range(len(line)):
				if 48 <= ord(line[i]) <= 57: #check if place is digit
					myCountry = line[:i-1]
					myPopulation = line[i:]
					myPopulation = myPopulation[:len(myPopulation) - 2]
					break
			country = []
			
			myHash = HashKey(myCountry)
			
			country.append(myHash)
			country.append(myCountry)
			country.append(myPopulation)
			
			countryArr.append(country)
			
			line = infile.readline()
			
	
	#countryArr = quick_sort(countryArr) #arrange all elements in order to their hash positions		
			
	newfileArr = []
	collidedArr = []
	
	for i in range(373):
		newfileArr.append("                                                 \n")
		
	for country in countryArr: #all countries
		currHash = country[0]
		
		if newfileArr[currHash] == "                                                 \n": #check if there is collision
			currCountry = country[1]
			currPopulation = country[2]
			
			string = currCountry + " " + currPopulation
			numSpaces = 49 - len(string)
			for i in range(numSpaces):
				string += " "
			string += "\n"
			#for i in range(numSpaces):
			#	string += " "
			newfileArr[currHash] = string #if no collision, insert correct string into correct slot
		else:
			#collision
			collidedArr.append(country)
						
	for country in collidedArr: #all country objects which have collision
		currHash = country[0]
		currCountry = country[1]
		currPopulation = country[2]
		
		overflow = 1
		overflowCheck = 1
		collisionFixed = False
		while not collisionFixed:
			if (currHash + overflow) > 373:
				overflow = overflow - 373 #loop overflow back to start
				
			if overflowCheck > 373:
				print("Not enough area to store country!")
				quit()
				
			if newfileArr[currHash + overflow] == "                                                 \n": #check if overflow area is full
				string = currCountry + " " + currPopulation
				numSpaces = 49 - len(string)
				for i in range(numSpaces):
					string += " "
				string += "\n"
				newfileArr[currHash + overflow] = string #insert string into overflow area
				collisionFixed = True
				
			else:
				overflow = overflow + 1
				overflowCheck = overflowCheck + 1
			
	with open("NEWFILE2","w") as outfile:
		for line in newfileArr:
			outfile.write(line)
	
	
	
				
##main
CreateCountry()