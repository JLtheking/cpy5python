import random

class Player():
   def __init__(self, username, score):
      self.username = username
      self.score = score

def quickSortPlayers(players):
	if players == []:
		return []
	
	left = []
	right = []
	pivot = players[0].score
	
	for player in players[1:]:
		if player.score < pivot:
			left.append(player)
		else:
			right.append(player)
			
	left = quickSortPlayers(left)
	right = quickSortPlayers(right)
	
	return right + [players[0]] + left

def randomScore():
  return random.choice(range(0,100000))

def randomName():
  nameLength = random.choice(range(3,8))

  name = chr(64 + random.choice(range(1,27)))
  for i in range(1,nameLength):
    name += chr(96 + random.choice(range(1,27)))

  return name

players = []

for i in range(5000):
	username = randomName()
	score = randomScore()
	
	player = Player(username, score)
	players.append(player)
	
leaderboard = quickSortPlayers(players)