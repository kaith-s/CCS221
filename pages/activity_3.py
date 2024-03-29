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

def translation(img):
    rows, cols = img.shape[:2]
    m_translation_ = np.float32([[1, 0, 60],
                [0, 1, 50],
                [0, 0, 1]])

    translated_img_= cv2.warpPerspective(img, m_translation_,(cols, rows))

    return translated_img_

def rotation(img):

    angle =np.radians(10)
    rows, cols = img.shape[:2]
    m_rotation_=np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                        [np.sin(angle), np.cos(angle),0],
                        [0,0,1]])

    m_rotation_=cv2.getRotationMatrix2D((cols/2,rows/2), 80, 1)
    rotated_img_ = cv2.warpAffine(img,m_rotation_,(cols,rows))

    return rotated_img_

def scaling_img(img):
    rows, cols = img.shape[:2]
    m_scaling_=np.float32([[1 ,0 ,0],
                       [0, 1.5 ,0],
                       [0,0,1]])
    scaled_img_ =cv2.warpPerspective(img,m_scaling_,(cols*2,rows*2))

    return scaled_img_

def reflection_(img):
    rows, cols = img.shape[:2]
    m_reflection_ =np.float32([[-1, 0, cols],
                          [0, 1, 0],
                          [0, 0, 1]])
    reflected_img_ =cv2.warpPerspective(img,m_reflection_,(int(cols),int (rows)))

    return reflected_img_

def shear_(img):
    rows, cols = img.shape[:2]
    m_shearing_=np.float32([[1, 0.5 ,0],
                         [0,1,0],
                         [0,0,1]])

    sheared_img = cv2.warpPerspective(img, m_shearing_,(int(cols*1.5),int(rows*1.5)))

    return sheared_img

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


    #trasnfo
    translated_img = translation(img)
    rotated_img = rotation(img)
    scaled_img = scaling_img(img)
    reflected_img = reflection_(img)
    sheared_img = shear_(img)


    st.subheader("Original Image")
    st.image(img)

    st.subheader("Translated Image")
    st.image(translated_img)

    st.subheader("Rotated Image")
    st.image(rotated_img)

    st.subheader("Scaled Image")
    st.image(scaled_img)

    st.subheader("Reflected Image")
    st.image(reflected_img)

    st.subheader("Sheared Image")
    st.image(sheared_img)

    plt.show()

main ()
