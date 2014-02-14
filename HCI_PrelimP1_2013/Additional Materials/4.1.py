def numSyllables(line):
	syllableCount = 0
	words = line.split(' ')
	for word in words:
		if word[-1] == ',' or word[-1] == '.':
			word = word[:-1] #trim away the , and . in each word
		
		vowelCount = 0
		vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
		for i in range(len(word)): #count number of vowels in each word
			if word[i] in vowels:
				if word[i-1] in vowels:
					#is part of a group vowel
					pass
				else:
					#is an individual vowel
					vowelCount += 1
		
		if word[i] == 'e': #check if last character is e
			vowelCount -= 1
			
		if vowelCount == 0:
			vowelCount = 1 #if no vowels, in word, it is treated as 1 syllable
				
		syllableCount += vowelCount
		
	return syllableCount

##main

with open("PAS.txt",'r') as infile:
	'''to read the middle ten lines, the total number of lines in the file will be checked
	followed by getting the average - 5th line and reading ten from that number'''
	for i, line in enumerate(infile):
		pass
	lastLine = i
	midPos = lastLine // 2 - 5
	lastPos = lastLine - 10
	
	firstLines, midLines, lastLines = [],[],[]
	
	infile.seek(0)
	
	for i, line in enumerate(infile):
		line = line[:-1] #trim away the \n from each line
		
		if 0 <= i <= 9:
			firstLines.append(line)
		elif midPos <= i <= midPos + 9:
			midLines.append(line)
		elif i > lastPos:
			lastLines.append(line)
	testLines = firstLines + midLines + lastLines


numPSW = 0

for line in testLines:
	if numSyllables(line) >= 3:
		numPSW += 1
sqrtPSW = numPSW ** 0.5
SMOG = sqrtPSW + 3

print("Sample text name: PAS.txt")
print("No. of PSW: " + str(numPSW))
print("Square Root of PSW: {0:.2f}".format(sqrtPSW))
print("SMOG grade: {0:.2f}".format(SMOG)) #format SMOG to 2dp