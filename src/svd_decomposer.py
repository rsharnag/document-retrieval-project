# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jyotesh"
__date__ ="$21 Feb, 2011 5:17:33 PM$"

import hasher
import tagger
import generalisation
from math import log
import numpy
from kdtree import KDTree

class svdDecompose:
    """

    """
    def __init__(self, hash_table):
        #freq_table contains the frequency for each word-tag pair
        self.freq_table = []
        #word_index_per_tag contains word-tag pair for each index
        self.word_index_per_tag = []
        self.hash = hash_table
        self.U=[]
        self.V=[]

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
                    open("output_TFIDF","a").write(str(word)+"\n")
                    self.word_index_per_tag.append([word,tag])
                    self.freq_table.append(freq_list)
        open("output_TFIDF","a").write(str(self.freq_table))
        """for i in range(0,len(self.word_index_per_tag)):
		print "word = ",self.word_index_per_tag[i][0],", tag = ",self.word_index_per_tag[i][1],", frequency = ",self.freq_table[i]"""

    def decompose(self):
        u,s,v = numpy.linalg.svd(self.freq_table)
        #print u
        #print v
        temp=[]
        for i in range(0,len(u)):
            for j in range(0,len(u[0])):
                temp.append(float(u[i][j]))
            self.U.append(temp)
            temp=[]
        for i in range(0,len(v)):
            for j in range(0,len(v[0])):
                temp.append(float(v[i][j]))
            self.V.append(temp)
            temp=[]
        #print self.U
        #print self.V
        i = 0
        if(len(self.U[0])<len(self.V[0])):
            temp = (len(self.V[0])-len(self.U[0]))*[0.0]
            for i in range(0,len(self.U)):
                self.U[i].extend(temp)
        elif(len(self.U[0])>len(self.V[0])):
            i = (len(self.U[0])-len(self.V[0]))
            while(i > 0):
                self.V.append(len(self.V[0])*[0.0])
                i -= 1
        open("output_SVD","w").write(str(self.V)) #+ "\n" + str(self.V))

    def find_neighbours(self, num_of_results=5):
        """Build a k-D Tree and find the nearnest neighbours of the given query"""
        data = []
        point_list = []
        nearest = []
        DataToDoc_map = {}
        count = {}
        FinalResult = []
        #create a Data Set for building k-D Tree
        i = 0
        while(i < len(self.V[0])): #len(V[i]) == len(V[0])
            j=1
            temp = []
            while(j < len(self.V)):
                temp.append(self.V[j][i])
                j+=1
            DataToDoc_map[tuple(temp)] = i
            i+=1
            data.append(temp)
        #print DataToDoc_map
        tree = KDTree.construct_from_data(data)
        #Points for which the nearest neighbours has to be found
        i=0
        while(i < len(self.U)):
            point_list.append(self.U[i][1:])
            i += 1
        i = 0
        while(i < len(point_list)):
            nearest = tree.query(point_list[i], t=num_of_results) # find nearest t points to the current point
            j = 0
            while(j < len(nearest)):
                t = DataToDoc_map[tuple(nearest[j])]
                if t in count:
                    count[t] += float((num_of_results-j))/float(num_of_results)
                else:
                    count[t] = float((num_of_results-j))/float(num_of_results)
                j += 1
            i += 1
        FinalResult = sorted(count, key=count.__getitem__, reverse=True)
        for i in count.keys():
            open("output_Count","a").write(str(i)+" "+str(count[i])+"\n")
        return FinalResult[:num_of_results]
    
if __name__ == "__main__":
    result = []
    hash_table = hasher.Hasher()
    hash_table.read_dump()
    taggerinst = tagger.Tagger(False)
    wordlist = taggerinst.classify("taggerText")
    generalizedWordList = []
    type = 0
    while type <= 3:
        generalizedWordList.extend(generalisation.generalisation(wordlist[type]))
        type+=1
    decomposer=svdDecompose(hash_table)
    decomposer.tfidf(generalizedWordList)
#    wordlist=["conceptualize","disciplines","copenhagen","appear","invented","boolean","successful"]
#    freq_count.tfidf(wordlist)
#    freq_count.decompose()
#    result = freq_count.find_neighbours()
#    open("output","w").write( str(freq_count.U)+"\n\n\n"+str(freq_count.V))
