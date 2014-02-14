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
	
	
	print(realans)

DecimalToBinary(18)
DecimalToBinary(0)
DecimalToBinary(255)
DecimalToBinary(128)
DecimalToBinary(64)