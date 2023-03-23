import numpy as np
import cv2
import matplotlib.pyplot as plt
import streamlit as st

def read_image(path):
    img = cv2.imread(path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def translation_ (img):
# read the input image
    img = cv2.imread('haha.png')
    print(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)

# get the image shape
    rows, cols, dim = img.shape
# transformation matrix for translation
    M = np.float32([[1, 0, 60],
                [0, 1, 50],
                [0, 0, 1]])

# apply a perspective transformation to the image
    translated_img = cv2.warpPerspective(img, M, (cols, rows))

    return translated_img

def main ():
    st.title ("Quiz 1: TRANSLATION")

    # file upload
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # read image
        bytes_data = uploaded_file.read()
        nparr = np.frombuffer(bytes_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        img = read_image()

    translated_img = translation_ (img)
   
    st.subheader("Original Image")
    st.image(img)

    st.subheader("Translated Image")
    st.image(translated_img)

main()


