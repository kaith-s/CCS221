# Members:
#  Car Torres 
#  Thea Kaith Franchette Selerio
#  Margaux Oriana Gasis



import matplotlib.pyplot as plt

def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

    #calculate steps required for generating pixels

    steps = abs(dx) if abs(dx) > abs (dy) else abs(dy)

    #calculate increment in x & y for each steps

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    for i in range(0, int(steps +1 )):

        #draw pixels

        plt.plot(int(x1), int (y1), color)
        x1 += Xinc
        y1 += Yinc
    
    midX = (x1 + x2) // 2
    midY = (y1 + y2) // 2
     
    plt.scatter(midY, midX, color = 'red') 
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')    
    plt.title("DDALine")
    plt.show()

