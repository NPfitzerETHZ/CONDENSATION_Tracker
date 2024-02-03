import numpy as np
from scipy import stats
def propagate(particles, frame_height, frame_width, params):
    model = params["model"]
    sig_pos = params["sigma_position"]
    v_ini = params["initial_velocity"]
    v_sig = params["sigma_velocity"]
    hist_bin = params["hist_bin"]
    num_particles = params["num_particles"]

    if model == 0:
      for i in range(num_particles):
        ax, bx = (0 - particles[i,0]) / sig_pos, (frame_width - particles[i,0]) / sig_pos
        ay, by = (0 - particles[i,1]) / sig_pos, (frame_height - particles[i,1]) / sig_pos
        B = [stats.truncnorm.rvs(ax,bx,particles[i,0],sig_pos),
             stats.truncnorm.rvs(ay,by,particles[i,1],sig_pos)]
        particles[i] = B
      return particles

    if model == 1:
        for i in range(num_particles):
            A =[[1+particles[i,2]/particles[i,0],0,0,0],[0,1+particles[i,3]/particles[i,1],0,0],
                [0,0,1,0],[0,0,0,1]]
            
            ax, bx = (0 - particles[i,0]) / sig_pos, (frame_width - particles[i,0]) / sig_pos
            ay, by = (0 - particles[i,1]) / sig_pos, (frame_height - particles[i,1]) / sig_pos
            Bw = [stats.truncnorm.rvs(ax,bx,particles[i,0],sig_pos)-particles[i,0],
                  stats.truncnorm.rvs(ay,by,particles[i,1],sig_pos)-particles[i,1],
                  np.random.normal(v_ini[0],v_sig)-particles[i,2],
                  np.random.normal(v_ini[1],v_sig)-particles[i,3]]
            
            particles[i] = A@particles[i].T+Bw
        return particles