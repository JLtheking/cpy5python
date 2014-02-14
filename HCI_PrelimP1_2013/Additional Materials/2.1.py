def Factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * Factorial(n-1)

print("0!: " + str(Factorial(0)))
print("50!: " + str(Factorial(50)))
print("100!:" + str(Factorial(100)))