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

        # removes all punctions from text
        def remove_puncs(self,string):
                stripped_text=""
                for c in string:
                        if c in '!,.()[]{}\n':
                                c=""
                        stripped_text+=c
                return stripped_text

        # searches for query words in documents. returns the name of file in which the word is found and its frequency
        # identifier 'matrix' holds the frequency of words in documents, in which rows represents words and columns represents documents, whose order is
        # specified in dump file 'documents'
        def hash_search(self,path,list):
                query_words=list
                count_file=0
                for infile in glob.glob(os.path.join(path, '*.txt') ):
                        count_file=count_file+1
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
                        # uncomment to view entire output
                        #print qw
                        #print self.hash_table[qw]
                #print matrix
                return matrix
                        
t0=time.time()
query_nouns=['research','nature','scientific','finibus','literature','renaissance','primary','problem','programmer','program']
query_verbs=['interpreting','discovering','publishing','facing','decisions','compared','appeared','looking','wondering','announced','beginning']
query_adverbs=['wide','sometimes','long','significant','moment','exactly','pitifully','properly','slightly','galley']
query_adjectives=['complete','provides','popular','final','several','exact']

lsi=LSI()

count=0
path=os.getcwd()
docs=[]
for infile in glob.glob(os.path.join(path, '*.txt')):
        docs.append(os.path.basename(infile))     
f=open('output_documents','w')
pickle.dump(docs,f)

f=open('output_nouns','w')
pickle.dump(lsi.hash_search(path,query_nouns),f)

f=open('output_verbs','w')
pickle.dump(lsi.hash_search(path,query_verbs),f)

f=open('output_adverbs','w')
pickle.dump(lsi.hash_search(path,query_adverbs),f)

f=open('output_adject','w')
pickle.dump(lsi.hash_search(path,query_adjectives),f)
f.close()

print "Execution Time"
print time.time()-t0, "Seconds"
