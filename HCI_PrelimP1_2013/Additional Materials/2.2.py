def Factorial(n):
	ans = n
	while n > 1:
		ans *= (n-1)
		n = n-1
	return ans

print("0!: " + str(Factorial(0)))
print("50!: " + str(Factorial(50)))
print("100!:" + str(Factorial(100)))
print("1000!:" + str(Factorial(1000)))