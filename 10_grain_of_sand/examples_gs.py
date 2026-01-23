# Estimate how many grains of sand fit into a sphere of radius r (in meters).
# Assumes one grain ≈ sphere of diameter 1 mm.

import math

# Volume of one grain of sand in cubic millimeters
grain_volume_mm3 = 1 / 1000  # 1000 grains = 1 mm³

LOG10_2 = math.log10(2)
LY = 9.4607e15  # light-year in meters

def grains_in_sphere(radius_m):
    radius_mm = radius_m * 1000
    sphere_volume_mm3 = (4/3) * math.pi * radius_mm**3
    return sphere_volume_mm3 / grain_volume_mm3

def sphere_volume_m3(radius_m):
    return (4/3) * math.pi * radius_m**3

def entropy_bits(num_grains):
    return math.log10(num_grains) / LOG10_2


cases = [
    ("Sphere r = 1 m", 1),
    ("Earth", 6_371_000),
    ("Earth–Sun distance", 1.496e11),
    ("Sun–Neptune distance", 4.5e12),
    ("Light-year (diameter 1 ly)", 0.5 * LY),
    ("Galaxy (diameter 1000 ly)", 500 * LY),
]

print(f"{'Description':<28} {'radius/distance [m]':>22} {'value [m³]':>15} {'[gs]':>15} {'entropy [bit]':>15}")
print("-" * 105)

for desc, r in cases:
    vol_m3 = sphere_volume_m3(r)
    gs = grains_in_sphere(r)
    bits = entropy_bits(gs)

    print(
        f"{desc:<28} "
        f"{r:>22.3e} "
        f"{vol_m3:>15.3e} "
        f"{gs:>15.3e} "
        f"{bits:>15.2f}"
    )

    """
    Description                     radius/distance [m]      value [m³]            [gs]   entropy [bit]
---------------------------------------------------------------------------------------------------------
Sphere r = 1 m                            1.000e+00       4.189e+00       4.189e+12           41.93
Earth                                     6.371e+06       1.083e+21       1.083e+33          109.74
Earth–Sun distance                        1.496e+11       1.402e+34       1.402e+46          153.30
Sun–Neptune distance                      4.500e+12       3.817e+38       3.817e+50          168.03
Light-year (diameter 1 ly)                4.730e+15       4.434e+47       4.434e+59          198.14
Galaxy (diameter 1000 ly)                 4.730e+18       4.434e+56       4.434e+68          228.04
"""

