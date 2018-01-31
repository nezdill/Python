#Arnez Dillard 2339394
#The circle module has functions that perform
#calculations related to circles.
import math
#The area function accepts a cicules radius as an
#argument and returns the area of the circle 
def get_radius_from_user():
    return float(input("Enter your radius: ")) #Receiving the radius
def get_diameter(radius):
    return radius * 2 #calculating diameter
def get_circumference(radius):
    return 2 * math.pi * radius #calculating circumference
def get_area(radius):
    return math.pi* radius * radius #calculating area
def show_results(radius):
    print("The Diameter is",get_diameter(radius)) #displaying the diameter
    print("The Circumference is",get_circumference(radius)) #displaying the circumeference
    print("The Area is" ,get_area(radius)) #displaying the area
show_results(get_radius_from_user())

