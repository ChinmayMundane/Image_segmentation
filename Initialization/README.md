# About
To solve time complexity for kmeans , we used different initialization methods. Now you may ask, what exactly is this initialization ? \
Our kmeans algorithm chooses random k points as our cluster centroid to segment image into k parts. This process is called as random initialization.
this process is not time saving as centroids are taken at random and so optimal centers would be found after many iterations , which will increase our runtime.
Therefore, different initialization techniques were used to limit the runtiime. Techniques used were as follows: \
Subtractive clustering \
Kmeans++ \
Random Initialization method

# Table of content
- [Subtractive clustering](#Subtractive_clustering)
  - [Steps](#Steps)
  - [Disadvantages](#Disadvantages)
- [Kmeans++](#Kmeans++)
  - [Steps](#Steps)
  - [Disadvantages](#Disadvantages)
- [Random Initialization method](#Random_Initialization_method)
  - [Steps](#Steps)
  - [Disadvantages](#Disadvantages)
- [Conclusion](#Conclusion)
- [References](#References)





# Subtractive clustering
Subtractive clustering method is data clustering method where it generates the centroid based on the potential value of the data points.
So subtractive cluster is used to generate the initial centers and these centers are used in k-means algorithm for the segmentation of image. 
 It distribute the data space
into gridding point and compute the potential for each data point base on its distance to the actual data point. So the
grid point with many data point nearby will have high potential value. And so this grid point with highest potential
value will be choose as first cluster centre. So after selecting the first cluster centre we will try to find the second cluster
centre by calculating the highest potential value in the remaining grid points. As grid points near the first cluster center
will reduce its potential value, the next cluster center will be grid with many data point nearby other than first cluster
center grid point. So this procedure of acquiring new cluster center and reducing the potential of surrounding grid
point repeat until potential of all grid points falls below a threshold value.

 
## Steps
1. Use the equation below to calculate the potential for every pixel value of the image. ![image](https://user-images.githubusercontent.com/109454803/193424699-36fba5de-db7b-4200-b79f-ff6318bf4633.png)
 \
where, \
data points: X = {x1, x2, x3 . . . xn } \
ra is hyper sphere cluster radius in data space
2. Find maximum potential in step 1 and set that point be first center cluster and its corresponding potential as
maximum potential.
3. Use equation ![image](https://user-images.githubusercontent.com/109454803/193424756-a5df5b03-e92b-49ba-a5b3-2e9cc6b0517e.png)

to update the potential value of other remaining pixels based on the first cluster center. \
where, \
 x1 and p1 as first cluster centre and its corresponding potential respectively \
 rb is the hyper sphere penalty radius in data space and it is a positive constant.
 
4. Again find the maximum potential in the step 2 and let that point be second point.
5. Continue the process until it finds the k number of cluster.

## Disadvantages
After applying the code with Kmeans and improved kmeans, we found out that runtime for this method was greatest of all methods.
As it had too much runtime , we searched for another method for initialization.
So, the alternate method we chose was Kmeans++.


# Kmeans++
To overcome the above-mentioned drawback we use K-means++.
This algorithm ensures a smarter initialization of the centroids and improves the quality of the clustering.
Apart from initialization, the rest of the algorithm is the same as the standard K-means algorithm.
That is K-means++ is the standard K-means algorithm coupled with a smarter initialization of the centroids.


## Steps
1. Randomly select the first centroid from the data points.
2. For each data point compute its distance from the nearest, previously chosen centroid.
3. Select the next centroid from the data points such that the probability of choosing a point
as centroid is directly proportional to its distance from the nearest, previously chosen centroid.
(i.e. the point having maximum distance from the nearest centroid is most likely to be selected next as a centroid)
4. Repeat steps 2 and 3 until k centroids have been sampled.

## Disadvantages
After applying Kmeans++ to kmeans and improved kmeans , we found that when we applied only improved kmeans ,
 its runtime was still better as compared to application of kmeans++ and improved kmeans.
 
# Random Initialization method
we tried another method as previous methods didn't give us satisfied result.
This time we used random initialization method. \
In this method, we basically iterate for certain time to find random clusters. 
And in this iteration, whose clusters are far away from one another are chosen to be  our initial cluster for kmeans.
we do this  because we want to segment image very accurately and if clusters are far away from one another,it will give us better output.
for better understanding , see this diagram below. \
![image](https://user-images.githubusercontent.com/109454803/193442834-c5b87801-f4eb-408d-83a4-fb26ff86cd1a.png) \
As you can see clusters are close to each other and so our image may give us some faulty output as centroids will pick some
 datapoints to which it doesn't belong. \
 ![image](https://user-images.githubusercontent.com/109454803/193442936-c56888aa-283a-4770-a50c-a5f9ade9be7b.png) \
 while here, centroids are far from each other and even if they are not at center of datapoints, it will still give us better output.

## Steps
- Randomly initialise K centroids.
- find the Sum OF Square Of Distance between each K centroids
- iterate this for 'n' no. of times(for our project we chose n = 10)
- find that Set Of Initial Cluster Centroid whose sum is maximum as its distance will also be maximum.
- set that to be our initial cluster centroid and run kmeans or improved kmeans on it.

## Disadvantages
when compared with kmeans++ , we found that in some cases it is effective while in other , kmeans++ is better.
So comparing both , we cannot know which method would be better but conversely you can say that both methods can be used.


# Conclusion
We can say that initialization methods are definitely better than applying only kmeans, if used with kmeans++ or random initiaization
as subtractive clustering takes most time, out of all.
But overall, improved kmeans method single handedly defeats every combination in terms of time efficiency and accuracy.
the results can be seen at main's readme file.


# References
Subtractive clustering - https://www.researchgate.net/publication/233932671_Fuzzy_Model_Identification_Based_on_Cluster_Estimation?enrichId=rgreq-08593b3226677b5b8cbc445ed54fdebb-XXX&enrichSource=Y292ZXJQYWdlOzIzMzkzMjY3MTtBUzoxOTA0MTEzNjA0NDAzMjBAMTQyMjQwOTAxNDAzOQ%3D%3D&el=1_x_2&_esc=publicationCoverPdf 

