#this file will be used to run each of the python files in the correct order

from .motif_counting import *
from .motif_adjacency_matrix import *
from .k_clusters import *

def run_algorithm(fp, motif, k):
    
    edge_counts = motif_counting(fp, motif)
    motif_adjacency_matrix = create_motif_adjacency_matrix(edge_counts)
    cluster_dict = k_clusters(motif_adjacency_matrix, k)
    print("The classification of nodes into {0} clusters by counting motif {1} is: {2}".format(k, motif, cluster_dict))    
    return cluster_dict