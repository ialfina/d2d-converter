#################################################################################
# Class ConlluData
#
# represents a token (a row of 10 columns) in CoNLLU format
#
# Author: Ika Alfina (ika.alfina@cs.ui.ac.id)
#
#################################################################################

class ConlluData:

	def __init__(self, ID, form, lemma, UPOS, XPOS, FEAT, headID, deprel):
		self.ID = int(ID) # colomn 1
		# self.ID = ID # colomn 1
		self.lemma = lemma # colomn 2
		self.form = form # colomn 3
		self.UPOS = UPOS # colomn 4
		self.XPOS = XPOS # colomn 5
		self.FEAT = FEAT # colomn 6
		self.headID = int(headID) # colomn 7
		self.deprel = deprel # colomn 8

	def getID(self):
		return self.ID

	def getLemma(self):
		return self.lemma
	
	def getForm(self):
		return self.form

	def getUPOS(self):
		return self.UPOS

	def getXPOS(self):
		return self.XPOS

	def getFEAT(self):
		return self.FEAT

	def getHeadID(self):
		return self.headID

	def getDeprel(self):
		return self.deprel

	def getConlluStr(self):
		#separator = "\t"
		theString = str(self.ID) + "\t" + self.form + "\t" + self.lemma + "\t" + \
					self.UPOS + "\t" + self.XPOS + "\t" + self.FEAT + "\t" + \
					str(self.headID) + "\t" + self.deprel + "\t" + "_" + "\t" + "_"

		return theString

	# -------------------------
	# changing value

	def setForm(self, form):
		self.form = form
	def setLemma(self, lemma):
		self.lemma=lemma

	def setUPOS(self, UPOS):
		self.UPOS = UPOS

	def setFEAT(self, FEAT):
		self.FEAT=FEAT
	
	def setHeadID(self, headID):
		self.headID = headID

	def setDeprel(self, deprel):
		self.deprel = deprel

	
