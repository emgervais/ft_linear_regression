import math
import csv
import sys
import os
from train import getData

def norm(mileages, mileage):
	x_min = min(mileages)
	x_max = max(mileages)

	return (mileage - x_min) / (x_max - x_min)

def denorm(prices, price):
	x_min = min(prices)
	x_max = max(prices)
	return price * (x_max - x_min) + x_min

def	estimatePrice(thetas, mileage, mileages, prices):
	price = thetas[1] * norm(mileages, mileage) + thetas[0]
	if thetas[1] == 0 and thetas[0] == 0:
		return 0
	return (denorm(prices, price))
	
def	getMileage():
	while 1:
		print('Please enter a mileage: ')
		try:
			mileage = input()
		except EOFError:
			sys.exit('EOF')
		except:
			sys.exit('Error')
		try:
			mileage = int(mileage)
			if mileage >= 0:
				break
			else:
				print('Please enter a valid mileage')
		except ValueError:
			print('Please enter a valid mileage')
	return (mileage)

def	getThetas(thetas):
	t0, t1 = 0, 0
	try:
		with open(thetas, 'r') as csvfile:
			file = csv.reader(csvfile, delimiter=',')
			for row in file:
				t0 = float(row[0])
				t1 = float(row[1])
				break
	except:
		print('Using default value as algo wasnt trained.')
	return (t0, t1)

def	main():
	thetas = getThetas('theta.csv')
	mileage = getMileage()
	prices, mileages = getData()
	price = estimatePrice(thetas, mileage, mileages, prices)
	print('The price for this mileage is: ', format(price, '.2f'))

if __name__ == "__main__":
	main()
