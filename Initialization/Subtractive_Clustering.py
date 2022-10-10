import numpy as np
import cv2
import math as m
import time

def calculations(Datapoint,Initial,Radius):
    """
    Description : The Given Function 'calculations' Is Used To Generate And Return Potential Of Each Datapoints
    Parameters : The Following Function Has 3 Parameters 
                 Datapoint - It Returns The Value Of Each Datapoints Whenever Called 
                 Initial - It Returns The Value Of Initial Centroid Whenever Called
                 Radius - It Returns The Radius Of Clusters To Be Formed
    Formulae : Consider An RGB Format Of An Image Therefore Potential Is Calculated As :
               Formula = exp((-4*((R1-R2)^2 + (G1-G2)^2 + (B1-B2)^2))/(Radius^2))
               where,
               R1,G1,B1 - RGB Pixel Intensity Of Given Datapoint
               R2,G2,B2 - RGB Pixel Intensity Of Initial Centroid Choosen
    Variables : Potential - 'Potential' Is Used To Store Potential Of Each Data Points And Return Its Value
    Returns : It Returns Variable '' Which Returns The Final Calculated Euclidean Distance
    """
    difference = Datapoint - Initial
    dif = np.array(difference)
    square = (-4)*(np.sum(dif**2))
    power = square / (Radius**2)
    Potential = m.exp(power)
    return Potential

def SUBTRACTIVE(image,K):
    """
    Description : The Given Function 'SUBTRACTIVE' Is Used To Generate Accurate K Initial Centroids For Faster 
                  And Accurate Implementation Of Clustering Algorithm
    Parameters : The Following Function Has 2 Parameters
                 image - Which Returns And Store NUmpy Array Of Image Whenever Called
                 K - Is The Number Of Initial Cluster Centroids To Be Generated
    Formulae : Algorithm For Subtractive Clustering Is Already Explained Before And Is Directly Implemented Here
    Variables : Ra,Rb - It Stores The Radius Of Clusters Required To Be Generated
                h,w,c - It Stores Height,Width,Channels Of An Image
                data - It Is 1-D Array Which Stores Pixel Values Of Each Data Points
                potential - It Is A 1-D List Which Stores Potential Of Each Datapoints
                pixel - It Is An Array Used For Storing Pixel Value Of A Datapoint
                cluster_x - It Is A List Which Is Used To Store x Coordinate Of A Pixel 
                cluster_y - It Is A List Which Is Used To Store y Coordinate Of A Pixel
                initial_centroids It Is A List Of Initial Centroids Generated By Subtractive Clustering
    Returns : It Returns Variable 'initial_centroids' Which Stores A List Of Initial Cluster Centroid
    """
    Ra = 0.35
    Rb = 1.5*Ra
    start = time.time()
    count = K
    h,w,c = image.shape[0],image.shape[1],image.shape[2]
    data = image.reshape(-1,c)
    potential = []
    for i in range(h*w):
        potential.append(0.0)
    pixel = np.zeros(c,float)
    cluster_x = []
    cluster_y = []
    initial_centroids = []
    centroid = []
    for i in range(h):
        for j in range(w):
            cluster_x.append(i)
            cluster_y.append(j)

    for x in range(len(data)):
        for y in range(x+1 , len(data)):
            value = calculations(data[x],data[y],Ra)
            potential[x] += value
            potential[y] += value

    while(count>0):

        maximum = max(potential) 
        index = potential.index(maximum)

        centroid = []
        for chan in range(c):
            centroid.append(image[cluster_x[index],cluster_y[index],chan])
        initial_centroids.append(centroid)
        
        for i in range(len(potential)):
            for chan in range(c):
                pixel[chan] = image[cluster_x[i],cluster_y[i],chan]
                
            value = calculations(centroid,pixel,Rb)
            potential[i] = potential[i] - (maximum*value)
        
        potential[index] = 0
        count -= 1
    
    end = time.time()
    print("The time of execution of above program is :",(end-start), "s")
    return initial_centroids