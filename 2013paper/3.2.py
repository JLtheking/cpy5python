class Node():
	LeftP, RightP, Data = None, None, 0
	
	def __init__(self):
		self.LeftP = None
		self.RightP = None
		self.Data = ""

ThisTree = [Node() for x in range(20)]
Root = -1
NextFreePosition = 0

print(ThisTree)

def AddItemToBinaryTree(NewFreeItem):
	if Root == -1:
		Root = NextFreePosition
		ThisTree[NextFreePosition].Data = NewFreeItem
	else:
		#traverse the tree to find the position for the new value
		CurrentPosition = Root
		LastMove = 'X'
		
		while CurrentPosition != 0:
			PreviousPosition = CurrentPosition
			if NewFreeItem < ThisTree[CurrentPosition].Data
				#move left
				LastMove = 'L'
				CurrentPosition = ThisTree[CurrentPosition].LeftP
			else:
				#move right
				LastMove = 'R'
				CurrentPosition = ThisTree[CurrentPosition].RightP
		
		if LastMove = 'R':
			ThisTree[PreviousPosition].RightP = NextFreePosition
		else:
			ThisTree[PreviousPosition].LeftP = NextFreePosition
			
		NextFreePosition = ThisTree[NextFreePosition].LeftP

