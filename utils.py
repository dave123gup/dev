
# Importing python libraries
import numpy as np
import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Loading/Reading the image
image = cv2.imread("dis.jpg")
#Converting the image from BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
# show your image
plt.figure()
plt.axis("off")
plt.imshow(image)

# reshape the image to be a list of pixels
image = image.reshape((image.shape[0] * image.shape[1], 3))
# cluster the pixel intensities
clusters = KMeans(n_clusters = 7)


clusters.fit(image)

def centroid_histogram(clusters):
	# grab the number of different clusters and create a histogram
	# based on the number of pixels assigned to each cluster
	numLabels = np.arange(0, len(np.unique(clusters.labels_)) + 1)

	(hist, _) = np.histogram(clusters.labels_, bins = numLabels)
 
	# normalize the histogram, such that it sums to one
	hist = hist.astype("float")
	hist /= hist.sum()
 
	# return the histogram
	return hist
def plot_colors(hist, centroids):
	# initialize the bar chart representing the relative frequency
	# of each of the colors
	bar = np.zeros((50, 300, 3), dtype = "uint8")
	startX = 0
 
	# loop over the percentage of each cluster and the color of
	# each cluster
	
	print "Centroids are as follows"
	print centroids
	for (percent, color) in zip(hist, centroids):
		# plot the relative percentage of each cluster
		endX = startX + (percent * 300)
		print (percent*100),color
		print "The above 3 values in square braces indicate the RGB of the constituent color"
		print "percent"
		print " "
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
			color.astype("uint8").tolist(), -1)
		startX = endX
	
	# return the bar chart
	return bar
# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = centroid_histogram(clusters)
bar = plot_colors(hist, clusters.cluster_centers_)
 
# show our color bart
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()
