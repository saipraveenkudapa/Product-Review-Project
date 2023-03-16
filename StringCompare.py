# Python code showing all the ratios together, 
# make sure you have installed fuzzywuzzy module 
"""
pip install fuzzywuzzy
pip install python-Levenshtein
"""
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
class StringCompare:
	
	def do(s1, s2):
		d=fuzz.token_sort_ratio(s1, s2)
		
		#print ("FuzzyWuzzy PartialRatio: ",  d)
		return float(d)
		
if __name__ == '__main__':
	StringCompare.do("sajid sajid sajid sajid nashu nashu chantu","sajid")
