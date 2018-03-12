#Importing libraries required
import numpy as np
import cv2

#Inputting the image
img = cv2.imread('leaf1.jpeg')
Z = img.reshape((-1,3))

# convert to np.float32(numpy array)
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)


#Change this k value
K = 2


#ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
ret,label,center=cv2.kmeans(Z,K,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
im = center[label.flatten()]
im = im.reshape((img.shape))

cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
