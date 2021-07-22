import pydicom
import os
import numpy 
from lungmask import mask
import SimpleITK as sitk
import matplotlib.pyplot as plt

if __name__ == '__main__':

    fpath = '//10.140.40.23/RAWPMR Backup/PHYSICS/Cameron/ILD_Software_Scripts/CT Full Inspirati  3.0  I70f  3'

    # Read image using pydicom
    os.chdir('//10.140.40.23/RAWPMR Backup/PHYSICS/Cameron/ILD_Software_Scripts/CT Full Inspirati  3.0  I70f  3')
    #ds = pydicom.dcmread('AC_A_002.CT.15.1.2021.02.17.09.31.38.859000.2.0.134975484.IMA')
    #plt.imshow((ds.pixel_array), cmap=plt.cm.bone)
    #plt.show()

    for dirName, subdirList, fileList in os.walk(fpath):                # work through directory
        lstFilesDCM = []                                                # create an empty list for file names
        for filename in fileList:                                       # for each file in patient scan 
            lstFilesDCM.append(filename)

    print(lstFilesDCM)

    input_image = sitk.ReadImage(lstFilesDCM)     # input image must be a SimpleITK object 
    print(input_image)
    segmentation = mask.apply(input_image)  # default model is U-net(R231), returns ndarray
    print(numpy.average(segmentation))
    slice = segmentation[50,:,:]
    plt.imshow((slice), cmap=plt.cm.bone)
    plt.show()

