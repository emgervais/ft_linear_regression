import numpy as np
import matplotlib.pyplot as plt
import math
import os
import csv
import signal
import sys

def getFile():
    with open('data.csv', 'r') as file:
        file_contents = file.read()
    return file_contents

def parse(content):
    mileage = []
    price = []
    lines = content.strip().split('\n')
    for line in lines[1:]:
        km, price_val = map(float, line.split(','))
        mileage.append(km)
        price.append(price_val)
    return np.array(price), np.array(mileage)

def getData():
    content = getFile()
    return parse(content)

def norm(mileages, prices):
    x_min = min(mileages)
    x_max = max(mileages)
    y_min = min(prices)
    y_max = max(prices)

    norm_x = [(x - x_min) / (x_max - x_min) for x in mileages]
    norm_y = [(y - y_min) / (y_max - y_min) for y in prices]
    return np.array(norm_x), np.array(norm_y)

def linear_regression(mileages, prices, learning_rate, num_iterations):
    theta_0 = 0
    theta_1 = 0
    m = len(mileages)
    for i in range(num_iterations):
        predictions = theta_0 + (theta_1 * mileages)
        errors = predictions - prices
        theta_0_gradient = np.sum(errors) / m
        theta_1_gradient = np.sum(errors * mileages) / m
        theta_0 -= learning_rate * theta_0_gradient
        theta_1 -= learning_rate * theta_1_gradient
        # learning_rate *= 1 / (1 + 0.1 * i)

        plt.scatter(mileages, prices, color='blue', label='Data Points')
        plt.plot(mileages, theta_0 + theta_1 * mileages, color='red', label='Regression Line')
        plt.xlabel('Mileage')
        plt.ylabel('Price')
        plt.title('Linear Regression')
        plt.pause(0.1)
        plt.clf()
    return theta_0, theta_1

def signal_handler(sig, frame):
    print("Exiting gracefully...")
    plt.close('all')
    sys.exit(0)

def save_parameters(theta_0, theta_1):
    with open('theta.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([theta_0, theta_1])

def	main():
    signal.signal(signal.SIGINT, signal_handler)
    learning_rate = 0.5
    num_iterations = 100
    price, mileage = getData()
    x, y = norm(mileage, price)
    theta_0, theta_1 = linear_regression(x, y, learning_rate, num_iterations)
    save_parameters(theta_0, theta_1)

if __name__ == "__main__":
	main()

