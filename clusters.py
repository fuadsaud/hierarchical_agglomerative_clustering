import distances as d
import numpy as np

class Cluster:
    def __init__(self, ids, points):
        self.ids    = np.array(ids)
        self.points = np.array(points)
        self.center = np.array([np.mean(feature) for feature in zip(*self.points)])

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Cluster({0}, {1})'.format(self.ids, self.center)

def linkage(clusters, metric, clusters_wanted=1):
    def cluster_centers():
        return [cluster.center for cluster in clusters]

    def merge_clusters(*clusters):
        ids    = [_id   for cluster in clusters for _id   in cluster.ids]
        points = [point for cluster in clusters for point in cluster.points]

        return Cluster(
                ids, points)

    def distances_matrix():
        return d.distances_matrix(cluster_centers(), metric=metric)

    def min_cluster(*clusters):
        return min([len(cluster.points) for cluster in clusters])

    def recursive_linkage():
        if len(clusters) == clusters_wanted:
            return clusters

        # calculate distances.
        distances = distances_matrix()

        # find smaller distance.
        min_dist, min_row, min_col = d.min_distance(distances)

        # pop clusters to be merged from the list.
        selected_clusters = [clusters.pop(min_row), clusters.pop(min_col - 1)]

        print 'smaller cluster beign merged', min_cluster(*selected_clusters)

        # merge clusters and add result cluster to the list.
        clusters.append(merge_clusters(*selected_clusters))

        return recursive_linkage()

    return recursive_linkage()
