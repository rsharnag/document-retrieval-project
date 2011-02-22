# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jyotesh"
__date__ ="$21 Feb, 2011 5:17:33 PM$"

import hasher
from math import log

class FreqCounter:
    def __init__(self):
        self.freq_table = {}
        self.hash = hasher.Hasher()
        self.count_table = self.hash.hash_table

    def tfidf(self):
        """calculates term frequency-inverse document frequency"""
        documents_count = len(self.hash.map_count)
        for word in self.count_table.keys():
            #documents_per_word contains number of documents which contain the current word
            #index 0-nouns, 1-verbs, 2-adjectives, 3-adverbs
            documents_per_word=[0,0,0,0]
            for element in self.count_table[word]:
                documents_per_word[element[2]] += 1
            for element in self.count_table[word]:
                file_index = element[0]
                word_count = element[1]
                tag = element[2]
                filename = self.hash.map_count[file_index]
                total_words = self.hash.word_count[filename]
                freq = (float(word_count) / total_words) * log(float(documents_count) / documents_per_word[tag])
                if self.freq_table.has_key(word):
                    self.freq_table[word].extend([file_index,freq,tag])
                else:
                    self.freq_table[word] = [file_index,freq,tag]

if __name__ == "__main__":
    freq_count = FreqCounter()
    print freq_count.freq_table
