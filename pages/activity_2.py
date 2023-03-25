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

  x_val = st.number_input (input("X coords:"))
  y_val = st.number_input(input("Y coords:"))
  c_val = st.number_input(input("Color Value (1-50)"))

  change (x_val, y_val, c_val)

if __name__ == '__main__':
   main()