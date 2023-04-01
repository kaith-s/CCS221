import numpy as np
import matplotlib.pyplot as plt
import streamlit as st 

st.set_option('deprecation.showPyplotGlobalUse', False)


def change(two_d_arr,x,y,color):
 
  two_d_arr[x][y] = color
  fig, ax = plt.subplots()
  img = ax.imshow(two_d_arr, interpolation = 'none', cmap = 'Pastel2')
  img.set_clim([0,50])
  plt.colorbar(img)
  st.pyplot(fig)

def main():
  st.title ("2D Grid")

  two_d_arr = np.array([[1,0,1], [0,1,0],[1,0,1]])

  for i in range (3):

    x_val = st.number_input ("Input the X coordinate (row 0,1,2) that are available:", 0, 2, 0, key=f"x_val_{i}")
    y_val = st.number_input ("Input the Y coordinate (column 0,1,2) that are available:", 0, 2, 0, key=f"y_val_{i}")
    c_val = st.number_input ("Enter a Color Value from (1-50):", 1, 50, 1, key=f"c_val_{i}")

  change (two_d_arr,x_val, y_val, c_val)

main()
