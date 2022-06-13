# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):

	if(len(word) == len(anagram)):
		
		sorted_word = sorted(word)
		sorted_anagram = sorted(anagram)

		if(sorted_word == sorted_anagram):
			print(word + " and " + anagram + " are anagram.")
			return True
		else:
			print(word + " and " + anagram + " are not anagram.")
			return False

	else:
		print(word + " and " + anagram + " are not anagram.")
		return False

find_anagram("below", "elbosw")

