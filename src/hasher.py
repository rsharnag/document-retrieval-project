# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="codepoet"
__date__ ="$16 Feb, 2011 3:45:26 PM$"

import tagger
import pickle
import os
import glob


if __name__ == "__main__":
    print "Hello World"

class LSI:
        def __init__(self):
                self.word_count={}
                self.hash_table={}

         # removes all punctions from text
        def remove_puncs(self,string):
                stripped_text=""
                for c in string:
                        if c in '!,.()[]{}\n':
                                c=""
                        stripped_text+=c
                return stripped_text

        def create_dump(self):
            for infile in glob.glob(os.path.join(path, '*.txt') ):
                count = open(infile).read().split().size()
                self.word_count[infile] = count
                count_file=count_file+1
                hash_words(infile)
            f1=open('hash_dump','w')
            f2=open('word_count_dump','w')
            pickle.dump(self.hash_table,f1)
            pickle.dump(self.word_count,f2)
            f1.close()
            f2.close()

        def read_dump(self):
            f=open('hash_dump','r')
            self.hash_table = pickle.load(f)

            
        def append_dump(self,filename):
            read_dump()
            hash_words(filename)
            f=open('hash_dump','w')
            pickle.dump(self.hash_table,f)
            f.close()


        def hash_words(self,path):
            t=tagger.Tagger()
            t.classify(path,False)
            for word in t.nouns:
                hash_table[word.lower()]=(path,t.nouns.count(word))
            for word in t.verbs:
                hash_table[word.lower()]=(path,t.verbs.count(word))
            for word in t.adjectives:
                hash_table[word.lower()]=(path,t.adjectives.count(word))
            for word in t.adverbs:
                hash_table[word.lower()]=(path,t.adverbs.count(word))




