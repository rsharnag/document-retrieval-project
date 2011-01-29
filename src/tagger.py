import nltk
import nltk.tag
import nltk.tokenize
import text
import time
# To change this template, choose Tools | Templates
# and open the template in the editor
__author__="aditya"
__date__ ="$22 Jan, 2011 12:11:31 PM$"

class Tagger:
    def __init__(self, debug=False):
        self._noun_type = ["NN","NNS","NNP","NNPS"]
        self._verb_type = ["VB","VBD","VBG","VBN","VBZ","VBP"]
        self._adjective_type = ["JJ","JJR","JJS"] 
        self._adverb_type = ["RB","RBR","RBS"]
        self.debug=debug

    def classify(self, filename):
        wordlist = [] #return var having a list of tokens tagged as <noun><adjective><verb><adverb>
        taggerText=text.ReadText(filename)
        tokens = nltk.tokenize.word_tokenize(taggerText.readAll)
        tags= nltk.tag.pos_tag(tokens)
        self.nouns = []
        self.adjectives = []
        self.adverbs = []
        self.verbs = []
        #print tags
        for tag in tags:
            if tag[1] in self._noun_type:
                self.nouns.append(tag[0])
            elif tag[1] in self._adjective_type:
                self.adjectives.append(tag[0])
            elif tag[1] in self._verb_type:
                self.verbs.append(tag[0])
            elif tag[1] in self._adverb_type:
                self.adverbs.append(tag[0])
            
        #Remove multiple entries
        if(self.debug):stime=time.time()
        self.nouns=list(set(self.nouns))
        wordlist.append(self.nouns)
        self.adjectives=list(set(self.adjectives))
        wordlist.append(self.adjectives)
        self.verbs=list(set(self.verbs))
        wordlist.append(self.verbs)
        self.adverbs=list(set(self.adverbs))
        wordlist.append(self.adverbs)
        if self.debug:
            print time.time()-stime
            print len(taggerText.readAll)
            print self.nouns
            print len(self.nouns)
            print self.adjectives
            print len(self.adjectives)
            print self.adverbs
            print len(self.adverbs)
            print self.verbs
            print len(self.verbs)
        return wordlist
