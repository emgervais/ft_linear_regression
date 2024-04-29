<h1>Car Price Prediction with Linear Regression</h1>

  <h2>Objective</h2>
  <p>The aim of this project is to introduce me to the basic concept behind machine learning. I will create a program that predicts the price of a car using a linear function trained with a gradient descent algorithm. While a specific example is provided for this project, the algorithm can be applied to any other dataset.</p>

  <h2>General Instructions</h2>
  <p>In this project, I was free to use any programming language and libraries as long as they do not perform all the work for you. The use of pre-built functions like numpy's polyfit is considered cheating</p>

  <h2>Mandatory Part</h2>
  <p>I implement a simple linear regression with a single feature - in this case, the mileage of the car.</p>
  <p>To do so, I need to create two programs:</p>
  <ul>
    <li><strong>Prediction Program:</strong> This program predicts the price of a car for a given mileage. It prompts the user for a mileage input and returns the estimated price using the following hypothesis:
      <code>estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)</code></li>
    <li><strong>Training Program:</strong> This program reads the dataset file and performs linear regression on the data. It saves the calculated theta0 and theta1 for use in the prediction program using the following formulas:
      <pre>
        tmpθ0 = learningRate * (1 / m) * Σ (estimatePrice(mileage[i]) - price[i])
        tmpθ1 = learningRate * (1 / m) * Σ (estimatePrice(mileage[i]) - price[i]) * mileage[i]
      </pre>
      <p>where m is the number of data points in the dataset.</p>
    </li>
  </ul>
  <h2>How to Use</h2>
  <ol>
    <li>Clone or download this repository.</li>
    <li>Run the training program to train the model using your dataset.</li>
    <li>Use the prediction program to estimate the price of a car for a given mileage.</li>
  </ol>
