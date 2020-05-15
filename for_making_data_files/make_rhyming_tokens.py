# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:55:21 2020

@author: Doug
"""

import pickle
from collections import defaultdict

rhyming_tokens = defaultdict(set)
syllable_tokens = [set() for y in range(10)]
for word in rhyme_dictionary:
    rhyme_part = rhyme_dictionary[word]
    rhyming_words = reverse_rhyme_dictionary[rhyme_part]
    for rhyming_word in rhyming_words:
        these_rhyming_tokens=tokenizer.encode(rhyming_word,add_prefix_space = True)
        rhyming_tokens[word] = rhyming_tokens[word].union(set(these_rhyming_tokens))
    word_tokens=tokenizer.encode(word,add_prefix_space = True)
    syll_count = min(syllable_count_dictionary[word.upper()],9)
    syllable_tokens[syll_count] = syllable_tokens[syll_count].union(word_tokens)

 for word in rhyme_dictionary:  
    rhyme_part = rhyme_dictionary[word]
    rhyming_words = reverse_rhyme_dictionary[rhyme_part]
    for rhyming_word in rhyming_words:
        these_rhyming_tokens=tokenizer.encode(rhyming_word.capitalize(),add_prefix_space = True)
        rhyming_tokens[word] = rhyming_tokens[word].union(set(these_rhyming_tokens))    
    word_tokens=tokenizer.encode(word.capitalize(),add_prefix_space = True)
    syll_count = min(syllable_count_dictionary[word.upper()],9)
    syllable_tokens[syll_count] = syllable_tokens[syll_count].union(word_tokens)
    
with open("rhyming_tokens.p","wb") as f:
    pickle.dump(rhyming_tokens, f)
with open("syllable_tokens.p","wb") as f:
    pickle.dump(syllable_tokens, f)