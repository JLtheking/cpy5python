with open("WORDS2.txt","r") as words:
	high = 0
	highwords = []
	highwords.append("")
	word = words.readline()
	n = words.readline()
	while word != "":
		if int(n) > high:
			highwords = []
			highwords.append(word)
			high = int(n)
		elif int(n) == high:
			highwords.append(word)
		word = words.readline()
		n = words.readline()

highwordstr = ""

for word in highwords:
	highwordstr += str(word[:-1]) + " and "


print("terms with highest amount of occurences are: " + highwordstr[:-4] + "with " + str(high) + " occurences.")