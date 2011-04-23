# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="aditya & rahul"
__date__ ="$26 Jan, 2011 4:13:20 PM$"

from nltk.corpus import wordnet as wn
def createSynsetDict(wordList):
    """Creates a dictionary of synonyms of given wordlist"""
    synWords={}
    for word in wordList:
        synWords[word] = wn.synsets(word)
    return synWords

def generalisation(originalWordList):
    generalisedWordList=[]
    currentWordList = originalWordList
    synWords = createSynsetDict(originalWordList)
    while(len(currentWordList)>=2):
        generalizedWords = [[],[],[]]
        #currShortest_Dist = 2
        currentWord = currentWordList.pop()
        generalisedWordList.extend([currentWord])
        for otherWord in currentWordList:
            for currentWordSyn in synWords[currentWord]:
                for ithWordSyn in synWords[otherWord]:
                    short_dist = ithWordSyn.shortest_path_distance(currentWordSyn)
                    #print short_dist
                    if (short_dist != None and short_dist <= 2):
                        generalizedWords[short_dist] = generalizedWords[short_dist] + ithWordSyn.common_hypernyms(currentWordSyn)
        l=[]
        if(len(generalizedWords[0])!= 0):
            currentWordList.remove(otherWord)
            generalisedWordList.extend([otherWord])
            for syns in generalizedWords[0]:
                l.extend(syns.lemma_names)
        elif (len(generalizedWords[1])!= 0):
            currentWordList.remove(otherWord)
            generalisedWordList.extend([otherWord])
            for syns in generalizedWords[1]:
                l.extend(syns.lemma_names)
        elif (len(generalizedWords[2])!= 0):
            currentWordList.remove(otherWord)
            generalisedWordList.extend([otherWord])
            for syns in generalizedWords[2]:
                l.extend(syns.lemma_names)
        generalisedWordList.extend(l)
    generalisedWordList.extend(currentWordList)
    generalisedWordList=list(set(generalisedWordList))
    open("output_generalizedWL","a").write(str(generalisedWordList))
    return generalisedWordList

if __name__ == "__main__":
    generalisation(['cell', 'anatomy', 'biology', 'knowledge', 'chromosome'])
