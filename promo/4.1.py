import random
import datetime

##main
username = input("Enter username:")
timestamp = datetime.datetime.now()
timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
print("Hello " + username + "!")
print("The time now is " + timestamp)

with open("LEADERBOARD.DAT","r") as infile:
	leaderArr = []
	
	line = infile.readline()
	while line != "":
		leader = line.split(",")
		leaderArr.append(leader)
		line = infile.readline()
	
	
for leader in leaderArr:
	print("The current game leader is " + leader[1] + " with a score of " + leader[2])
	

with open("QUESTIONS.DAT","r") as infile:
	line = infile.readline()
	qArr = []
	while line != "":
		if line[0] == "Q":
			question = []
			question.append(line)
			
			line = infile.readline()
			while line[0] == "A":
				question.append(line)
				line = infile.readline()
				if line == "":
					break
			
			qArr.append(question)
numQ = len(qArr)
score = 0
done = False
while not done:
	proceed = input("Proceed? [y/n]")
	if proceed == "n":
		done = True
		break
	elif proceed == "y":
		for i in range(numQ):
			print(qArr[i][0])
			numA = len(qArr[i]) - 1
			for j in range(1,numA):
				print(qArr[i][j])
			uinput = input("Enter Answer:")
			correct = False
			while not correct:
				if uinput == "1":
					print("correct!")
					correct = True
					score += 1
				else:
					print("wrong!")
			
	else:
		print("Invalid input.")
