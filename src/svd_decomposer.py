# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jyotesh"
__date__ ="$21 Feb, 2011 5:17:33 PM$"

import hasher
from math import log
import numpy

class svdDecompose:
    """

    """
    def __init__(self):
        #freq_table contains the frequency for each word-tag pair
        self.freq_table = []
        #word_index_per_tag contains word-tag pair for each index
        self.word_index_per_tag = []
        self.hash = hasher.Hasher()
        self.hash.read_dump()

    def tfidf(self,wordlist):
        """calculates term frequency-inverse document frequency"""
        documents_count = len(self.hash.map_count)
        for word in wordlist:
            #documents_per_word contains number of documents which contain the current word
            #index 0-nouns, 1-verbs, 2-adjectives, 3-adverbs
            if(not(self.hash.hash_table.has_key(word))):
                continue
            documents_per_word=[0,0,0,0]
            for element in self.hash.hash_table[word]:
                documents_per_word[element[2]] += 1
            for tag in range(0,4):
                #freq_list contains frequencies for each word-tag pair per file
                freq_list = documents_count*[0.0]
                tag_present = 0
                for element in self.hash.hash_table[word]:
                    if tag == element[2]:
                        tag_present = 1
                        file_index = element[0]
                        word_count = element[1]
                        filename = self.hash.map_count[file_index]
                        total_words = self.hash.word_count[filename]
                        freq = (float(word_count) / total_words) * log(float(documents_count) / documents_per_word[tag])
                        freq_list[file_index] = freq
                if tag_present == 1:
                    self.word_index_per_tag.append([word,tag])
                    self.freq_table.append(freq_list)
        """for i in range(0,len(self.word_index_per_tag)):
		print "word = ",self.word_index_per_tag[i][0],", tag = ",self.word_index_per_tag[i][1],", frequency = ",self.freq_table[i]"""
    def decompose(self):
        self.U,self.S,self.V = numpy.linalg.svd(self.freq_table)

    def find_neighbours(self):
        return
if __name__ == "__main__":
    
    freq_count = svdDecompose()
    wordlist=["conceptualize","disciplines","copenhagen","appear","invented","boolean","successful"]
    freq_count.tfidf(wordlist)
    freq_count.decompose()
    open("output","w").write( str(freq_count.U)+"\n"+str(freq_count.V))
    
