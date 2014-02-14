def bitshift(string):
	shiftedbit = string[0]
	newstring = ""
	for i in range(1,8): #shifts all bits forward by 1, except the eighth bit
		newstring += string[i]
	newstring += shiftedbit
	return newstring

inputAccepted = False
while not inputAccepted:
	string = input("Input bits to shift: ")

	#validate input
	if string == "":
		print("Empty input") #presence check
	elif len(string) != 8:
		print("Input must be 8-bit") #length check
	else:
		
		for i in range(len(string)):
			if string[i] != '0' and string[i] != '1': #value check
				print("Input can only utilise the digits 0 and 1 for bits")
				break
		else:
			inputAccepted = True

string = bitshift(string)
print(string)