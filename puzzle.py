import itertools
import enchant
import sys
import string

def main(argv):
	given_word = argv[0].lower()
	word_length = int(argv[1])
	existing_alphabet_list = list(given_word)
	dictionary = enchant.Dict("en_US")
	alphabet_string = string.ascii_lowercase
	all_alphabets_list = list(alphabet_string)
	all_positions_list = list(range(word_length))
	result = []
	position_combinations = itertools.combinations(all_positions_list, word_length - len(given_word))
	for p in position_combinations:
		for a in all_alphabets_list:
			string_list = ['$']*word_length
			for pos in p:
				string_list[pos] = a
			ptr = 0
			ptr_list = 0
			while(ptr_list < word_length):
				if((string_list[ptr_list])=='$'):
					string_list[ptr_list] = given_word[ptr]
					ptr+=1
				ptr_list+=1
			if(dictionary.check(''.join(string_list))):
				result.append(''.join(string_list))
	print(result)

"""usage - python3 puzzle.py voeyba 10 -> volleyball"""
if __name__ == "__main__":
     main(sys.argv[1:])