import numpy as np

def color_histogram(xmin,ymin,xmax,ymax,frame,hist_bin):
    #hist_bin^3 list
    hist = [[[0 for _ in range(hist_bin)] for _ in range(hist_bin)] for _ in range(hist_bin)]
    fmaxx,fmaxy = frame.shape[1],frame.shape[0]
    bin_size = int(256/hist_bin)
    for i in range(ymin,ymax):
        for j in range(xmin,xmax):
            if i < fmaxy and j < fmaxx:
                p = frame[i,j,:]
                p_red = int(p[0]/bin_size)
                p_green = int(p[1]/bin_size)
                p_blue = int(p[2]/bin_size)
                hist[p_red][p_green][p_blue] +=1
    return np.array(hist)