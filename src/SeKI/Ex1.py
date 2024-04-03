import numpy as np

class Perceptron:
    def __init__(self):
        # Randomly initialize weights and bias
        self.weights = np.random.rand(2)
        self.bias = np.random.rand(1)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def predict(self, inputs):
        # Calculate weighted sum and apply activation function
        return self.sigmoid(np.dot(inputs, self.weights) + self.bias)

    def train(self, training_data, learning_rate=0.1, epochs=10000):
        for epoch in range(epochs):
            for inputs, target in training_data:
                # Forward pass
                output = self.predict(inputs)

                # Calculate the error
                error = target - output

                # Update weights and bias using backpropagation
                self.weights += learning_rate * error * inputs * self.sigmoid_derivative(output)
                self.bias += learning_rate * error * self.sigmoid_derivative(output)

            # Print the error for every 1000 epochs
            if epoch % 1000 == 0:
                print(f"Epoch {epoch}, Error: {error}")

# Training data for the "add" function
add_training_data = [
    (np.array([0, 2]), 2),
    (np.array([0, 5]), 5),
    (np.array([5, 5]), 0),
    (np.array([10, 2]), 12),
    (np.array([0, 1]), 1),
    (np.array([3, 0]), 3),
    (np.array([5, 2]), 7),
    (np.array([10, 20]), 30)
]

# Create and train the perceptron for the "add" function
add_perceptron = Perceptron()
print("Training for the 'add' function:")
add_perceptron.train(add_training_data)

# Reset perceptron for the "multiply" function
add_perceptron = Perceptron()

# Training data for the "multiply" function
multiply_training_data = [
    (np.array([0, 0]), 0),
    (np.array([0, 1]), 0),
    (np.array([1, 0]), 0),
    (np.array([1, 1]), 1)
]

# Train the perceptron for the "multiply" function
print("\nTraining for the 'multiply' function:")
add_perceptron.train(multiply_training_data)

# Test the trained MLP
# Training data for the "add" function
add_test_data = [
    (np.array([0, 2]), 2),
    (np.array([1, 5]), 6),
    (np.array([1, 3]), 4),
    (np.array([1, 1]), 2)
]
print("Testing the trained MLP:")
for inputs, target in add_test_data:
    prediction = add_perceptron.predict(inputs)
    print(f"Inputs: {inputs}, Target: {target}, Predicted: {prediction[0]:.3f}")
