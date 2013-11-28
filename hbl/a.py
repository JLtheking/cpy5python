class Player():
   def __init__(self, username, score):
      self.username = username
      self.score = score

done = False

players = []

while not done:
	username = input('Player name (or press ENTER to quit): ')
	if username == "":
		done = True
		break
	
	scoreValidated = False
	while not scoreValidated:
		score = int(input('Player score (between 0 and 99999 inclusive): '))
		if 0 <= score <= 99999:
			scoreValidated = True
		else:
			print("Score must be an interger between 0 and 99999 inclusive")
	
	player = Player(username, score)
	players.append(player)
	print()