class Player():
  def __init__(self, username, score):
    self.username = username
    self.score = score

def insert(leaderboard, playerUsername, playerScore):
	player = Player(playerUsername, playerScore)
	left = 0
	right = len(leaderboard) - 1
	
	#append player to front or back of leaderboard directly
	if playerScore > leaderboard[0].score:
		return player + leaderboard
	if playerScore < leaderboard[-1].score:
		return leaderboard + player
	
	#start loop
	while (left <= right):
		mid = (left + right) // 2
		if (leaderboard[mid].score >= playerScore) and (playerScore > leaderboard[mid+1].score):
			return leaderboard[:mid+1] + player + leaderboard[mid+1:]
		#return condition - add player into correct position
		
		if (leaderboard[mid].score >= playerScore):
			left = mid + 1
		else:
			right = mid - 1
		#change scope values
	return leaderboard