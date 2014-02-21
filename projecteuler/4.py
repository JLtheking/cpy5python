def checkpalindrome(n):
	return n == int(str(n)[::-1])


highest = 0
for firstnum in range(999,100,-1):
	for secondnum in range(999,100, -1):
		foo = firstnum * secondnum
		if foo > highest and checkpalindrome(foo):
			highest = foo

print(highest) #906609