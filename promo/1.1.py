def bubble_sort(A):
  swapped = True # assume not sorted
  while swapped:
    swapped = False
    for i in range(1,len(A)):
      if A[i-1][0] < A[i][0]:
        A[i-1], A[i] = A[i], A[i-1]
        swapped = True
  return A

##main

bonusArr = []

for i in range(5):
	enumValidated = False
	bonusValidated = False
	while not enumValidated:
		uinput = input("Enter Employee number:")
		enumValidated = True #assume validated
		
		if uinput == "": #presence check
			if i == 0:#empty input, does not want to quit
				print("You must enter an employee number!")
				enumValidated = False
			else:#quit
				done = True
				break
			
		elif len(uinput) != 2:#length check
			print("Employee number must be 2 characters in length!")
			enumValidated = False
		
		elif uinput[0] != "E":
			print("First character of Employee number must be an 'E'!")
			enumValidated = False
			
		else:
			try:
				int(uinput[1])
				enum = uinput
			except:
				print("second character of Employee number must be an integer!")
				enumValidated = False

	
	while not bonusValidated:
		uinput = input("Enter salary of Employee:")
		bonusValidated = True #assume validated
		
		if uinput == "": #presence check
			#empty input, does not want to quit
			print("You must enter an employee number!")
			bonusValidated = False
			
		try:
			uinput = int(uinput)
			
			if not 10 <= uinput <= 5000:
				print("Salary must be between 10 and 5000 inclusive")
				bonusValidated = False
			else:
				salary = uinput
			
		except:
			print("The salary has to be an integer!")
			bonusValidated = False
			
	if salary < 1000:
		bonus = 0.1 * salary
	elif salary < 3000:
		bonus = 0.15 * salary
	else: #salary >= 3000
		bonus = 0.25 * salary
	
	bonus = "{0:.2f}".format(bonus)
	
	employee = [bonus,enum]
	
	
	bonusArr.append(employee)
	
bonusArr = bubble_sort(bonusArr)

with open("BONUS.txt","w") as outfile:
	for line in bonusArr:
		string = line[1] + " " + str(line[0]) + "\n"
		outfile.write(string)