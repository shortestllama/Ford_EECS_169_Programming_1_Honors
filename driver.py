'''
Author: Jack Ford
KUID: 30637365
Date: 11/17/21
Lab: lab 10
Last modified: 12/1/21
Purpose: Get circle information from the user and print out circle statistics.
'''

from circle import Circle
#or: import circle, but then need to say circle.Circle or something

def user_circle():
	print("Enter information for Circle:")
	radius = float(input("Radius: "))
	xPos = float(input("X Position: "))
	yPos = float(input("Y Position: "))
	return Circle(radius, xPos, yPos)

def print_circle_info(circ, name="Circle"):
	print(f"Information for {name}:")
	print(f"location: ({circ.xPos}, {circ.yPos})")
	print(f"diameter: {circ.diameter()}")
	print(f"area: {circ.area()}")
	print(f"circumference: {circ.circumference()}")
	print(f"distance from the origin: {circ.dist_to_origin()}")

def main():
	circle1 = user_circle()
	circle2 = user_circle()
	print_circle_info(circle1, "Circle 1")
	print_circle_info(circle2, "Circle 2")
	print(f"Circle 1 intersects Circle 2 {circle1.intersectCount(circle2)} time(s).")

main()
