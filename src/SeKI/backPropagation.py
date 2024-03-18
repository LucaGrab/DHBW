import numpy as np

class Perceptron:
    def __init__(self):
        # Initialize weights and bias randomly
        self.weights = np.random.rand(2)
        self.bias = np.random.rand(1)

    def sigmoid(self, x):
        # Sigmoid activation function
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        # Derivative of the sigmoid activation function
        return x * (1 - x)

    def predict(self, inputs): #glaube hier ist was falsch
        # Forward pass
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        return self.sigmoid(weighted_sum)

    def train(self, training_data, epochs=1000, learning_rate=0.05):
        for epoch in range(epochs):
            for inputs, target in training_data:
                # Forward pass
                predicted_output = self.predict(inputs)

                # Calculate error
                error = target - predicted_output

                # Backpropagation
                adjustment = error * self.sigmoid_derivative(predicted_output)
                self.weights += learning_rate * adjustment * inputs
                self.bias += learning_rate * adjustment

            # Print the mean squared error for every 100 epochs
            if epoch % 100 == 0:
                mse = np.mean(np.square(np.array([self.predict(inputs) for inputs, _ in training_data]) - np.array([target for _, target in training_data])))
                print(f"Epoch {epoch}, Mean Squared Error: {mse}")
                print("weights", self.weights)

# Training data for the "add" function
training_data = [((1, 1), 2), ((0.5, 0.5), 1.0),((1,3),4),((3,1),4)]

# Create a perceptron
perceptron = Perceptron()

# Train the perceptron
perceptron.train(training_data, epochs=1000)

# Test the trained perceptron
print("Testing the trained perceptron:")
for inputs, target in training_data:
    prediction = perceptron.predict(inputs)
    print(f"Inputs: {inputs}, Target: {target}, Predicted: {prediction[0]:.3f}")
