#part 4
# https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
# https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
# https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
# https://github.com/opencv/opencv/blob/master/samples/python/kmeans.py
# https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
# https://stackoverflow.com/questions/39316447/opencv-giving-wrong-color-to-colored-images-on-loading

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from time import sleep

print('starting')

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX
    # return the bar chart
    return bar

#video capture loop
cap = cv2.VideoCapture(0)
while(1):
    _, frame = cap.read()
    dom = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    dom = dom.reshape((dom.shape[0] * dom.shape[1],3))
    #implement k-means clustering
    cluster = KMeans(n_clusters=3)
    cluster.fit(dom)
    histogram = find_histogram(cluster)
    bar = plot_colors2(histogram, cluster.cluster_centers_)
    cv2.imshow('frame',frame)
    cv2.imshow('bar',cv2.cvtColor(bar, cv2.COLOR_RGB2BGR))
    sleep(0.1)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
print('exiting')
