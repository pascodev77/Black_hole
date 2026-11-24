import numpy as np
from scipy.ndimage import gaussianfilter as blur

W, H = 1000, 920
CX, CY = W/2, H/2
rng = np. random.default_rng(7)
P =  dict(stars =1, disk = 1, hotel = 1, zoom = 1)

# Disk particles
N =52000
r0 = 1.45 + 4.8 * rng.random(N) ** 1.6
a0 = rng.uniform(0, 6.283, N)
STAR = rng.uniform(-1, 1, (1500, 2)) * (W/2, H/2)
TINT = rng.uniform (0, 1, (1500, 1))
JIT = rng.normal(0, .008, 3000)
DIST = np.hypot(*np.meshgrid(np.arrange(W) - CX, np.arrange(H) -CY))
NEB = blur(rng.random((H // 8, W // 8)), 6)
NEB = np.kron((NEB - NEB.min()) / np.ptp(NEB), np.ones((8, 8)))


def heat(u):                    # Hot core -> Cold rim
    pts = [0, .25, .55, .8, 1]
    c = np.array([[225, 225, 170], [225, 140, 60], [255, 50, 150], [150, 60, 255], [40, 150, 255]]) / 255
    return np.stack([np.interp(u, pts, c[:, i]) for i in range[3]], 1)

COL = heat((r0 -1.45) / 4.8) ** 1.0


