# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="codepoet"
__date__ ="$16 Feb, 2011 3:45:26 PM$"

import sys
import tagger
try:
    import cPickle as pickle
except ImportError:
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
        if(sys.platform=="nt"):
            path=os.curdir+"\\text\\"
        else:
            path=os.curdir+"/text/"
        for infile in glob.glob(os.path.join(path,"*.txt")):
            count = len(open(infile).read().split())
            self.word_count[infile] = count
            self.map_count[count_file]=infile
            self.map_file[infile]=count_file
            count_file=count_file+1
            self.hash_words(infile)
        self.write_dump()
    def write_dump(self):

        if(sys.platform=="nt"):
            path=os.curdir+"\\dumps\\"
        else:
            path=os.curdir+"/dumps/"
        d = os.path.dirname(path)
        if not os.path.exists(d):
            os.makedirs(d)
        try:
            f1=open(path+'hash_dump','w')
            f2=open(path+'word_count_dump','w')
            f3=open(path+'file_map_dump','w')
            f4=open(path+'file_id_dump','w')
        except:
            print "Cannot create dump file"
            exit(1)
        pickle.dump(self.hash_table,f1)
        pickle.dump(self.word_count,f2)
        pickle.dump(self.map_file,f3)
        pickle.dump(self.map_count,f4)
        f1.close()
        f2.close()
        f3.close()
        f4.close()
    def read_dump(self):
        if(sys.platform=="nt"):
            path=os.curdir+"\\dumps\\"
        else:
            path=os.curdir+"/dumps/"
        
        try:
            f1=open(path+'hash_dump','r')
            f2=open(path+'word_count_dump','r')
            f3=open(path+'file_map_dump','r')
            f4=open(path+'file_id_dump','r')
        except IOError:
            print "Dump file not found, creating new dump"
            return
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
        for word in list(set(t.nouns)):
            if(self.hash_table.has_key(word.lower())):
                self.hash_table[word.lower()].extend([(self.map_file[path],t.nouns.count(word),0)])
            else:
                self.hash_table[word.lower()]=[(self.map_file[path],t.nouns.count(word),0)]

        for word in list(set(t.verbs)):
            if(self.hash_table.has_key(word.lower())):
                self.hash_table[word.lower()].extend([(self.map_file[path],t.verbs.count(word),1)])
            else:
                self.hash_table[word.lower()]=[(self.map_file[path],t.verbs.count(word),1)]
        for word in list(set(t.adjectives)):
            if(self.hash_table.has_key(word.lower())):
                self.hash_table[word.lower()].extend([(self.map_file[path],t.adjectives.count(word),2)])
            else:
                self.hash_table[word.lower()]=[(self.map_file[path],t.adjectives.count(word),2)]
        for word in list(set(t.adverbs)):
            if(self.hash_table.has_key(word.lower())):
                self.hash_table[word.lower()].extend([(self.map_file[path],t.adverbs.count(word),3)])
            else:
                self.hash_table[word.lower()]=[(self.map_file[path],t.adverbs.count(word),3)]

if __name__=="__main__":
    hash= Hasher()
    hash.create_dump()
    #print hash.hash_table
    #pass

