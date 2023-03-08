import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

import tensorflow as tf
import streamlit as st

def _plt_basic_object_ (points) :
     
     """" Plots a basic object, assuming its convex and not too complex"""

     tri = Delaunay (points).convex_hull

     fig = plt.figure (figsize = (8, 8))
     ax = fig.add_subplot (111, projection = '3d')
     S = ax.plot_trisurf (points [:,0], points [:,1], points [:,2], 
                            triangles = tri,
                            shade = True, cmap = cm.rainbow  , lw = 0.5)

     ax.set_xlim3d (-5,5)
     ax.set_ylim3d (-5,5)
     ax.set_zlim3d (-5,5)

     plt.show()

def _cube_ (bottom_lower = (0,0,0,), side_length = 5):
     
     """ Create cube starting from the given bottom-lower point (lowest x,y,z values)"""
     bottom_lower = np.array (bottom_lower)

     points = np.vstack ([
          bottom_lower,
          bottom_lower + [0, side_length, 0],
          bottom_lower + [side_length, side_length, 0],
          bottom_lower + [side_length, 0, 0],
          bottom_lower + [0,0,side_length],
          bottom_lower + [0, side_length, side_length],
          bottom_lower + [side_length, side_length, side_length],
          bottom_lower + [side_length, 0, side_length],
          bottom_lower,
     ])

     return points


side_length = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', side_length)
init_cube_ = _cube_ (side_length)
points = tf.constant (init_cube_, dtype = tf.float32)

_plt_basic_object_ (init_cube_)





