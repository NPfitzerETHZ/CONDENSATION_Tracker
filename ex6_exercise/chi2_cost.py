import numpy as np


def chi2_cost(hist_x, hist):
    hist_x = np.array(np.concatenate(hist_x).flat)
    hist = np.array(np.concatenate(hist).flat)

    dist = 1/2*np.sum( (hist_x-hist)**2 / (hist_x+hist + 1e-8) )
    return dist