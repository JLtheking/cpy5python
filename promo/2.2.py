fibArr = [0,1]
for i in range(100):
	fibArr.append("")

def Fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	
	try:
		newfib = int(fibArr[n-1] + fibArr[n-2])
		
		fibArr[n] = newfib
		return fibArr[n]
	except:#fibArr[n-1] has not been calculated yet
		return Fibonacci(n-1) + Fibonacci(n-2)

##main
print(Fibonacci(50))