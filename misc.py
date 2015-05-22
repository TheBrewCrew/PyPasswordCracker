#PA 4
import re

"Miscellaneous functions to practice Python"

class Failure(Exception):
    """Failure exception"""
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

# Problem 1

# data type functions

def closest_to(l,v):
	"""Return the element of the list l closest in value to v.  In the case of
       a tie, the first such element is returned.  If l is empty, None is returned."""
	if not l:
		return None
	closest = l[0]
	diff = abs(v - l[0])
	for x in l:
		if diff > abs(v - x):
			closest = x
			diff = abs(v - x)
	return closest

def make_dict(keys,values):
    """Return a dictionary pairing corresponding keys to values."""
    return {key: value for key, value in map(None, keys, values)}
   
# file IO functions
def word_count(fn):
	"""Open the file fn and return a dictionary mapping words to the number
       of times they occur in the file.  A word is defined as a sequence of
       alphanumeric characters and _.  All spaces and punctuation are ignored.
       Words are returned in lower case"""
	cnt = dict()
	with open(fn, 'r') as fd:
		for word in re.split('\W+', fd.read()):
			w = word.lower()
			if w in cnt:
				cnt[w] += 1
			else:
				cnt[w] = 1
	del cnt['']
	return cnt
