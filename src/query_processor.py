# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="aditya"
__date__ ="$27 Jan, 2011 11:09:18 PM$"

#import nltk

import tagger
import generalisation
import svd_decomposer
class DocProcessor:

    def __init__(self,hash):
       self.taggerinst = tagger.Tagger(False)
       self.generalizedWordList=[]
       self.hash=hash

    def process(self, filename = "taggerText", numOfResult=10):
        wordlist = self.taggerinst.classify(filename)
        type = 0
        while type <= 3:
            self.generalizedWordList.extend(generalisation.generalisation(wordlist[type]))
            type+=1
        decomposer=svd_decomposer.svdDecompose(self.hash)
        decomposer.tfidf(self.generalizedWordList)
        decomposer.decompose()
        self.results=decomposer.find_neighbours(numOfResult)
        for i in self.results:
            print self.hash.map_count[i]
        return self.results

if(__name__=="__main__"):
    from hasher import Hasher
    hash=Hasher()
    hash.read_dump()
    doc_processor = DocProcessor(hash)
    doc_processor.process()
    open("output_TFIDF","w").write(" ")
    print "Finished"
