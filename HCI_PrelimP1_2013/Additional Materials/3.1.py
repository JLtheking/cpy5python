with open("MARKS.txt",'r') as infile:
	data = []
	line = infile.readline()
	while line != "": #add info from read file into a 2D array
		info = line.split(',')
		info[2] = int(info[2]) #convert the last element, which includes \n, into purely an integer
		#info[2] = info[2][0:2] will also work
		
		data.append(info)
		
		line = infile.readline()

##main
highest = 0
highestStudent = []
total = 0
numStudents = 0
for info in data:
	mark = info[2]
	if mark > highest: #update highest mark and student
		highest = mark
		highestStudent = []
		highestStudent.append(info[1])
	elif mark == highest:
		highestStudent.append(info[1]) #add student who got equally highest mark into an array
	total += mark
	numStudents += 1

highestStudentsStr = ""
for studentName in highestStudent: #print all students who got the same highest mark
	highestStudentsStr += studentName + " and "
highestStudentsStr = highestStudentsStr[:-5]

#calculate average mark and format it to 2dp
avg = "{0:.2f}".format(total / numStudents)

print("The highest mark was " + str(highest) + " scored by " + highestStudentsStr)
print("The average mark was " + avg)