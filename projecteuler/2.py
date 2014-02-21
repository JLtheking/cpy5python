totalevens = 2
fib1 = 1
fib2 = 2
fibnext = fib1 + fib2


while fibnext < 4000000:
	if fibnext % 2 == 0: #even
		totalevens += fibnext
	fib1 = fib2
	fib2 = fibnext
	fibnext = fib1 + fib2

print(totalevens)
#4613732