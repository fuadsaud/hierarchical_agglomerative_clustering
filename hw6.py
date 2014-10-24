import csv
import sys
import numpy as np
import scipy.spatial.distance  as ssd
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

def distance(r1, r2):
    return ssd.euclidean(r1, r2)

def distance_matrix(records):
    distances = np.zeros((len(data), len(data)))

    for i, base_record in enumerate(records):
        for j, record in enumerate(records):
            distances[i][j] = distance(base_record, record)

    return distances

def min_distance(distances):
    min_dist = float('inf')

    for i, d in enumerate(distances):
        for j, distance in enumerate(d):
            if 0 < distance < min_dist:
                return (distance, i, j)

def linkage(data):
    for i in range(data.shape[0] - 1):
        distances = distance_matrix(data)

        np.savetxt('foo.csv', distances, delimiter=',', fmt='%10f')

        # find smaller distance
        min_dist, min_row, min_col = min_distance(distances)

        print 'min dist', min_dist
        print 'min row',  min_row
        print 'min col',  min_col

        # remove clusters from matrix
        clusters = (data[min_row], data[min_col])

        print 'shape', data.shape
        data = np.delete(data, min_row, axis=0)
        data = np.delete(data, min_col - 1, axis=0)

        # link two clusters
        new_cluster = np.array([np.mean(feature) for feature in zip(*clusters)])

        # add new clusters to matrix
        data = np.vstack((data, new_cluster))
        print data

def read_csv(f):
    try:
        reader = csv.reader(f)

        reader.next()

        # creates a numpy matrix with the data read from the csv (discarding id
        # field)
        return np.array([[int(field) for i, field in enumerate(row) if i != 0] for row in reader])
    finally:
        f.close()

data = read_csv(open(sys.argv[1], 'r'))


linkage(data)
