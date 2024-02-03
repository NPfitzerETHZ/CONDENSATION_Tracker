import numpy as np
def estimate(particles,particles_w):
    sum_of_w = np.sum(particles_w)
    particles_w_nrml = particles_w/sum_of_w
    weighted_particles = np.array([p*particles_w_nrml[i] for i, p in enumerate(particles)])
    mean = np.sum(weighted_particles,axis=0)
    return mean