#################################################################################
#
# headSwap.py
#
# Author: Ika Alfina (ika.alfina@cs.ui.ac.id)
#
#################################################################################

def headSwap(tokenList, oldHeadID, newHeadID, moveDepFlag):

	# Parameters:
	# 1) tokenList represents a sentence (list of tokens). A token is implemented as a ConlluData object
	# 2) oldHeadID: the ID of the old head: an integer
	# 3) newHeadID: the ID of the new head: an integer
	# 4) moveDepFlag: boolean, true if all dependents of the old head will be given to the new head

	# collect all dependents of the old head
	oldDependentList = []

	for token in tokenList:
		if token.getHeadID() == oldHeadID and token.getID() != newHeadID:
			oldDependentList.append(token)

	# get the current and new head object
	oldHead = tokenList[oldHeadID-1]
	newHead = tokenList[newHeadID-1]
	
	# swap the head
	label = newHead.getDeprel()
	newHead.setHeadID(oldHead.getHeadID())
	newHead.setDeprel(oldHead.getDeprel())
	oldHead.setHeadID(newHeadID)
	oldHead.setDeprel(label)

	# swap the dependents
	if moveDepFlag:
		for depToken in oldDependentList:
			depToken.setHeadID(newHeadID)

