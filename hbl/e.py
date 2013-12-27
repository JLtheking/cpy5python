class Player():
  def __init__(self, username, score):
   self.username = username
   self.score = score

def linearSearch(leaderboard, username):
  length = len(leaderboard)
  for i in range(length):
    if leaderboard[i].username == username:
      return leaderboard[i].score
  return 0
	 