# Estimate how many grains of sand fit into a sphere of radius r (in meters).
# Assumes one grain ≈ sphere of diameter 1 mm.

import math

# Volume of one grain of sand in cubic millimeters
grain_volume_mm3 = 1 / 1000  # 1000 grains = 1 mm³

def grains_in_sphere(radius_m):
    """
    Calculate the number of grains of sand in a sphere.
    
    Parameters:
    radius_m : float
        Radius of the sphere in meters.
        
    Returns:
    float
        Number of grains of sand that fit into the sphere.
    """
    # Convert radius from meters to millimeters
    radius_mm = radius_m * 1000
    
    # Calculate volume of the sphere in cubic millimeters
    sphere_volume_mm3 = (4/3) * math.pi * radius_mm**3
    
    # Divide by volume of one grain to get total number of grains
    num_grains = sphere_volume_mm3 / grain_volume_mm3
    
    return num_grains

# Examples
r1 = 1             # radius = 1 meter
r2 = 6371000        # radius of Earth in meters
r3 = 1.496e11       # Earth-Sun distance in meters

# Print results in scientific notation with 2 decimal places
print("Grains in sphere with radius 1 m: {:.2e} [gs]".format(grains_in_sphere(r1)))
print("Grains in a sphere the size of Earth: {:.2e} [gs]".format(grains_in_sphere(r2)))
print("Grains in a sphere with radius Earth-Sun distance: {:.2e} [gs]".format(grains_in_sphere(r3)))

"""
Grains in sphere with radius 1 m: 4.19 e+12 [gs]
Grains in a sphere the size of Earth: 1.08 e+33 [gs]
Grains in a sphere with radius Earth-Sun distance: 1.40 e+46 [gs]
"""
