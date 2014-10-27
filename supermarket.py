import csv
import sys
import clusters
import scipy.spatial.distance as ssd

def clusters_from_csv(f):
    try:
        reader = csv.reader(f)

        reader.next()

        # creates a numpy matrix with the clusters read from the csv
        records = [map(int, row) for row in reader]

        return [clusters.Cluster([row[0]], [row[1:-1]]) for row in records]
    finally:
        f.close()

records = clusters_from_csv(open(sys.argv[1], 'r'))

clustering = clusters.linkage(
        records,
        clusters_wanted=3,
        metric=ssd.canberra)

for i, cluster in enumerate(clustering):
    print 'Cluster {0} (length: {1}, center: {2})'.format(
            i + 1,
            len(cluster.points),
            cluster.center)

    for _id, point in sorted(zip(cluster.ids, cluster.points)):
        print ('%2d' % _id), '(', ' '.join('%02s' % i for i in point), ' )'
