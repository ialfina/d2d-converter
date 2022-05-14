
LOC_NOUN = ["luar", "dalam", "atas", "bawah", "utara", "selatan", "timur", "barat", "awal", "akhir", "tengah", "dekat", "seberang"]
NEGATING_WORDS = {"tidak", "tak", "bukan", "jangan"}
FOREGROUNDING_PART = {"lah", "kah", "tah"}

HARI = {"Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"}
BULAN_ID = {"Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"}
BULAN_ARAB = {"Muharram", "Shafar", "Rabiul", "Jumadil", "Rajab", "Sya'ban", "Ramadhan", "Ramadan", "Syawal", "Zulkaedah", "Zulhijjah"}
BULAN = BULAN_ID.union(BULAN_ARAB)
TIME_PROPN = HARI.union(BULAN)


TIME_UNIT = {"abad", "tahun", "bulan", "pekan", "tanggal", "hari", "zaman", "era", "periode", "masa", "musim", "saat", "waktu", "jam", "pukul", "menit", "detik"}
TIME_TENSE = {"sekarang", "besok", "kemaren", "lusa"}
TIME_NOUN = TIME_UNIT.union(TIME_TENSE)


def isPassive(aForm):

	if aForm.startswith("di") or aForm.startswith("ter"):
		return True

	else:
		return False


def compound(sentList):

	for sent in sentList:
		for token in sent:
			if token.getDeprel() == "compound":
				headToken = sent[token.getHeadID()-1]
				if token.getUPOS() == "CD":
					if headToken.getUPOS() == "CD":
						token.setDeprel("flat")

				elif token.getUPOS() == "FW":
					if headToken.getUPOS() == "FW":
						token.setDeprel("flat:foreign")
					elif headToken.getUPOS() in {"NN", "NNP"}:
						token.setDeprel("nmod")

				elif token.getUPOS() == "NN":
					if token.getForm() in LOC_NOUN:
						token.setDeprel("nmod:lmod")
					else:
						if headToken.getUPOS() in {"NN", "NNP", "FW"} :
							token.setDeprel("nmod")
				
				elif token.getUPOS() == "NNP":
					if headToken.getUPOS() in {"NN", "FW"} :
						token.setDeprel("nmod")
					elif headToken.getUPOS() == "NNP":
						token.setDeprel("flat:name")

def compound_prt(sentList):

	for sent in sentList:
		for token in sent:
			if token.getDeprel() == "compound:prt":
				headToken = sent[token.getHeadID()-1]
				if token.getUPOS() == "RP":
					if headToken.getUPOS() in {"VB", "JJ"}:
						token.setDeprel("advmod:emph")

def dep(sentList):

	for sent in sentList:
		for token in sent:
			if token.getDeprel() == "dep":
				headToken = sent[token.getHeadID()-1]
				if token.getUPOS() == "CC":
					token.setDeprel("cc")

				elif token.getUPOS() == "CD":
					if headToken.getUPOS() == "CD":
						token.setDeprel("flat")
					elif headToken.getUPOS() in {"NN", "NNP", "FW", "SYM"}:
						token.setDeprel("nummod")
					elif headToken.getUPOS() in {"VB", "JJ"}:
						token.setDeprel("obl")

				elif token.getUPOS() == "DT":
					token.setDeprel("det")

	
				elif token.getUPOS() == "IN":
					if headToken.getUPOS() in {"NN", "NNP", "FW", "PRP", "CD"}:
						token.setDeprel("case")
					elif headToken.getUPOS() in {"VB", "JJ"}:
						token.setDeprel("mark")

				elif token.getUPOS() == "MD":
					token.setDeprel("aux")

				elif token.getUPOS() == "NN":
					if token.getForm() in LOC_NOUN:
						if headToken.getUPOS() in {"NN", "NNP", "FW"}:
							token.setDeprel("nmod:lmod")
				
				elif token.getUPOS() in {"NN", "NNP", "FW", "PRP", "WP"}:
					if headToken.getUPOS() in {"NN", "NNP", "FW", "PRP", "WP", "CD"}:
						token.setDeprel("nmod")
					elif headToken.getUPOS() in {"VB", "JJ"}:
						token.setDeprel("obl")

				elif token.getUPOS() == "PRP$":
					if headToken.getUPOS() in {"NN", "NNP", "FW"}:
						token.setDeprel("nmod:poss")

				elif token.getUPOS() == "RB":
					token.setDeprel("advmod")


				elif token.getUPOS() == "RP":
					if token.getForm() in NEGATING_WORDS:
						token.setDeprel("advmod")
					elif token.getForm() in FOREGROUNDING_PART:
						token.setDeprel("advmod:emph")

				elif token.getUPOS() in {"VB", "JJ"}:
					if headToken.getUPOS() in {"NN", "NNP", "FW", "PRP", "CD"}:
						token.setDeprel("acl")
					elif headToken.getUPOS() in {"VB", "JJ"}:
						token.setDeprel("advcl")


def nmod(sentList):

	for sent in sentList:
		for token in sent:
			if token.getDeprel() == "nmod":
				headToken = sent[token.getHeadID()-1]
				if (token.getUPOS() == "NNP" and token.getForm() in TIME_PROPN) or (token.getUPOS() == "NN" and token.getForm() in TIME_NOUN):
					if headToken.getUPOS() in {"NN", "NNP", "FW", "PRP"}:
						token.setDeprel("nmod:tmod")
					elif headToken.getUPOS() in {"VB", "JJ"}:
						token.setDeprel("obl:tmod")

				elif token.getUPOS() in {"NN", "NNP", "FW", "PRP", "WP"}:
					if headToken.getUPOS() in {"VB", "JJ"}:
						token.setDeprel("obl")

def nmod_tmod(sentList):

	for sent in sentList:
		for token in sent:
			if token.getDeprel() == "nmod:tmod":
				headToken = sent[token.getHeadID()-1]
				if (token.getUPOS() == "NNP" and token.getForm() in TIME_PROPN) or (token.getUPOS() == "NN" and token.getForm() in TIME_NOUN):
					if headToken.getUPOS() in {"VB", "JJ"}:
						token.setDeprel("obl:tmod")

def nsubj(sentList):

	for sent in sentList:
		for token in sent:
			if token.getDeprel() == "nsubj":
				headToken = sent[token.getHeadID()-1]
				if headToken.getUPOS() == "VB" and isPassive(headToken.getForm()):
					token.setDeprel("nsubj:pass")


def obj(sentList):

	for sent in sentList:
		for token in sent:
			if token.getDeprel() == "obj":
				headToken = sent[token.getHeadID()-1]
				if (token.getUPOS() == "NNP" and token.getForm() in TIME_PROPN) or (token.getUPOS() == "NN" and token.getForm() in TIME_NOUN):
					if headToken.getUPOS() == "VB":
						token.setDeprel("obl:tmod")

				else:
					if isPassive(headToken.getForm()):
						token.setDeprel("obl")


def changeAllLabels(sentList):

	compound(sentList)
	compound_prt(sentList)
	dep(sentList)
	nmod(sentList)
	nmod_tmod(sentList)
	nsubj(sentList)
	obj(sentList)




	

				