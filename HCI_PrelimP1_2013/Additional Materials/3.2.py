with open("MARKS.txt",'r') as infile:
	data = []
	line = infile.readline()
	while line != "": #add info from read file into a 2D array
		info = line.split(',')
		info[2] = int(info[2]) #convert the last element, which includes \n, into purely an integer
		#info[2] = info[2][0:2] will also work
		
		data.append(info)
		
		line = infile.readline()

##3.1
highest = 0
total = 0
numStudents = 0
for info in data:
	mark = info[2]
	if mark > highest: #update highest mark and student
		highest = mark
	total += mark
	numStudents += 1

#calculate average mark and format it to 2dp
avg = "{0:.2f}".format(total / numStudents)


##main
with open("GRADES.txt",'w') as outfile:
	for line in data: #loop for each line read
		
		line.append(avg) #add average into next element to be output
		
		#calculate grade
		mark = line[2]
		if mark == highest: #current student is highest scoring student
			grade = 'M'
		elif mark < float(avg) - 10: #score 10 marks below module average
			grade = 'F'
		else:
			grade = 'P'
		
		line.append(grade) #add grade as next element
		
		line[2] = str(line[2]) #convert integer into string, so the array can work with .join
		finalString = ",".join(line) #compiles all elements into one final string to be output
		finalString += "\n"
		
		outfile.write(finalString) #writes line into GRADES.txt