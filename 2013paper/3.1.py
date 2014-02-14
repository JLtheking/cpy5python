class Node():
	LeftP, RightP, Data = None, None, 0
	
	def __init__(self):
		self.LeftP = None
		self.RightP = None
		self.Data = ""

ThisTree = [Node() for x in range(20)]
Root = 0
NextFreePosition = 0