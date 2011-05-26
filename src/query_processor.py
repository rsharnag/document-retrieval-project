# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="aditya"
__date__ ="$27 Jan, 2011 11:09:18 PM$"

#import nltk

import tagger
import  os
import generalisation
import svd_decomposer
try:
    import cPickle as pickle
except ImportError:
    import pickle
class DocProcessor:

    def __init__(self,hash):
       self._taggerinst = tagger.Tagger(False)
       self._generalizedWordList=[]
       self._hash=hash
    def process(self, filename = "taggerText", numOfResult=10):
        self._wordlist = self._taggerinst.classify(filename)
        self.dumpList("taggerResult")
        wordlist=[]
        for i in range(0, 4):
            wordlist=wordlist+self._wordlist[i]
        type = 0
        while type <= 1:
            self._generalizedWordList.extend(generalisation.generalisation(self._wordlist[type]))
            type+=1
        
        self._generalisedWords=list(set(self._generalizedWordList)-set(wordlist))
        self.dumpList("generalisedWords")
        decomposer=svd_decomposer.svdDecompose(self._hash)
        decomposer.tfidf(self._generalizedWordList)
        decomposer.decompose()
        self._results=decomposer.find_neighbours(numOfResult)
        for i in self._results:
            print self._hash.map_count[i]
        return self._results
    def dumpList(self, type):
        if(type=="taggerResult"):
            try:
                file=open(os.curdir+"/dumps/tagger_dump", "w")
                pickle.dump(self._wordlist, file)
                file.close()
            except:
                print 'cant create tagger dump file'
                return
        elif(type=="generalisedWords"):
            try:
                file=open(os.curdir+"/dumps/GW_dump", "w")
                pickle.dump(self._generalisedWords, file)
                file.close()
            except:
                print 'cant create tagger dump file'
                return
            
    
if(__name__=="__main__"):
    from hasher import Hasher
    hash=Hasher()
    hash.read_dump()
    doc_processor = DocProcessor(hash)
    doc_processor.process()
    open("output_TFIDF","w").write(" ")
    print "Finished"
