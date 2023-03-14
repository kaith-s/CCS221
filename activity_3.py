import numpy as np
import cv2
import matplotlib.pyplot as plt
import streamlit as st 

def read_image (path):
    img = cv2.imread (path)
    return cv2.cvtColor (img, cv2.COLOR_BGR2RGB)

def translation_img (img):
    rows, cols = img.shape [:2]
    M = np.float32([[1, 0, 60],
                [0, 1, 50],
                [0, 0, 1]])
    
    translated_img = cv2.warpPerspective(img, M, (cols, rows))
    return translated_img



# file upload
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
        # read image
        bytes_data = uploaded_file.read()
        nparr = np.frombuffer(bytes_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
else:
    img = read_image ("haha.jpg")

def main ():

# apply a perspective transformation to the image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # read image
        bytes_data = uploaded_file.read()
        nparr = np.frombuffer(bytes_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        img = read_image ("haha.jpg")

  

#rotation transformation matrix
    angle= np.radians(10)
    m_rotation_ = np.float32([[np.cos(angle), -(np.sin(angle)),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])
    rotated_img_ = cv2.warpPerspective(img ,m_rotation_,(int(cols),int(rows)))

    plt.axis('off')
    st.image(rotated_img_)

    m_rotation_=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)

    rotated_img_=cv2.warpAffine(img ,m_rotation_,(cols,rows))
    plt.axis('off')
    st.image(rotated_img_)

#scaling transformation matrix
    m_scaling_=np.float32([[1.5,0,0],[0,1.8,0],[0,0,1]])
    scaled_img_=cv2.warpPerspective(img, m_scaling_,(cols*2,rows*2))

    plt.axis('off')
    st.image(scaled_img_)

    resized_img_=cv2.resize(img, None,fx=4,fy=4, interpolation=cv2.INTER_CUBIC)
    resized_img_.shape

    plt.axis('off')
    st.image(resized_img_)

#OR
    height, width = img.shape[:2]
    resized_img_= cv2.resize(img,(8*width, 8*height), interpolation = cv2.INTER_CUBIC)
    resized_img_.shape

    plt.axis('off')
    st.image(resized_img_)




