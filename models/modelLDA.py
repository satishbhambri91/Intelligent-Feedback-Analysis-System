#This file was a POC for the LDA model

import os
import gensim

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from Parser import Corpus
from nltk.stem.porter import PorterStemmer
from gensim import corpora

asps = []
asps2 = []
asps3 = []

folderList = []

#Importing the documents
def getFiles(asps):
    for root, dirs,files in os.walk(r'/Users/satishbhambri/Desktop/IFS/f2011/R7L5'):
        #print(root)
        #print(dirs)
        for file in files:
            if file.endswith('.txt'):
                asps.append(file)
    return asps


def getFiles2(asps2):
    for root, dirs,files in os.walk(r'/Users/satishbhambri/Desktop/IFS/f2011/R6L5'):
        #print(root)
        #print(dirs)
        for file in files:
            if file.endswith('.txt'):
                asps2.append(file)

def getFiles3(asps3):
    for root, dirs,files in os.walk(r'/Users/satishbhambri/Desktop/IFS/f2011/R5L5'):
        #print(root)
        #print(dirs)
        for file in files:
            if file.endswith('.txt'):
                asps3.append(file)
#Cleaning the documents

#Tokenization

tokenizer = RegexpTokenizer(r'\w+')

dict = {}
dict2 = {}
dict3 = {}
def combineText(lst):
    #studentCorpus = open('studentCorpus.txt', 'r+')
    with open('/Users/satishbhambri/Desktop/IFS/f2011/R7L5/studentCorpus.txt', 'r+') as stucorp:
        for file in lst:
            #stucorp.write(file + '\n' + ': ')
            with open('/Users/satishbhambri/Desktop/IFS/f2011/R7L5/' + file) as infile:
                df = infile.read()
                dfk = tokenizer.tokenize(df) #tokenization

                dict[file] = dfk
        stucorp.write(str(dict))
       # print(dict)

        # tfidfVectorize(dict)
                #stucorp.write("\n"*2)
            # with open('/Users/satishbhambri/Desktop/IFS/f2011/R7L5/' + file) as infile:
            #     for line in infile:
            #         stucorp.write(line)

def combineText2(lst2):
    #studentCorpus = open('studentCorpus.txt', 'r+')
    with open('/Users/satishbhambri/Desktop/IFS/f2011/R6L5/studentCorpus.txt', 'r+') as stucorp:
        for file in lst2:
            #stucorp.write(file + '\n' + ': ')
            with open('/Users/satishbhambri/Desktop/IFS/f2011/R6L5/' + file) as infile:
                df = infile.read()
                dfk = tokenizer.tokenize(df) #tokenization

                dict2[file] = dfk
        stucorp.write(str(dict2))
       # print(dict)

        # tfidfVectorize(dict)
                #stucorp.write("\n"*2)
            # with open('/Users/satishbhambri/Desktop/IFS/f2011/R7L5/' + file) as infile:
            #     for line in infile:
            #         stucorp.write(line)


def combineText3(lst3):
    #studentCorpus = open('studentCorpus.txt', 'r+')
    with open('/Users/satishbhambri/Desktop/IFS/f2011/R5L5/studentCorpus.txt', 'r+') as stucorp:
        for file in lst3:
            #stucorp.write(file + '\n' + ': ')
            with open('/Users/satishbhambri/Desktop/IFS/f2011/R5L5/' + file) as infile:
                df = infile.read()
                dfk = tokenizer.tokenize(df) #tokenization

                dict3[file] = dfk
        stucorp.write(str(dict3))
       # print(dict)

        # tfidfVectorize(dict)
                #stucorp.write("\n"*2)
            # with open('/Users/satishbhambri/Desktop/IFS/f2011/R7L5/' + file) as infile:
            #     for line in infile:
            #         stucorp.write(line)

def tokenization(dict):
    pass


