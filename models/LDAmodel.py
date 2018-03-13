from gensim import corpora
import gensim
import Parser.StudentKeywordExtractor
import Parser.StopwordsRemoval


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

    return corpus
#
# dict = {}
# lst = []
# dlst = []
# stulst = Parser.StudentKeywordExtractor.getFiles(lst)
# studct = Parser.StudentKeywordExtractor.combineText(stulst,dict)
#
# doclist = Parser.StopwordsRemoval(studct,dlst)
#
# docTermMatrix(doclist)