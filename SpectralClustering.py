import sys
import os
import numpy as np
import operator
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics
sys.path.insert(0, r'/home/satish/ASU/Webplp/project/intelligent-feedback-system')
import constants
sys.path.insert(0, r'/home/satish/ASU/Webplp/project/intelligent-feedback-system')
import GetSimilarityMatrix




def buildGraph(arrayofstudents):
    # number_students, studentarray, studentmap = GetSimilarityMatrix.getStudentIDNameMap()

    # G = nx.Graph()
    # path = "../data/student/filtered_text_token/"
    # file_names = os.listdir(path)
    # for file_name in file_names:
    #     token = file_name.split(".")
    #     studentid = token[0]
    #     G.add_node(studentid)
    #     for collab, w in studentcollabmap[studentid]:
    #         G.add_edge(studentid, collab, weight=1/w);

    G = nx.Graph()
    count = 0
    for k, v in hash_obj.items():
        if k in arrayofstudents:
            G.add_node(k)
            for node in v:
                for n, w in v.items():
                    G.add_edge(k,n, weight=w)

    return G




def specclustering(studentarray):
    np.random.seed(1)


    # Get your mentioned graph
    G = buildGraph(studentarray)


    # Get adjacency-matrix as numpy-array
    adj_mat = nx.to_numpy_matrix(G)
    print(adj_mat)

    # Cluster
    sc = SpectralClustering(5, affinity='precomputed', n_init=100, assign_labels='discretize')
    #sc = AgglomerativeClustering(5, )
    sm = sc.fit(adj_mat)
    print(sm.labels_)


    # Compare ground-truth and clustering-results
    print('spectral clustering')
    clusterfile = open('Cluster.txt', 'w')
    i = 0
    dict = {}

    while i<len(G.nodes()):
         x = int(sc.labels_[i])
         if x in dict:
             dict[x].append(G.nodes()[i])
         else:
             dict[x] = []
             dict[x].append(G.nodes()[i])
         i = i+1



    for k,v in dict.items():
        clusterfile.write(str(k) + ":" + str(v) + ",")
        clusterfile.write("\n")
    clusterfile.close()

    n = 5

    bestlist = []
    maxvalue = 0
    for k, v in dict.items():
        if len(v)>n:
            maxsum , centroid = getcentroid(v, G)
            print(centroid)
            print(maxsum)
            list, sumval = getsumofclosest(n,centroid,G)
            if sumval > maxvalue:
                bestlist = list
                maxvalue = sumval


    print(bestlist)
    pass

def getsumofclosest(n,centroid,G):

    dict = {}
    nodelist = G.neighbors(centroid);
    for node in nodelist:
        dict[node] = G.edge[centroid][node]['weight']

    sorted_dict = sorted(dict.items(),key=(operator.itemgetter(1)),reverse=True)
    print(sorted_dict)
    i = 0
    val = 0;
    list = [centroid]
    for k, v in sorted_dict:
        if i == n-1:
            break
        list.append(k)
        val = val + v
        i = i+1

    return list, val

def getTotalDistance(node, list, G):
    sum = 0
    for item in list:
        if G.has_edge(node,item):
            sum = sum + G.edge[node][item]['weight']
    return sum

def getcentroid(list, G):
    maxsum = 0
    center = 0
    for item in list:
        sum = getTotalDistance(item, list, G)
        if sum > maxsum:
            maxsum = sum
            center = item
    return maxsum, center

if __name__ == "__main__": specclustering()