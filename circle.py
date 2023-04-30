'''
Author: Jack Ford
KUID: 3067365
Date: 11/17/21
Lab: Lab 10
Last modified: 12/1/21
Purpose: Circle class to calculate the circle statistics.
'''

from math import pi, sqrt

class Circle:
	def __init__(self, radius, xPos, yPos):
		self.radius = radius
		self.xPos = xPos
		self.yPos = yPos

	def diameter(self):
		return 2 * self.radius

	def area(self):
		return pi * (self.radius ** 2)

	def circumference(self):
		return 2 * pi * self.radius

	def dist_to_origin(self):
		return sqrt((self.xPos ** 2) + (self.yPos ** 2))

	def intersect(self, other_circle):
		dist = sqrt(((self.xPos - other_circle.xPos) ** 2) + ((self.yPos - other_circle.yPos) ** 2))

		if dist <= (self.radius + other_circle.radius):
			return True

		return False

	def intersectCount(self, other_circle):
		dist = sqrt(((self.xPos - other_circle.xPos) ** 2) + ((self.yPos - other_circle.yPos) ** 2))

		if dist == 0:
			if self.radius == other_circle.radius:
				return 'infinite'

			else:
				return 0

		if dist < (self.radius + other_circle.radius):
			if self.radius > other_circle.radius:
				r1 = self.radius
				r2 = other_circle.radius

			else:
				r1 = other_circle.radius
				r2 = self.radius

			if (dist + r2) < r1:
				return 0

			if (dist + r2) == r1:
				return 1

			if (dist + r2) > r1:
				return 2

			return 2

		if dist == (self.radius + other_circle.radius):
			return 1

		if dist > (self.radius + other_circle.radius):
			return 0
