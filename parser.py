from pinyin import *
	
def read_file(file_name):
	
	# EXAMPLE INPUT LINE:   㐖 㐖 [Ye4] /see
	# TRADITIONAL_HANZI SIMPLIFIED_HANZI [PINYIN] /TRANSLATION
	
	# Put each dictionary item into the array
	items = []

	f = open(file_name, "r")
	lines = f.readlines()
	
	for line in lines[500:505]:
		#print(line)
		l = line.strip()
		
		#These are info lines at the beginning of the file
		#NOTE: Might be useful to store version #, date, etc for dictionary reference
		if l.startswith(("#", "#!")):
			continue

		#partition out definition text, replace slshes with semicolons, normalize quotations, get rid of any \n
		assert l.partition('/')[2].split('/')[-1] == ""
		defi_list = l.partition('/')[2].split('/')[:-1]
		#Get trad and simpl hanzis then split and take only the simplified
		trad, simp = [e.strip(" ") for e in l.partition('[')[0].split(' ', 1)]
		#Take the content in between the two brackets
		pin = l.partition('[')[2].partition(']')[0]
		#TODO: make accented pin
		print(l.strip())
		print(defi_list)
		print(trad)
		print(simp)
		print(pin)
		print("")
		
		pin = convert(pin);			
		
		#items.append({"hanzi":han, "pinyin":pin, "def":defi})
	
	#for e in items:
	#	print(e)
	#write_file("CH_DIC.js", items)
		
read_file("cedict_1_0_ts_utf-8_mdbg.txt")
