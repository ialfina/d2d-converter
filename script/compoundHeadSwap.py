#################################################################################
#
# compoundHeadSwap.py 
#
# to swap the position of head-dependent of compounds deprel, along with its associated dependents
#
# input: a dependency treebank in ConLLU format, the output of Stanford UD Converter
#
# output: a revised treebank that suits Indonesian for compound label
#
# warning: make sure there are 2 blank lines after the last sentence of the input file 
#
# @author Ika Alfina ika.alfina@cs.ui.ac.id
#
#################################################################################

from headSwap import headSwap

#################################################################################
# to generate list of phrases (pair of head and dependent) with compound label in a sentence 
#################################################################################
	
def generatePhraseList(sent):
	compoundPhrases = {}
		
	# create the list of "head of compound" and its dependent list
	for token in sent:

		if token.getDeprel() == "compound":
			ID = token.getID()
			head = token.getHeadID()

			if head not in compoundPhrases:
				dependentList = []
				dependentList.append(ID)
				compoundPhrases[head] = dependentList
			else:
				dependentList = compoundPhrases[head]
				dependentList.append(ID)
				compoundPhrases[head] = dependentList

	return compoundPhrases

#################################################################################
# the compound rule 
#################################################################################

LOC_NOUN = ["luar", "dalam", "atas", "bawah", "utara", "selatan", "timur", "barat", "awal", "akhir", "tengah", "dekat", "seberang"]

def compound(sentenceList):
	

	for sent in sentenceList:
		compoundPhrases = generatePhraseList(sent)

		
		for head_ID in compoundPhrases:

			# got the objects needed for current compound phrase

			token_head = sent[head_ID-1]

			depTokenDataList = []
			depList = compoundPhrases[head_ID]

			for dep in depList:
				depToken = sent[dep-1]
				depTokenDataList.append(depToken)

			
			firstDep = depTokenDataList[0]

			# exclude the special cases
 			# 1. locative nouns with head final 
			if firstDep.getForm() in LOC_NOUN: 
				pass

 			# other wise, conduct the compound head-swap
			else:
				oldHeadID = head_ID
				newHeadID = firstDep.getID()
				headSwap(sent, oldHeadID, newHeadID, True)

				# update the compound-phrase
				for head in compoundPhrases:
					tmp = compoundPhrases[head]
					if oldHeadID in tmp:
						idx = tmp.index(oldHeadID)
						tmp[idx] = newHeadID
						compoundPhrases[head] = tmp

