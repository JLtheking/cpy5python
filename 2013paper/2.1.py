import re

EmployeeID = []
Surname = []

with open("EMPLOYEEDATA.txt",'r') as infile:
	line = infile.readline()
	while line != "":
		pcode = line.split(" : ")
		for i in range(len(pcode)):
			if pcode[i][0] == "E":
				foo = pcode[i].split('"')
				EmployeeID.append(foo[1])
			elif pcode[i][0] == "S":
				foo = pcode[i].split('"')
				Surname.append(foo[1])
			
		line = infile.readline()

#print(EmployeeID)
#print(Surname)
arr = [EmployeeID,Surname]


pattern = re.compile("[SLN][0-9]{3}")

print("Search by EmployeeID or Surname:")
query = input()
if re.match(pattern, query):
	#employee search
	search = 0
	result = 1
else:
	#surname search
	search = 1
	result = 0

found = False
print("\nSearch results are:")
for i in range(len(arr[search])):
	if arr[search][i] == query:
		print(arr[result][i])
		found = True
if not found:
	if search == 1: #surname search
		print("Surname not found in database")
	else: #employee search
		print("Employee ID not found in database")