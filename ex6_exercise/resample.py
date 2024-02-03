from random import choices
from numpy import array,ndarray
def resample(particles,particles_w):
    particles = ndarray.tolist(particles)
    particles_w = ndarray.tolist(particles_w)
    p_and_w = array([p + particles_w[i] for i, p in enumerate(particles)])
    p_and_w = array(choices(p_and_w,weights=p_and_w[:,-1],k=len(particles)))
    particles = p_and_w[:,0:-1]
    particles_w = p_and_w[:,-1]
    return particles,particles_w