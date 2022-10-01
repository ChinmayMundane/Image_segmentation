# About
To solve time complexity for kmeans , we used different initialization methods. Now you may ask, what exactly is this initialization ? \
Our kmeans algorithm chooses random k points as our cluster centroid to segment image into k parts. This process is called as random initialization.
this process is not time saving as centroids are taken at random and so optimal centers would be found after many iterations , which will increase our runtime.
Therefore, different initialization techniques were used to limit the runtiime. Techniques used were as follows: \
Subtractive clustering \
Kmeans++ 

# Table of content
- [Subtractive clustering](#Subtractive_clustering)
  - [Steps](#Steps)
  - [Disadvantages](#Disadvantages)
- [Kmeans++](#Kmeans++)
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
1. Use the equation below to calculate the potential for every pixel value of the image. \
![Screenshot (44)](https://user-images.githubusercontent.com/109454803/193085675-026e3575-3b05-4b08-b0ed-a21c0ff86bd6.png) \
where, \
data points: X = {x1, x2, x3 . . . xn } \
ra is hyper sphere cluster radius in data space
2. Find maximum potential in step 1 and set that point be first center cluster and its corresponding potential as
maximum potential.
3. Use equation ![Screenshot (45)](https://user-images.githubusercontent.com/109454803/193086704-deacde97-91bf-4c9e-b9a2-b8ace05de945.png)

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
After applying Kmeans++ to kmeans and improved kmeans , we found that whn we applied only improved kmeans ,
 its runtime was still better as compared to application of kmeans++ and improved kmeans.
 
 
# Conclusion
We can say that initialization methods are definitely better than applying only kmeans, if used with kmeans++ 
as subtractive clustering takes most time, out of all.
But overall, improved kmeans method single handedly defeats every combination in terms of time efficiency and accuracy.
the results can be seen at main's readme file


# References
Subtractive clustering - https://www.researchgate.net/publication/233932671_Fuzzy_Model_Identification_Based_on_Cluster_Estimation?enrichId=rgreq-08593b3226677b5b8cbc445ed54fdebb-XXX&enrichSource=Y292ZXJQYWdlOzIzMzkzMjY3MTtBUzoxOTA0MTEzNjA0NDAzMjBAMTQyMjQwOTAxNDAzOQ%3D%3D&el=1_x_2&_esc=publicationCoverPdf \
Kmeans++ - https://www.geeksforgeeks.org/ml-k-means-algorithm/

