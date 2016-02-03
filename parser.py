from pinyin import *
import argparse

DICTFILE = "cedict_1_0_ts_utf-8_mdbg.txt"

def print_item(item):
	print("Word number: {}".format(item["i"]))
	print("Traditional: {}".format(item["trad"]))
	print("Simplified: {}".format(item["simp"]))
	print("Pinyin: {}".format(item["pin"]))
	print("Definitions: {}".format(item["defns"]))
	print("")

def read_file(process_item):
	lines = open(DICTFILE, "r").readlines()
	for i, _line in enumerate(lines):
		line = _line.strip()

		if line.startswith(("#", "#!")): #skip comments
			continue

		#assumption about formatting of dict: trailing '/' on each line
		assert line.partition('/')[2].split('/')[-1] == ""

		defns = "; ".join(line.partition('/')[2].split('/')[:-1])
		trad, simp = [e.strip(" ") for e in line.partition('[')[0].split(' ', 1)]
		pin = decode_pinyin(line.partition('[')[2].partition(']')[0])

		item = {"i": i, "trad":trad, "simp":simp, "defns":defns, "pin": pin}
		process_item(item)

def search_file(search_term):
	def search_process_item(item):
		#substring of definition or matches the character/pinyin exactly
		if search_term == item["simp"]:
#		if search_term in item["defns"] or search_term in [item["trad"], item["simp"], item["pin"]]:
			print(search_term, item["pin"])
			#print_item(item)
	read_file(search_process_item)

def simp_to_pinyin_dict():
	import json
	return json.loads(open('temp.json', 'r').read())

	d = {}
	def process(item):
		d[item["simp"]] = item
	read_file(process)
	import json
	open('temp.json', 'w').write(json.dumps(d))
	return d

def format_anki(numbers):
	pass

def main():
	parser = argparse.ArgumentParser(description="Ned's Chinese Anki Card Assistant")
	parser.add_argument('--search', dest='search_term', type=str, help='search term')
	parser.add_argument('--words', dest='word_numbers', metavar='word_number', nargs='+', type=int, help='word numbers to make cards from')
	#parser.add_argument('--dest', dest='dest', default=None, help='destination for anki output (default stdout)')
	args = parser.parse_args()

	if args.search_term is None and args.word_numbers is None:
		parser.print_help()
		exit()

	if args.search_term is not None and args.word_numbers is not None:
		print("Error: cannot both search and print word numbers.")
		exit()

	if args.search_term is not None:
		search_file(args.search_term)
	else:
		assert args.word_numbers is not None
		format_anki(args.word_numbers)

webcore = open('webcore', 'r').read() + open('webcore_done', 'r').read()

d = simp_to_pinyin_dict()
#d['？'] = {'pin': '?', 'trad': '?'}

d2 = {}
for ch in webcore:
	if ch in d:
		assert(d[ch]['simp'] == ch)
		trad = d[ch]['trad']
		if trad == ch:
			continue
		d2[trad] = ch

for k, v in d2.items():
	print("{}\t{}".format(k, v))

exit()

for line in webcore.splitlines():
	if line == "":
		print(line)
		continue
	#print(line)
	simp, defn = line.split("\t")
	simp = simp.strip()
	defn = defn.strip()
	if simp not in d:
		#print("[*] Warning: {} not found, constructing pinyin from constituent characters.".format(simp))
		pin = "".join(d[c]['pin'] for c in simp)
		trad = "".join(d[c]['trad'] for c in simp)
	else:
		pin = d[simp]['pin']
		trad = d[simp]['trad']

	print("\t".join((trad, simp)))

	#print(line)

exit()

chars = ['们', '在', '跟', '问', '不', '四', '文', '表', '作', '有', '说', '吗', '习', '考', '一', '家', '客', '二', '生', '声', '题', '试', '请', '谢', '怎', '你', '中', '课', '么', '三', '同', '再', '气', '很', '懂', '练', '第', '好', '念', '页', '下', '师', '上', '英', '打', '演', '学', '词', '看', '开', '几', '写', '书', '大', '遍', '了', '老', '对', '没', '业', '轻', '见', '我']
for simp in chars:
	if simp not in d:
		print("[-] {} not found, exiting.".format(simp))
		exit()
	ch_info = d[simp]
	#print(ch_info)
	print("{}\t{}\t{}\t{}".format(ch_info['trad'], ch_info['simp'], ch_info['pin'], ch_info['defns']))

#simp_to_pinyin_dict()
