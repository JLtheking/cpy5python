import random

class Player():
   def __init__(self, username, score):
      self.username = username
      self.score = score

def randomName():
  nameLength = random.choice(range(3,8))

  name = chr(64 + random.choice(range(1,27)))
  for i in range(1,nameLength):
    name += chr(96 + random.choice(range(1,27)))

  return name

players = []

for i in range(5000):
	username = randomName()
	score = 5000
	
	player = Player(username, score)
	players.append(player)
	
