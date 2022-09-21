import math as m
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def code(image,K):

    # image = plt.imread(path)
    image1 = np.copy(image)
    # plt.imshow(image)
    # plt.show()

    h,w,c = image.shape[0],image.shape[1],image.shape[2]
    # K = int(input("Enter Number Of Clusters To Be Formed : "))
    count = K
    x = random.randint(0,h)
    y = random.randint(0,w)
    # pixel = np.zeros(c)
    # pixel1 = np.zeros(c)
    pixel = []
    pixel1 = []
    
    for k in range(c):
        pixel.append(image[x,y,k])
    
    # print(pixel,'4')
    initial_centroid = [np.array(pixel)]
    # initial_centroid.append(pixel)
    distance = []
    clust_x = []
    clust_y = []
    min_distance = []


    while(count>1):
        
        min_distance = []
        clust_x = []
        clust_y = []
        pixel = []
        # pixel1 = np.zeros(c,float)
        for i in range(h):
            for j in range(w):
                # pixel = []
                pixel1 = []
                for chan in range(c):
                    pixel1.append(image[i,j,chan])
                
                for k in range(len(initial_centroid)):
                    distance.append(m.sqrt(np.sum((np.array(pixel1) - initial_centroid[k])**2)))
                mdis = min(distance)
                distance = []

                min_distance.append(mdis)
                clust_x.append(i)
                clust_y.append(j)
        maximum = max(min_distance)
        index1 = min_distance.index(maximum)
        # print(clust_x[index],clust_y[index])
        # print(initial_centroid)
        for chan in range(c):
            pixel.append(image[ clust_x[index1] , clust_y[index1] , chan ])
            # print(pixel[chan],'cc')
        # print(pixel,'p')
        initial_centroid.append(pixel)
        count = count - 1
    return initial_centroid
        
if __name__ == "__main__":
    code()