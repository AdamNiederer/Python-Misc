#!/usr/bin/python3

import markovify

# Author: Joshua Li
# Description:
# 	Just testing out the markovify module to generate
#	text using Markov chains trained on text corpora.
#	Text data ("MASC 3.0.0") was obtained from 
#	http://www.anc.org/data/masc/downloads/data-download/

# Markovify: https://github.com/jsvine/markovify
# It's highly extensible, but I will just be testing some methods
# for now.

'''
Borrowed code from https://github.com/jsvine/markovify/blob/master/README.md
to test out nltk pos integration w/ markovify
'''
import nltk
import re

class POSifiedText(markovify.Text): # POS means part of speech
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence
'''
End borrowed code
'''

if __name__ == "__main__":

	with open("data/masc_500k_texts/written/technical/1471-2091-2-9.txt") as f:
		text = f.read().strip()
		#print(text)
		#print(markovify.splitters.split_into_sentences(text))

	#test = markovify.Text(text)
	#print(test.rejoined_text)
	#print(test.rejoined_text.replace("||", ""))
	#exit()

	model = markovify.Text(text)
	#model = POSifiedText(text) # Doesn't exactly work yet
	for i in range(10):
		print()
		#print(model.make_sentence(tries=100))
		print(model.make_short_sentence(140))