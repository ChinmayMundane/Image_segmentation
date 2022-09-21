import cv2
import numpy as np
import matplotlib.pyplot as plt 

def pcs(image):
    new_max = 240
    new_min = 70
    image1 = np.copy(image)
    h,w,c = image.shape[0],image.shape[1],image.shape[2]
    pixel = np.zeros(c,float)
    new_pixel = np.zeros(c,float)
    for i in range(h):
        for j in range(w):
            for chan in range(c):
                pixel[chan] = image[i,j,chan] 
                new_pixel = (((new_max-new_min)*(pixel))/255) + new_min
            for chan in range(c):
                image1[i,j,chan]=new_pixel[chan]
    
    return image1