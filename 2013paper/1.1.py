with open("WORDS1.txt","r") as words:
	high = 0
	highword = ""
	word = words.readline()
	n = words.readline()
	while word != "":
		if int(n) > high:
			highword = word
			high = int(n)
		word = words.readline()
		n = words.readline()

print("term with highest amount of occurences is: " + highword + " with " + str(high) + " occurences.")