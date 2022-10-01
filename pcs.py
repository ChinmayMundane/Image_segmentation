import numpy as np

def PCS(image,new_max,new_min):
    """
    Description : The Given Function 'PCS' Is Used To Perform Pre Processing On Image To Attain An Aim Of 
                  Getting Better Clustering Result
    Parameters : The Following Function Has 1 Parameter 
                 image - It Returns Numpy Array Of Image 
                 new_max - It Return New Maximum Value Of Pixel
                 new_min - It Return New Minimum Value Of Pixel
    Formulae : In This Method We Have Implemented Partial Compression And Stretching Algorithm
    Variables : pixel - 'pixel' Is Array Used To Store RGB Values Of Image
                new_pixel- 'new_pixel' Is Array Used To Store New Modified Pixel Value
    Returns : It Returns 'image1'  Which Stores A Numpy Array Of Modified Image
    """
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