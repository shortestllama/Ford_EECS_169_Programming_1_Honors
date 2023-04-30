'''
Author: Jack Ford
KUID: 3067365
Date: 12/1/21
Lab: Lab 11
Last modified: 12/8/21
Purpose: Initialize a DriversLicense object and perform actions on said object
'''

class DriversLicense:
	def __init__(self, first_name, last_name, age, is_voter, license_num):
		self._first_name = first_name
		self._last_name = last_name
		self._age = age
		self._is_voter = is_voter
		self._license_num = license_num

	def get_first_name(self):
		return self._first_name

	def get_last_name(self):
		return self._last_name

	def get_age(self):
		return self._age

	def get_is_voter(self):
		return self._is_voter

	def get_license_num(self):
		return self._license_num

	def set_first_name(self, first_name):
		self._first_name = first_name

	def set_last_name(self, last_name):
		self._last_name = last_name

	def set_age(self, age):
		self._age = age

	def set_is_voter(self, is_voter):
		self._is_voter = is_voter

	def set_license_num(self, license_num):
		self._license_num = license_num

	def __eq__(self, other):
		return self._license_num == other._license_num

	def __ne__(self, other):
		return not(self == other)

	def __str__(self):
		return f'{self._last_name}, {self._first_name} ({self._age}): {self._license_num}'
