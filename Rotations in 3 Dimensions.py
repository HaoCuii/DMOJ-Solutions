import math
t = int(input())

for i in range(t):
    p1, p2, p3, o1, o2, o3, theta = map(float, input().split())


    magnitude = math.sqrt(o1**2 + o2**2 + o3**2)
    o1 /= magnitude
    o2 /= magnitude
    o3 /= magnitude

    dot_product = p1 * o1 + p2 * o2 + p3 * o3

    def Rodrigues(x, y, z):

        cross_product_x = o2 * z - o3 * y
        cross_product_y = o3 * x - o1 * z
        cross_product_z = o1 * y - o2 * x

        rotated_x = (x * math.cos(theta) +
                     cross_product_x * math.sin(theta) +
                     o1 * dot_product * (1 - math.cos(theta)))
        
        rotated_y = (y * math.cos(theta) +
                     cross_product_y * math.sin(theta) +
                     o2 * dot_product * (1 - math.cos(theta)))
        
        rotated_z = (z * math.cos(theta) +
                     cross_product_z * math.sin(theta) +
                     o3 * dot_product * (1 - math.cos(theta)))
        
        return rotated_x, rotated_y, rotated_z

    rotated_p1, rotated_p2, rotated_p3 = Rodrigues(p1, p2, p3)
    print(f"{rotated_p1:.6f} {rotated_p2:.6f} {rotated_p3:.6f}")
