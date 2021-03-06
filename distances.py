import numpy as np
import scipy.spatial.distance as ssd

from scipy import dot, linalg

def distances_matrix(records, metric=ssd.euclidean):
    distances = np.zeros((len(records), len(records)))

    for i, base_record in enumerate(records):
        for j, record in enumerate(records):
            distances[i][j] = metric(base_record, record)

    return distances

def min_distance(distances):
    min_dist = float('inf')

    for i, d in enumerate(distances):
        for j, distance in enumerate(d):
            if 0 < distance < min_dist:
                min_dist = distance
                min_row  = i
                min_col  = j

    return (min_dist, min_row, min_col)

