def Fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	
	firstNum = 0
	secondNum = 1
	for i in range(1,n):
		ans = firstNum + secondNum
		firstNum = secondNum
		secondNum = ans
		
	return ans

##main
print(Fibonacci(50))