#Group 5
#Car Torres
#Margaux Oriana Gasis
#Thea Kaith Franchette Selerio

import numpy as np
import cv2 
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from io import StringIO

def read_image(path):
    img = cv2.imread(path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def translation(img, tx, ty):
    rows, cols = img.shape[:2]
    m_translation_ =np.float32([[1,0, tx],
                        [0,1 , ty],
                        [0,0,1]])

    translated_img_= cv2.warpPerspective(img,m_translation_,(cols, rows))
    return translated_img_

def rotation(img, rotx):

    angle =np.radians(10)
    rows, cols = img.shape[:2]
    m_rotation_=np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                        [np.sin(angle), np.cos(angle),0],
                        [0,0,1]])

    m_rotation_=cv2.getRotationMatrix2D((cols/2,rows/2), rotx, 1)
    rotated_img_ = cv2.warpAffine(img,m_rotation_,(cols,rows))
    return rotated_img_

def scaling_img(img, scaleX, scaleY):
    rows, cols = img.shape[:2]
    m_scaling_=np.float32([[scaleX ,0 ,0],
                       [0, scaleY ,0],
                       [0,0,1]])
    scaled_img_ =cv2.warpPerspective(img,m_scaling_,(cols*2,rows*2))
    return scaled_img_

def reflection_v(img):
    rows, cols = img.shape[:2]
    m_reflection_ =np.float32([[1,0,0],
                          [0,-1, rows],
                          [0,0,1]])
    reflected_img_ =cv2.warpPerspective(img,m_reflection_,(int(cols),int (rows)))
    return reflected_img_

def reflection_h(img):
    rows, cols = img.shape[:2]
    m_reflection_ =np.float32([[-1, 0, cols],
                          [0, 1, 0],
                          [0, 0, 1]])
    reflected_img_ =cv2.warpPerspective(img,m_reflection_,(int(cols),int (rows)))
    return reflected_img_

def shear_X(img, shearX):
    rows, cols = img.shape[:2]
    m_shearing_x=np.float32([[1, shearX ,0],
                         [0,1,0],
                         [0,0,1]])

    sheared_img_x = cv2.warpPerspective(img, m_shearing_x,(int(cols*1.5),int(rows*1.5)))

    return sheared_img_x

def shear_Y(img, shearY):
    rows, cols = img.shape[:2]
    m_shearing_x=np.float32([[1, 0 ,0],
                         [ shearY , 1 ,0],
                         [0, 0, 1]])

    sheared_img_x = cv2.warpPerspective(img, m_shearing_x,(int(cols*1.5),int(rows*1.5)))

    return sheared_img_x

def main():
    st.title ("Activity 3: IMAGE TRANSFORMATIONS")

      # file upload
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # read image
        bytes_data = uploaded_file.read()
        nparr = np.frombuffer(bytes_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        img = read_image()

    #The following lines calls each of the functions for specific transformations of the images.
    tx = int(input("Enter the value to shift in X-axis: ")) 
    ty = int(input("Enter the value to shift in Y-axis: "))
    rotx = int(input("Enter value to rotate the image in degrees: "))
    scaleX = int(input("Enter the value to scale in X-Axis: "))
    scaleY = int(input("Enter the value to scale in Y-Axis: "))
    shearX = float(input("Enter the value to shear in X-Axis: "))
    shearY = float(input("Enter the value to shear in Y-Axis: "))


        #The following lines calls each of the functions for specific transformations of the images.
    translated_img_ = translation(img)
    rotated_img_ = rotation(img)
    scaled_img_ = scaling_img(img)
    reflected_h = reflection_h(img)
    reflected_v = reflection_v(img)
    sheared_img_x = shear_X(img)
    sheared_img_y = shear_Y(img)


    st.subheader("Original Image")
    st.image(img)

    st.subheader("Translated Image")
    st.image(translated_img_)

    st.subheader("Rotated Image")
    st.image(rotated_img_)

    st.subheader("Scaled Image")
    st.image(scaled_img_)

    st.subheader("Reflected Image")
    st.image(reflected_h)

    st.subheader("Reflected Image")
    st.image(reflected_v)

    st.subheader("Sheared Image")
    st.image(sheared_img_x)

    st.subheader("Sheared Image")
    st.image(sheared_img_y)

    plt.show()

main ()