def stopwordsRemoval(dict):
    docsList = []
    en_stop = get_stop_words('en')
    for key,value in dict.items():
        with open('/Users/satishbhambri/Desktop/IFS/f2011/Results.txt', 'r+') as resultfile:
            resultfile.write("Without Stop words removal\n")
            resultfile.write(str(value))
        stopped_tokens = [i for i in value if not i in en_stop]
        dict[key] = stopped_tokens
        stopped_tokens2 = [j for j in value if not j in Corpus.stopset]
        dict[key] = stopped_tokens
        with open('/Users/satishbhambri/Desktop/IFS/f2011/Results.txt', 'r+') as resultfile:
            resultfile.write("After stop words removal\n")
            resultfile.write(str(value))
        # Create p_stemmer of class PorterStemmer

        #stemming
        p_stemmer = PorterStemmer()
        texts = [p_stemmer.stem(i) for i in stopped_tokens2]
        dict[key] = texts
        with open('/Users/satishbhambri/Desktop/IFS/f2011/Results.txt', 'r+') as resultfile:
            resultfile.write("After Stemming\n")
            resultfile.write(str(texts))

       #creating a list of documents

        docsList.append(dict[key])
    with open('/Users/satishbhambri/Desktop/IFS/f2011/Results.txt', 'r+') as resultfile:
        resultfile.write(str(docsList))
    return docsList


def stemmingWords(dict):
    # to reduce topically similar words to their root. For example, “stemming,” “stemmer,” “stemmed,” all have similar meanings; stemming reduces those terms to “stem.” This is important for topic modeling, which would otherwise view those terms as separate entities and reduce their importance in the model.

    #Porter stemming algorithm

    #implemented in stopwords removal
    pass





def docTermMatrix(list):
    dictionary = corpora.Dictionary(list)
    #The Dictionary() function traverses texts, assigning a unique integer id to each unique token while also collecting word counts and relevant statistics
    # print("\nToken ID's")
    #print(dictionary.token2id)
    # dictionary must be converted into a bag-of-words
    corpus = [dictionary.doc2bow(text) for text in list]

    #The doc2bow() function converts dictionary into a bag-of-words. The result, corpus, is a list of vectors equal to the number of documents. In each document vector is a series of tuples. As an example, print(corpus[0]) results in the following

    # print(corpus[0])

    # This list of tuples represents our first document, doc_a. The tuples are (term ID, term frequency) pairs, so if  print(dictionary.token2id) says brocolli’s id is 0, then the first tuple indicates that brocolli appeared twice in doc_a. doc2bow() only includes terms that actually occur: terms that do not occur in a document will not appear in that document’s vector.

    #Applying the LDA model
    #corpus is a document-term matrix and now we’re ready to generate an LDA model

    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word=dictionary, passes=20, minimum_probability=0)

    for top in ldamodel.print_topics():
         print(top)

  #  lda_corpus = ldamodel[corpus]

    lda_corpus = [max(prob, key=lambda y: y[1]) for prob in ldamodel[corpus]]
    # i = 1
    print("LDA Corpus")
    print(lda_corpus)
    # for prob in ldamodel[corpus]:
    #     print(len(asps))
    #     print(i)
    #     print("Probability")
    #     print(prob)
    #     i = i + 1

    playlists = [[] for i in range(4)]
    for i, x in enumerate(lda_corpus):
        playlists[x[0]].append(list[i])



    # for key, tuple in asps, lda_corpus:
    #     Lab1[key] = tuple




    # scores = list(chain(*[[score for topic_id, score in topic] \
    #                       for topic in [doc for doc in lda_corpus]]))

    # scores = []
    # # for doc in lda_corpus:
    # #     for topic2 in doc:
    # #         for topic_id, score in topic2:
    # #             scores.append(score)
    # threshold = sum(scores) / len(scores)
    # print(threshold)
    #print(ldamodel.print_topics(num_topics=3, num_words=3))

    # cluster1 = [j for i, j in zip(lda_corpus, docsList) if i[0][1] > threshold]
    # cluster2 = [j for i, j in zip(lda_corpus, docsList) if i[1][1] > threshold]
    # cluster3 = [j for i, j in zip(lda_corpus, docsList) if i[2][1] > threshold]

    # print(playlists)
    # print(cluster2)
    # print(cluster3)

#
# getFiles(asps)
# print(asps)
# getFiles2(asps2)
# print(asps2)
# getFiles3(asps3)
# print(asps3)
# combineText(asps)
# combineText2(asps2)
# combineText3(asps3)
#
# dlist = stopwordsRemoval(dict)
# dlist2 = stopwordsRemoval(dict2)
# dlist3 = stopwordsRemoval(dict3)
#
#
#
# docTermMatrix(dlist)
# docTermMatrix(dlist2)
# docTermMatrix(dlist3)
