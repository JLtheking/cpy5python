def DecimalToBinary(DecimalNumber):
	ans = ""
	while DecimalNumber > 0:
		rem = DecimalNumber % 2
		DecimalNumber = DecimalNumber // 2
		ans += str(rem)
	
	numzeros = 8 - len(ans)
	
	realans = ""
	
	for i in range(numzeros):
		realans += '0'
	
	for i in range(len(ans)):
		realans += ans[len(ans) - i - 1]
	
	
	return realans

def bitshift(string):
	shiftedbit = string[0]
	newstring = ""
	for i in range(1,8): #shifts all bits forward by 1, except the eighth bit
		newstring += string[i]
	newstring += shiftedbit
	return newstring


##main
word = input("Input word to be encrypted: ")
ans = ""

for i in range(len(word)):
	char = word[i] #current character to encrypt
	charAscii = ord(char) + 1
	charBin = DecimalToBinary(charAscii)
	charShifted = bitshift(charBin)
	ans += charShifted + " "

print(ans)