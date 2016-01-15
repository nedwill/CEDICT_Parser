import json
import sys
import string

data = json.loads(open('simp_to_pinyin.json', 'r').read())

if len(sys.argv) != 2:
	print("usage: {} <filename>".format(sys.argv[0]))
	exit()

filename = sys.argv[1]
out_filename = "pinyin_" + filename
try:
	file_data = open(filename, 'r').read()
except UnicodeDecodeError:
	#assume other encoding
	file_data = open(filename, 'rb').read().decode('cp936')

def convert_char(c):
	try:
		return data[c] + " "
	except KeyError:
		return c

def convert_line(line):
	line_contains_chinese = any(c in data and c not in string.printable for c in line)
	if not line_contains_chinese:
		return line

	print(line)
	return line

open(out_filename, 'w').write("\n".join(convert_line(line) for line in file_data.splitlines()[:50]))
