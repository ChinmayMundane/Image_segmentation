import numpy as np

def PCS(image):
    """
    Description : The Given Function 'PCS' Is Used To Perform Pre Processing On Image To Attain An Aim Of Getting Better Output
    Parameters : The Following Function Has 1 Parameter 
                 K - It Tells Number Of Cluster To Be Formed / Number Of Initial Centroid To Be Generated
    Formulae : In This Method We Try To Store 10 Or More Sets Of K Cluster Centroid And We Calculate Sum Of Square 
               Of Distance Between Initial Centroids Choosen For Each Set
               Example : Suppose A Set Has 4 Cluster Centroids Than We Try To Collect 10 Or More Sets With 4 Cluster Centroid
                         And Then We Try To Calculate Sum OF Square Of Distance Between Each Of The 4 Cluster Centroid
                         And Only That Set Of Initial Cluster Centroid Is Choosen Where The Sum Is Maximum
    Variables : cluster - 'cluster' Is List Used To Store 10 Or More Set Of Inital Cluster Centroid
                sum - 'sum' Is List Used To Store Sum Of Square Of Distances Calculated
                       For Each Set
    Returns : It Returns Variable 'initial_centroids' Which Stores A List Of Initial Cluster Centroid
    """
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