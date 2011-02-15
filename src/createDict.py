#__author__="ankit tare"
#__date__ ="$12 feb, 2011 1:56:11 PM$"

import os
import glob
import sys
import time
import pickle

class LSI:
        hash_table={}
        def __init__(self):
                self.data=[]

        def remove_puncs(self,string):
                stripped_text=""
                for c in string:
                        if c in '!,.()[]{}\n':
                                c=""
                        stripped_text+=c
                return stripped_text

        def hash_search(self,path,list):
                query_words=list
                for infile in glob.glob(os.path.join(path, '*.txt') ):
                        f=open(infile)
                        str=f.read()
                        str=str.lower()
                        str=self.remove_puncs(str)
                        words=str.split(" ")
                        i=0
                        for qw in query_words:
                                self.hash_table.setdefault(query_words[i], []).append(os.path.basename(infile))
                                self.hash_table.setdefault(query_words[i], []).append(words.count(qw))
                                i=i+1
                        
        def build_matrix(self,path,list,count):
                query_words=list
                count_file=count;
                matrix=[]
                for qw in query_words:
                        temp=[]
                        i=0
                        tel=self.hash_table[qw]
                        while i<2*count_file:
                                temp.append(tel[i+1])
                                i=i+2
                        matrix.append(temp)
                        del temp
                return matrix
                        
t0=time.time()
query_nouns=['research','nature','scientific','finibus','literature','renaissance','primary','problem','programmer','program']
query_verbs=['interpreting','discovering','publishing','facing','decisions']
query_adverbs=['wide','sometimes','long','significant','moment']
query_adjectives=['complete','provides','popular','final']

lsi=LSI()
lsi.hash_search(os.getcwd(),query_nouns)
lsi.hash_search(os.getcwd(),query_verbs)
lsi.hash_search(os.getcwd(),query_adverbs)
lsi.hash_search(os.getcwd(),query_adjectives)

count=0
path=os.getcwd()
docs=[]
for infile in glob.glob(os.path.join(path, '*.txt')):
                       count=count+1 
                       docs.append(os.path.basename(infile))
f=open('documents','w')
pickle.dump(docs,f)

f=open('output_nouns','w')
pickle.dump(lsi.build_matrix(path,query_nouns,count),f)

f=open('output_verbs','w')
pickle.dump(lsi.build_matrix(path,query_verbs,count),f)
print lsi.build_matrix(path,query_verbs,count)

f=open('output_adverbs','w')
pickle.dump(lsi.build_matrix(path,query_adverbs,count),f)

f=open('output_adjectives','w')
print lsi.build_matrix(path,query_adjectives,count)
pickle.dump(lsi.build_matrix(path,query_adjectives,count),f)

print "Execution Time"
print time.time()-t0, "Seconds"
