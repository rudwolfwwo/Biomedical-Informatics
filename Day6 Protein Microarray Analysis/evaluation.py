#-----------------------------------------------------#
#                   Library imports                   #
from scipy.cluster.hierarchy import fclusterdata
#-----------------------------------------------------#

#-----------------------------------------------------#
#               Hierarchical Clustering               #
#-----------------------------------------------------#
def clustering(dt_results, dt_healthy, dt_cancer):
    fclusterdata(X, t=2, criterion='maxclust')
    pass