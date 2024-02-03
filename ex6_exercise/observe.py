from color_histogram import color_histogram
from chi2_cost import chi2_cost
import numpy as np

def observe(particles, frame, bbox_height, bbox_width,hist_bin, hist, sigma_observe):
    particles_w = []
    chi2_distances = []
    for p in particles:
        xc,yc = p[0],p[1]
        xmin = int(xc-bbox_width/2)
        ymin = int(yc-bbox_height/2)
        xmax = int(xc+bbox_width/2)
        ymax = int(yc+bbox_height/2)
        p_hist = color_histogram(xmin,ymin,xmax,ymax,frame,hist_bin)
        chi2_dist = chi2_cost(p_hist,hist)
        p_w = 1/(np.sqrt(2*np.pi)*sigma_observe)*np.exp(-1/2*(chi2_dist/sigma_observe)**2)
        particles_w.append([p_w])
        chi2_distances.append(chi2_dist)
    return np.array(particles_w)
