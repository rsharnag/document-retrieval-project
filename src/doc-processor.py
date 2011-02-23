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
       self.decomposer=svdDecompose()
       self.hash=hash
    def process(self, filename = "taggerText"):
        wordlist = self.taggerinst.classify(filename)
        type = 0
        while type <= 3:
            self.generalizedWordList.extend(generalisation.generalisation(wordlist[type]))
            type+=1
        decomposer=svdDecompose(self.hash)
        decomposer.tfidf(self.generalizedWordList)
        decomposer.decompose()
        self.results=decomposer.find_neighbours()


doc_processor = DocProcessor()
doc_processor.process()
print "Finished"