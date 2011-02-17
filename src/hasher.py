# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="codepoet"
__date__ ="$16 Feb, 2011 3:45:26 PM$"

import tagger
import pickle
import os
import glob

class Hasher:
    """
        Hasher class to create hash table ,dumping it to file on disk ,append file to hash table
    """
    def __init__(self):
            self.word_count={}
            self.hash_table={}
            self.map_file={}
            self.map_count={}

     # removes all punctions from text
    def remove_puncs(self,string):
            stripped_text=""
            for c in string:
                    if c in '!,.()[]{}\n':
                            c=""
                    stripped_text+=c
            return stripped_text

    def create_dump(self):
        count_file=0
        for infile in glob.glob(os.path.join(os.curdir,"*.txt")):
            count = len(open(infile).read().split())
            self.word_count[infile] = count
            self.map_count[count_file]=infile
            self.map_file[infile]=count_file
            count_file=count_file+1
            self.hash_words(infile)
        self.write_dump()
    def write_dump(self):
        f1=open('hash_dump','w')
        f2=open('word_count_dump','w')
        f3=open('file_map_dump','w')
        f4=open('file_id_dump','w')
        pickle.dump(self.hash_table,f1)
        pickle.dump(self.word_count,f2)
        pickle.dump(self.map_file,f3)
        pickle.dump(self.map_count,f4)
        f1.close()
        f2.close()
        f3.close()
        f4.close()
    def read_dump(self):
        try:
            f1=open('hash_dump','r')
            f2=open('word_count_dump','r')
            f3=open('file_map_dump','r')
            f4=open('file_id_dump','r')
        except IOError:
            print "Dump file not found"
            exit(1)
        self.hash_table = pickle.load(f1)
        f1.close()
        self.word_count = pickle.load(f2)
        f2.close()
        self.map_file = pickle.load(f3)
        f3.close()
        self.map_count = pickle.load(f4)
        f4.close()
    def append_dump(self,filename):
        self.read_dump()
        if(len(self.map_count.keys())==0):
            count_file=0
        else:
            count_file=max(self.map_count.keys())
        self.map_file[filename]=count_file
        self.map_count[count_file]=filename
        self.hash_words(filename)
        self.write_dump()


    def hash_words(self,path):
        t=tagger.Tagger()
        t.classify(path,False)
        for word in t.nouns:
            self.hash_table[word.lower()]=(self.map_file[path],t.nouns.count(word))
        for word in t.verbs:
            self.hash_table[word.lower()]=(self.map_file[path],t.verbs.count(word))
        for word in t.adjectives:
            self.hash_table[word.lower()]=(self.map_file[path],t.adjectives.count(word))
        for word in t.adverbs:
            self.hash_table[word.lower()]=(self.map_file[path],t.adverbs.count(word))

if __name__=="__main__":
    hash= Hasher()
    hash.append_dump(".\\sample.txt")
    

