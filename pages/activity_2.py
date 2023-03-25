import numpy as np
import matplotlib.pyplot as plt
import streamlit as st 

st.set_option('deprecation.showPyplotGlobalUse', False)

two_d_arr = np.array([[1,0,1], [0,1,0],[1,0,1]])

def change(x,y,color):
 
  for i in range(len(two_d_arr)):
    for j in range(len(two_d_arr[i])):
      two_d_arr[x][y] = color

  img = plt.imshow(two_d_arr, interpolation = 'none', cmap = 'Pastel2')
  img.set_clim([0,50])
  plt.colorbar()
  st.pyplot()

def main():
  st.title ("2D Grid")

  x_val = st.number_input ("X coords (row 0-2):", key ="x", min_value= 0, max_value=5)
  y_val = st.number_input ("Y coords (column 0-2):", key="y", min_value=0, max_value=5)
  c_val = st.number_input ("Color Value (1-50):", key="c", min_value=2, max_value= 100)

  change (x_val, y_val, c_val)

if __name__ == '__main__':
   main()