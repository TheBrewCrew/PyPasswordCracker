#PA 4
from misc import *
import crypt

def load_words(filename,regexp):
	"""Load the words from the file filename that match the regular
       expression regexp.  Returns a list of matching words in the order
       they are in the file."""
	words = list()
	with open(filename, 'r') as fd:
		regex = re.compile(regexp)
		for line in fd:
			match = regex.search(line.strip())
			if match:
				words.append(match.group())
	return words

def reverse(str):
	return str[::-1]

def transform_reverse(str):
	rev = str[::-1]
	if str != rev:
		return [str, rev]
	else:
		return [str]

casedict = {'A': 'a', 'a': 'A',
			'B': 'b', 'b': 'B',
			'C': 'c', 'c': 'C',
			'D': 'd', 'd': 'D',
			'E': 'e', 'e': 'E',
			'F': 'f', 'f': 'F',
			'G': 'g', 'g': 'G',
			'H': 'h', 'h': 'H',
			'I': 'i', 'i': 'I',
			'J': 'j', 'j': 'J',
			'K': 'k', 'k': 'K',
			'L': 'l', 'l': 'L',
			'M': 'm', 'm': 'M',
			'N': 'n', 'n': 'N',
			'O': 'o', 'o': 'O',
			'P': 'p', 'p': 'P',
			'Q': 'q', 'q': 'Q',
			'R': 'r', 'r': 'R',
			'S': 's', 's': 'S',
			'T': 't', 't': 'T',
			'U': 'u', 'u': 'U',
			'V': 'v', 'v': 'V',
			'W': 'w', 'w': 'W',
			'X': 'x', 'x': 'X',
			'Y': 'y', 'y': 'Y',
			'Z': 'z', 'z': 'Z'}
def transform_capitalize(str):
	words = [str]
	for i, char in enumerate(str):
		if char in casedict:
			end = casedict[char] + str[i+1:]
			words.extend([word[:i] + end for word in words])
	return words

digitdict = {'o': ['0'], 'O': ['0'],
			 'z': ['2'], 'Z': ['2'],
			 'a': ['4'], 'A': ['4'],
			 'i': ['1'], 'I': ['1'],
			 'l': ['1'], 'L': ['1'],
			 'e': ['3'], 'E': ['3'],
			 's': ['5'], 'S': ['5'],
			 't': ['7'], 'T': ['7'],
			 'g': ['9'], 'G': ['9'],
			 'q': ['9'], 'Q': ['9'],
			 'b': ['6','8'], 'B': ['6','8']}
def transform_digits(str):
	words = [str]
	for i, char in enumerate(str):
		if char in digitdict:
			words2 = list(words)
			for digit in digitdict[char]:
				end = digit + str[i+1:]
				words.extend([word[:i] + end for word in words2])
	return words

def check_pass(plain,enc):
	"""Check to see if the plaintext plain encrypts to the encrypted
       text enc"""
	return enc == crypt.crypt(plain, enc[:2])

def load_passwd(filename):
	"""Load the password file filename and returns a list of
       dictionaries with fields "account", "password", "UID", "GID",
       "GECOS", "directory", and "shell", each mapping to the
       corresponding field of the file."""
	accounts = list()
	with open(filename, 'r') as fd:
		regex = re.compile(r"^(?P<account>[a-z0-9_]+):(?P<password>[./a-zA-Z0-9]+):(?P<UID>\d+):(?P<GID>\d+):(?P<GECOS>[^:\n]*):(?P<directory>[^:\n]+):(?P<shell>[^:\n]*)$")
		for line in fd:
			match = regex.search(line.strip())
			if match:
				account = dict()
				account['account'] = match.group('account')
				account['password'] = match.group('password')
				account['UID'] = int(match.group('UID'))
				account['GID'] = int(match.group('GID'))
				account['GECOS'] = match.group('GECOS')
				account['directory'] = match.group('directory')
				account['shell'] = match.group('shell')
				accounts.append(account)
	return accounts

def crack_pass_file(fn_pass,fn_words,fn_out):
	"""Crack as many passwords in file fn_pass as possible using words
       in the file words"""
	words = load_words(fn_words, r"^.{6,8}$")
	accounts = load_passwd(fn_pass)
	with open(fn_out, 'w', 0) as out:
		for word in words:
			for passwd in transform_reverse(word):
				for account in list(accounts):
					if check_pass(passwd, account['password']):
						out.write(''.join([account['account'],'=',passwd,'\n']))
						# print("Cracked: " + account['account'])
						accounts.remove(account)
		# print("Simple passwords cracked")
		# print("Uncracked accounts: " + str(len(accounts)))
		if accounts:
			for word in words:
				# print("Current word: " + word)
				for word2 in transform_reverse(word):
					for passwd in transform_digits(word2)[1:]:
						for account in list(accounts):
							if check_pass(passwd, account['password']):
								out.write(''.join([account['account'],'=',passwd,'\n']))
								# print("Cracked: " + account['account'])
								accounts.remove(account)
		# print("Digit transformed passwords cracked")
		# print("Uncracked accounts: " + str(len(accounts)))
		if accounts:
			for word in words:
				# print("Current word: " + word)
				for word2 in transform_reverse(word):
					for passwd in transform_capitalize(word2)[1:]:
						for account in list(accounts):
							if check_pass(passwd, account['password']):
								out.write(''.join([account['account'],'=',passwd,'\n']))
								# print("Cracked: " + account['account'])
								accounts.remove(account)
		# print("Capitalization transformed passwords cracked")
		# print("Uncracked accounts: " + str(len(accounts)))
		if accounts:
			for word in words:
				# print("Current word: " + word)
				for word2 in transform_reverse(word):
					for word3 in transform_digits(word2)[1:]:
						for passwd in transform_capitalize(word3)[1:]:
							for account in list(accounts):
								if check_pass(passwd, account['password']):
									out.write(''.join([account['account'],'=',passwd,'\n']))
									# print("Cracked: " + account['account'])
									accounts.remove(account)
		# print("Nested transformed passwords cracked")
		# print("Uncracked accounts: " + str(len(accounts)))
