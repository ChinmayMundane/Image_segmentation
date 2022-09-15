from cmath import inf
import numpy as np
import cv2

K1 = input("Enter Number Of Clusters : ")
K = int(K1)
image=cv2.imread("I:\image segmentation\image1.jpg")
h,w,c=image.shape[0],image.shape[1],image.shape[2]
image = image.reshape(-1,3)
sz = len(image)
print(sz)
centroids=[]
center=np.random.randint(0,255,size=(1,c))
center = center.flatten()
centroids.append(center)


def dist(b1,pnt):
    distance = np.sum((b1 - pnt)**2)
    return distance


def initialize(img):
    
    for l in range(K-1):
        distan = []
        
        for i in range(0,sz):
            d=inf
            
            for t in range(len(centroids)):
               
                temp_dist = dist(centroids[t],img[i])
                d = min(d,temp_dist)
            distan.append(d)
            
       
        next_centroid = image[np.argmax(distan), :]
   
        centroids.append(next_centroid)
        print(K,"k")
       
        
    return centroids
centroids = initialize(image)
print(centroids)
