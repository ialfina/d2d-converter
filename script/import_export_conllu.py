#################################################################################
#
# Code for import-export the Conllu treebank
#
# Author: Ika Alfina (ika.alfina@cs.ui.ac.id)
#
#################################################################################

from conllu import ConnluData

#################################################################################
# IMPORT THE TREEBANK
#################################################################################

def importTreebank(inputfile):

	sentenceList = []
	tokenList = []

	fileObj = open(inputfile, "r")
	lines = fileObj.readlines()
	
	for line in lines:
		if line.startswith("#") == False: #ignore comments
			tokens = line.split("\t")
			if len(tokens) == 10:
				# 0 = ID, 1 = FORM, 3 = UPOS, 4 = XPOS, 5 = FEAT, 6 = head_id, 7 = deprel
				# check multiword token line
				if "-" not in tokens[0]: # ignore multiword tokens line
					tmp = ConlluData(tokens[0], tokens[1], tokens[2], tokens[3], tokens[4], tokens[5], tokens[6], tokens[7])
					tokenList.append(tmp)
			else:
				sentenceList.append(tokenList)
				# reset the tokenList for the next sentence
				tokenList = []

	return sentenceList

#################################################################################
# EXPORT to the output treebank file
#################################################################################

def exportTreebank(outFileName, sentenceList):

	outputfile = open(outFileName, "w")

	# sent_id = 1

	for sent in sentenceList:
		# outputfile.write("# " + "sent_id = " + str(sent_id) + "\n")
		# outputfile.write("# " + "text_id = " + sent.getSentenceStr() + "\n")

		# for token in sent.getTokenList():
		for token in sent:
			theStr = token.getConlluStr() + "\n" # convert to the CoNLLU format
			outputfile.write(theStr)

		outputfile.write("\n")
		# sent_id += 1
			
	outputfile.close()

