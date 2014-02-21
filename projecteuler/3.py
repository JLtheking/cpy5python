n = 600851475143
sqrtn = n ** 0.5
divisor = 2

while divisor < sqrtn: #divisor should never go above sqrtn
	while n % divisor == 0:
		n /= divisor
		if n == 1:
			print(divisor) #print highest prime divisor and break out of loop
			break
	divisor += 1
	
#6857