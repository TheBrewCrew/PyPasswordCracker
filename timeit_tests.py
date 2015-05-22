timeit.timeit('apply_transforms("aviatic")','from crack import apply_transforms', number=10000)
timeit.timeit('check_pass("aviatic","VgzdTLne0kfs6")','from crack import check_pass', number=10000)
timeit.timeit('list(accounts)',"accounts=[{'account': 'root', 'shell': '/bin/bash', 'UID': 0, 'GID': 0, 'GECOS': 'Corema Latterll', 'directory': '/home/root', 'password': 'VgzdTLne0kfs6'}, {'account': 'checani', 'shell': '/bin/bash', 'UID': 1, 'GID': 1, 'GECOS': 'Pengpu Checani', 'directory': '/home/checani', 'password': 'IqAFDoIjL2cDs'}, {'account': 'rkrakow', 'shell': '/bin/bash', 'UID': 2, 'GID': 2, 'GECOS': 'Rodentia Krakow', 'directory': '/home/rkrakow', 'password': 'DLD3nJmCvt3pY'}, {'account': 'forkland', 'shell': '/bin/bash', 'UID': 3, 'GID': 3, 'GECOS': 'Forkland Maskins', 'directory': '/home/forkland', 'password': 'oWMVyy1FTdNL6'}, {'account': 'obongo', 'shell': '/bin/bash', 'UID': 4, 'GID': 4, 'GECOS': 'Obongo Obwalden', 'directory': '/home/obongo', 'password': 'O44lPEloqk5tY'}, {'account': 'pglenda', 'shell': '/bin/bash', 'UID': 5, 'GID': 5, 'GECOS': 'Pahsien Glenda', 'directory': '/home/pglenda', 'password': 'xboW5dHcsqvSQ'}, {'account': 'madel', 'shell': '/bin/bash', 'UID': 6, 'GID': 6, 'GECOS': 'Madel Aporosa', 'directory': '/home/madel', 'password': 'qEHvJXMkTSAZA'}, {'account': 'ssauks', 'shell': '/bin/bash', 'UID': 7, 'GID': 7, 'GECOS': 'Schober Sauks', 'directory': '/home/ssauks', 'password': 'Q3Kz1z7eAiwjg'}, {'account': 'slajoie', 'shell': '/bin/bash', 'UID': 8, 'GID': 8, 'GECOS': 'Scheiner Lajoie', 'directory': '/home/slajoie', 'password': 'wWTHgoE8SC8W6'}, {'account': 'tieton', 'shell': '/bin/bash', 'UID': 9, 'GID': 9, 'GECOS': 'Lerwa Tieton', 'directory': '/home/tieton', 'password': 'RWORYLxRSSzMU'}]", number=10000)
timeit.timeit('print("Current word: " + word)','word="test"', number=10000)
def dup_detect(l):
	cnt = dict()
	for word in l:
		if word in cnt:
			cnt[word] += 1
			print("duplicate word: " + word)
		else:
			cnt[word] = 1
	return cnt
def apply_transforms(word):
	for w2 in transform_digits(word):
		for w3 in transform_capitalize(w2):
			yield w3
def apply_transforms2(word):
	for w in transform_digits(word):
		yield w
	for w in transform_capitalize(word):
		yield w
def apply_transforms3(word):
	for w2 in transform_digits(word)[1:]:
		for w3 in transform_capitalize(w2)[1:]:
			yield w3
dup_detect(list(apply_transforms('abounded')))