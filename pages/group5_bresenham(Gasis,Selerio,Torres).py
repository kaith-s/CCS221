#bresenham's line algorithm
import matplotlib.pyplot as plt

import streamlit as st


def bresenhamLine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

    # determine the sign of the change in x and y
    sx = 1 if dx > 0 else -1
    sy = 1 if dy > 0 else -1

    # calculate the absolute value of the change in x and y
    dx = abs(dx)
    dy = abs(dy)

    # initialize the decision parameter
    p = 2 * dy - dx

    for x, y in zip(range(x1, x2+sx, sx), range(y1, y2+sy, sy)):
        # plot the pixel
        plt.plot(int (x), int (y), color)

        
        # update the decision parameter
        if p >= 0:
            y = y + sy
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

    midX = (x1 + x2) // 2
    midY = (y1 + y2) // 2
     
    plt.scatter(midY, midX)

    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title("Bresenham's Line")
    plt.show()


def main():

    color = "b."

    x1 = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
    st.write('Values:', x1)

    y1 = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
    st.write('Values:', y1)

    x2 = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
    st.write('Values:', x2)

    y2 = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
    st.write('Values:', y2)

   
    
    color = "y."
    bresenhamLine(x1, y1, x2, y2, color)

if __name__ == '__main__':
    main()