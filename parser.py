from pinyin import *
	
def read_file(file_name):
	
	# EXAMPLE INPUT LINE:   㐖 㐖 [Ye4] /see
	# TRADITIONAL_HANZI SIMPLIFIED_HANZI [PINYIN] /TRANSLATION
	
	# Put each dictionary item into the array
	items = []

	f = open(file_name, "r")
	lines = f.readlines()
	
	for line in lines[500:505]:
		l = line.strip()
		
		#These are info lines at the beginning of the file
		#NOTE: Might be useful to store version #, date, etc for dictionary reference
		if l.startswith(("#", "#!")):
			continue

		assert l.partition('/')[2].split('/')[-1] == ""
		defns = "; ".join(l.partition('/')[2].split('/')[:-1])
		#Get trad and simpl hanzis then split and take only the simplified
		trad, simp = [e.strip(" ") for e in l.partition('[')[0].split(' ', 1)]
		#Take the content in between the two brackets
		pin = decode_pinyin(l.partition('[')[2].partition(']')[0])
		items.append({"trad":trad, "simp":simp, "defns":defns, "pin": pin})
	print(items)
		
read_file("cedict_1_0_ts_utf-8_mdbg.txt")
