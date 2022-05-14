import sys
from import_export_conllu import importTreebank, exportTreebank
from compoundHeadSwap import compound
from changeLabels import changeAllLabels

#################################################################################
# MAIN
#################################################################################

def main():

	if len(sys.argv) != 5:
		print("Usage: program.py -i [inputfile] -o [outputfile] ")
		print("Example: program.py -i input.conllu -o output.conllu")

	else:
		inputF = sys.argv[2]
		outputF = sys.argv[4]

		# import the treebank
		sentenceL = importTreebank(inputF)

		# convert head-direction of compound phrases
		print("\n1. Execute compound rule")
		compound(sentenceL)

		# fix the label
		print("\n2. Execute rename rule")
		changeAllLabels(sentenceL)


		# export the treebank
		exportTreebank(outputF, sentenceL)

		print("\nTree rotations were completed!")

#################################################################################
# Execute main
#################################################################################
if __name__ == '__main__':
	main()

