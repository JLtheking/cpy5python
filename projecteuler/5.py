currentnum = 2520
found = False
while not found:
	for i in range(20,1,-1):
		if currentnum % i != 0:
			print(currentnum)
			break
		if i == 2:
			print(currentnum)
			found = True
			break
	currentnum += 1