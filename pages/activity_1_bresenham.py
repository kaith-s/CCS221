#bresenham's line algorithm
import matplotlib.pyplot as plt

import streamlit as st


def bres_line_mpoint(x1,y1,x2,y2):
    x,y = x1, y1
    dx = abs(x2 - x1) 
    dy = abs(y2 - y1) 
    slope = dy/float(dx)

    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    xcoords = [x]
    ycoords = [y]

    xm = (x1 + x2)/2
    ym = (y1 + y2)/2  # These lines of codes are the midpoint formula
    st.write("\nX midpoint: ", xm)
    st.write("Y midpoint: ", ym)

    fig, ax = plt.subplots()
    ax.plot(xm, ym, marker='o', markerfacecolor="green")
    for i in range(1, int(dx)):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy 
        x = x + 1 if x < x2 else x - 1
        xcoords.append(x)
        ycoords.append(y)
    ax.plot(xcoords, ycoords)
    st.pyplot(fig)



def main():
    st.sidebar.title("Select Algorithm")
    algorithm = st.sidebar.selectbox("Select Algorithm", ("DDA", "Bresenham"))

    x1 = st.sidebar.number_input("Enter the Starting point of x:")
    y1 = st.sidebar.number_input("Enter the Starting point of y:")
    x2 = st.sidebar.number_input("Enter the end point of x:")
    y2 = st.sidebar.number_input("Enter the end point of y:")

    if algorithm == "Bresenham":  
        bres_line_mpoint(x1,y1,x2,y2)