# obtain the surface area of a prism . 

a = float(input("Enter the a of the hexagonal prism: "))
h = float (input("Enter the h of the hexagonal prism "))

from math import sqrt  
def find_area_of_Hexagonal_prism(a, h):  
    return ( (6 * a * h) + (3 * sqrt(3) * a * a)) # area value.  
   
    
print(find_area_of_Hexagonal_prism(a, h) )  
