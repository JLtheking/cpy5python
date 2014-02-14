import random

class Player():
	def __init__(self, username, score):
		self.username = username
		self.score = score
		
	def display(self):
		print(self.username + ": " + self.score)
	
#assuming leaderboard already consist of a list of quicksorted players in descending order

def scoreListGenerator(leaderboard, playerScore):
	length = len(leaderboard)
	left = 0
	right = length - 1
	
	while (left <= right):
		mid = (left + right) // 2
		if (leaderboard[mid].score == playerScore):
			index = mid
		#return condition
		
		if (leaderboard[mid].score >= playerScore):
			left = mid + 1
		else:
			right = mid - 1
		#change scope values
	else:
		print("score not found in leaderboard error")
		
	if mid < 5:
		for i in range(10):
			leaderboard[i].display()
	elif length - 5 < mid:
		for i in range(10):
			leaderboard[length - 10 + i].display()
	else:
		for i in range(10):
			leaderboard[mid - 5 + i].display()