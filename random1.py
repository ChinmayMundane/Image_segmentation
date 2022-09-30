import numpy as np
def RANDOM(K):
    """
    Description : The Given Function 'RANDOM' Is Used To Calculate Efficient And Accurate Initial Centroid
                  By Randomly Selecting 10 Datapoints And Selecting Data Points Farthest From Each Ethor
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
    sum = []
    cluster = []
    R = 0
    while R <=10:
        Centers=np.random.randint(0,255,size=(K,3))
        cluster.append(Centers)
        distance = 0
        for i in range(1,K):
            arr = np.sqrt(np.sum((Centers[i]-Centers[i-1])**2))
            distance += arr
        sum.append(distance)
        R +=1
    max_value = max(sum)
    index = sum.index(max_value)
    initial_centroids = cluster[index]
    return initial_centroids