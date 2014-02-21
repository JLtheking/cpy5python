num = 0
list3 = []
#loop 3
while num < 1000:
	num += 3
	if num % 5 != 0: #prevents repetition of numbers in the 2 different lists
		list3.append(num)

num = 0
#loop 5
list5 = []
while num < 1000:
	num += 5
	list5.append(num)

total = 0
for num in list3:
	total += num

for num in list5:
	total += num
	
print(total) #235170