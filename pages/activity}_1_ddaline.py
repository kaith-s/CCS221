# Members:
#  Car Torres 
#  Thea Kaith Franchette Selerio
#  Margaux Oriana Gasis



import matplotlib.pyplot as plt
import streamlit as st


def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

    #calculate steps required for generating pixels

    steps = abs(dx) if abs(dx) > abs (dy) else abs(dy)

    #calculate increment in x & y for each steps

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    

    fig,ax=plt.subplots()
    for i in range(0, int(steps +1 )):

        #draw pixels

        ax.plot(int(x1), int (y1), color)
        x1 += Xinc
        y1 += Yinc
        
    
    midX = (x1 + x2) // 2
    midY = (y1 + y2) // 2
    ax.plot(midX, midY, marker='o', markerfacecolor="green")
     
    
    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")

    st.pyplot(fig)

def main():
    st.sidebar.title("Select Algorithm")
    algorithm = st.sidebar.selectbox("Select Algorithm", ("DDA", "Bresenham"))

    x1 = st.sidebar.number_input("Enter the Starting point of x:")
    y1 = st.sidebar.number_input("Enter the Starting point of y:")
    x2 = st.sidebar.number_input("Enter the end point of x:")
    y2 = st.sidebar.number_input("Enter the end point of y:")

    if algorithm == "DDA":  
        color ="r."
        DDALine(x1, y1, x2, y2, color)

main()


