#Group 5
#Car Torres
#Margaux Oriana Gasis
#Thea Kaith Franchette Selerio

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import streamlit as st

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

st.title ("Activity 4")

tf.compat.v1.disable_eager_execution()

option = []

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
     st.pyplot (fig)
     return fig

#cube
def _cube_ (bottom_lower = (0,0,0,), side_length = 5):
     
     """ Create cube starting from the given bottom-lower point (lowest x,y,z values)"""
     bottom_lower = np.array (bottom_lower)
      

     cubepoints = np.vstack ([
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

     return cubepoints

init_cube_ = _cube_ (side_length=3)
cubepoints = tf.constant (init_cube_, dtype = tf.float32)


def rotate(option, points):
    def rotate_obj(points, angle):
        angle = float(angle)
        rotation_matrix = tf.stack([
                        [tf.cos(angle), tf.sin(angle), 0],
                        [-tf.sin(angle), tf.cos(angle), 0],
                        [0, 0, 1]
        ])

        rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))
        
        return rotate_object
        
        
    with tf.compat.v1.Session(rotated_object) as session:
         
          if option == "Cube":
            rotated_object = session.run(rotate_obj(init_cube_, 75)) 
          _plt_basic_object_ (rotated_object)

#pyramid
def _pyramid_ (bottom_lower = (0,0,0,), side_length = 5, height = 5):
     
     """ Create pyramid starting from the given bottom-lower point (lowest x,y,z values)"""
     bottom_lower = np.array (bottom_lower)

     base_points = np.vstack ([
          bottom_lower,
          bottom_lower + [0, side_length, 0],
          bottom_lower + [side_length, side_length, 0],
          bottom_lower + [side_length, 0, 0],
     ])

     top_point = bottom_lower + [side_length/2, side_length/2, height]

     points = np.vstack ([base_points, top_point])

     return points

init_pyramid_ = _pyramid_ (side_length=3)
points = tf.constant (init_pyramid_, dtype = tf.float32)

_plt_basic_object_ (init_pyramid_)

def translate_obj (points, amount):
     return tf.add (points, amount)

translation_amount = tf.constant ([1,2,3], dtype=tf.float32)
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
     translated_pyramid = session.run (translated_object)

_plt_basic_object_ (translated_pyramid)

def rotate(option, points):
    def rotate_obj(points, angle):
        angle = float(angle)
        rotation_matrix = tf.stack([
                        [tf.cos(angle), tf.sin(angle), 0],
                        [-tf.sin(angle), tf.cos(angle), 0],
                        [0, 0, 1]
        ])

        rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))
        
        return rotate_object
        
        
    with tf.compat.v1.Session() as session:
            if option == "Pyramid":
               rotated_object = session.run(rotate_obj(init_pyramid_, 75)) 
            _plt_basic_object_ (rotated_object)


#triangular prism
def _triangular_prism_(bottom_lower=(0, 0, 0), side_length=5, height=5):
    
    bottom_lower = np.array(bottom_lower)
    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [0, 0, height],
        bottom_lower + [0, side_length, height],
        bottom_lower + [side_length, side_length, height],
        bottom_lower,
    ])

    rotation_matrix = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    points = np.dot(points, rotation_matrix.T)
    return points

init_triangular_prism_ = _triangular_prism_ (side_length=3)
points = tf.constant (init_triangular_prism_, dtype = tf.float32)

_plt_basic_object_ (init_triangular_prism_)

def translate_obj (points, amount):
     return tf.add (points, amount)

translation_amount = tf.constant ([1,2,3], dtype=tf.float32)
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
     translated_triangular_prism = session.run (translated_object)

_plt_basic_object_ (translated_triangular_prism)

def rotate(option):
    def rotate_obj(points, angle):
        angle = float(angle)
        rotation_matrix = tf.stack([
                        [tf.cos(angle), tf.sin(angle), 0],
                        [-tf.sin(angle), tf.cos(angle), 0],
                        [0, 0, 1]
        ])

        rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))
        
        return rotate_object
             
    with tf.compat.v1.Session() as session:
          if option == "Triangular Prism":
            rotated_object = session.run(rotate_obj(init_triangular_prism_, 75)) 
            _plt_basic_object_ (rotated_object)

#sphere
def _sphere_(center=(0,0,0,), radius=1):
    
    """ Create sphere starting from the given center point and radius"""
    center = np.array(center)

    phi, theta = np.mgrid[0:np.pi:20j, 0:2*np.pi:20j]
    x = center[0] + radius*np.sin(phi)*np.cos(theta)
    y = center[1] + radius*np.sin(phi)*np.sin(theta)
    z = center[2] + radius*np.cos(phi)

    points = np.vstack([x.flatten(), y.flatten(), z.flatten()]).T

    return points

init_sphere_ = _sphere_ (radius=3)
points = tf.constant (init_sphere_, dtype = tf.float32)

_plt_basic_object_ (init_sphere_)

def translate_obj (points, amount):
     return tf.add (points, amount)

translation_amount = tf.constant ([1,2,3], dtype=tf.float32)
translated_object = translate_obj(points, translation_amount)

with tf.compat.v1.Session() as session:
     translated_sphere = session.run (translated_object)

_plt_basic_object_ (translated_sphere)

def rotate(option, points):
    def rotate_obj(points, angle):
        angle = float(angle)
        rotation_matrix = tf.stack([
                        [tf.cos(angle), tf.sin(angle), 0],
                        [-tf.sin(angle), tf.cos(angle), 0],
                        [0, 0, 1]
        ])

        rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))
        
        return rotate_object
                
    with tf.compat.v1.Session() as session:      
        if option == "Sphere":
            rotated_object = session.run(rotate_obj(init_sphere_, 75)) 
            _plt_basic_object_ (rotated_object)       

            
             

def main ():

     st.sidebar.title("Select 3D")
     option = st.sidebar.selectbox('What shape would you like to manipulate?', ("Cube", 'Pyramid', 'Triangular Prism', 'Sphere'))

     st.write('The shape you chose is:', option)

     if (option == "Cube"):
          st.sidebar.title("Points for Cube")
          x = st.sidebar.slider("Enter for x:", -5, 5, step=1,key='my_slider1')
          y = st.sidebar.slider("Enter for y:", -5, 5, step=1,key='my_slider2')
          z = st.sidebar.slider("Enter for z:", -5, 5, step=1,key='my_slider3')
        
          translation_amount = tf.constant ([x,y,z], dtype=tf.float32)
          translated_points = translation_amount + cubepoints
          st.subheader("Cube")
          st.pyplot()

          

     

          


main()

