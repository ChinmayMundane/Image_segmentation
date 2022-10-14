# Our Project
Image segmentation using initialization techniques + K-means clustering algorithm from scratch using unsupervised learning.


# Table of contents
- [About the Project](#About-the-Project)
  - [Tech Stack](#Tech-Stack)
  - [File Structure](#File-Structure)
- [Getting Started](#Getting-Started)
  - [Prerequisites and installlation](#Prerequisites-and-installlation)
  - [Installation](#Installation)
  - [Execution](#Execution)
- [Theory and Approach](#Theory-and-Approach)
-  [Flowchart](#Flowchart)
-  [Results and Demo](#Results-and-Demo)
-  [Future Work](#Future-Work)
-  [Contributors](#Contributors)
-  [Acknowledgements and Resources](#Acknowledgements-and-Resources)
-  [License](#License)

# About the Project
Image segmentation is the classification of an image into different groups. Here we have use k-means clustering algorithm for image segmentation.K -means clustering algorithm is an unsupervised algorithm and it is used to segment the interest area from the background. But before applying K -means algorithm, first partial stretching enhancement is applied to the image to improve the quality of the image. Next, Initialization techniques like subtractive clustering, kmeans++, random initialization is used to generate the initial centers and these centers are used in k-means algorithm for the segmentation of image. Then finally medial filter is applied to the segmented image to remove any unwanted region from the image. \
![image](https://user-images.githubusercontent.com/109454803/194568361-7efcbcf9-80c1-4d8f-b2e9-9ac691f8fbc7.png)



## Tech Stack
- [Python](https://www.python.org/)
- [Opencv](https://opencv.org/)
- [Numpy](https://numpy.org/doc/#)


## File Structure
```
.📦
├── 📂assets				    # contains images and video			
│   ├── 📜images										 
├── 📂Clustering                            # contains code of kmeans and improved kmeans and its breif summary
|   ├── 📜Improved.py
|   ├── 📜K_Means.py 
|   ├── 📜README.md
├── 📂Initialization                        # codes and summary of initialization techniques
|   ├── 📜KMeans_Plus.py
|   ├── 📜README.md
|   ├── 📜Random.py
|   ├── 📜Subtractive_Clustering.py
├── 📜main.py                               # module to run code of your choice
├── 📂Processing                            # code to improve contrast
|   ├── 📜pcs.py
|   ├── 📜README.md 
├── 📂Results                               # Project result
|   ├── 📜Set1
|   ├── 📜Set2
|   ├── 📜Set3
|   ├── 📜Set4
|   ├── 📜Set5
|   ├── 📜Set6
├──  📂report				   # Project report
|   └── 📜report.pdf		
└──📜README.md		                   # Project readme
```

# Getting Started
## Prerequisites and installlation
- Should have python downloaded. You can refer [here](https://www.python.org/downloads/) for the setup.
- Any code editor
- The installations provided below are installed using pip. so you first need to install pip.
  - To install pip , follow this [link](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)
- To install numpy
```
pip install numpy
```
- To install OpenCV
```
 pip install opencv-python
```


## Installation
- Clone the repo
```
git clone https://github.com/ChinmayMundane/Image_segmentation.git
```

## Execution
Now that you have installed the repo, let's get started with exciting part i.e. how to run it !
- open your terminal(make sure you are in same folder/directory where you cloned the repo)
- now run
```
python <file_name>.py
```

# Theory and Approach
Our main idea is to segment the image using kmeans from scratch.This project can further be used in many areas like medical analysis , image detection , image extraction,etc. we select random number of clusters.let us suppose that to be 'K'. next we divide the image into K parts of size n and segment it into that many parts. 

- preprocessing
our project requires processing the images under test. Image processing is the operation of converting images into computer readable data. To perform the necessary operations we used P.C.S (partial contrast stretching) which improves the contrast of image, so that the output would be better.

- Initialization techniques
initializaton techniques are methods with which we find optimal cluster centers so that the runtime as well as the accuracy can be made better.we have used many techniques such as subtractive clustering, kmeans++ and randomm initialization for our project. out of them , kmeans++ and random initialization can be used. 


- K-Means clustering
So, after improving contrast of image and selecting no. of cluster centers, we need to cluster them by using K-Means clustering.K-means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean. To know more check Clustering folder.

# Flowchart
![image](https://user-images.githubusercontent.com/109454803/195906413-7e855bbc-df6d-4217-a74c-2d7d007e9deb.png)



# Results and Demo
![image](https://user-images.githubusercontent.com/109454803/194618933-bff15859-b4db-49b2-9e60-3c1f4a95ee2d.png) \
![image](https://user-images.githubusercontent.com/109454803/194618973-02d9a2bc-8109-4dd6-9a93-3d38a8dbd2c5.png) \
![image](https://user-images.githubusercontent.com/109454803/194619026-5c7ef824-7ee2-495c-9631-e8abc3b3c28b.png) 


Result Analysis
Algorithm used | No Pre-Initialization | K-means++ | Random Initialization | OpenCV 
--- | --- | --- |--- |---
K-means | 22.5s | 22.1s | 28.3s | 0.55s
Improved K-means | 12.7s | 19.1s | 21.6s | 0.55s




# Future Work
- To increase its time efficiency by using alternate methods like F.B.K(FAST BALANCED K-MEANS) algorithm .
- we will also work on semantic segmentation where we have a task of clustering parts of an image together which belong to the same object class.

# Contributors
- [Chinmay Mundane](https://github.com/ChinmayMundane)
- [Smit Shah](https://github.com/Smit1603)

# Acknowledgements and Resources
- [SRA VJTI](https://sravjti.in/) Eklavya 2022
- [Kmeans research paper](https://www.sciencedirect.com/science/article/pii/S1877050915014143#:~:text=Subtractive%20clustering%20method%20is%20data,for%20the%20segmentation%20of%20image)
- [Improved kmeans](https://ieeexplore.ieee.org/document/5453745)
- [subtractive clustering](https://www.researchgate.net/publication/233932671_Fuzzy_Model_Identification_Based_on_Cluster_Estimation?enrichId=rgreq-08593b3226677b5b8cbc445ed54fdebb-XXX&enrichSource=Y292ZXJQYWdlOzIzMzkzMjY3MTtBUzoxOTA0MTEzNjA0NDAzMjBAMTQyMjQwOTAxNDAzOQ%3D%3D&el=1_x_2&_esc=publicationCoverPdf)
- Our mentors [Dhruv kunjadiya](https://github.com/Dhruv454000) and [Pratham Shah](https://github.com/shahpratham) for their guidance throughout the whole project.


# License
MIT License




