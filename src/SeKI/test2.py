import numpy as np

class SingleLayerPerceptron:
    def _init_(self):
        # Initialize the weights and the bias to random values
        self.weights = np.random.rand(2)
        self.bias = np.random.rand(1)
        self.learning_rate = 0.01

    def predict(self, inputs):
        # Simple weighted sum of inputs + bias
        return np.dot(inputs, self.weights) + self.bias

    def train(self, training_data):
        # Train the perceptron using the training data
        for _ in range(100):  # Number of epochs
            for inputs, expected in training_data:
                prediction = self.predict(inputs)
                error = expected - prediction
                # Adjust weights and bias based on the error and learning rate
                self.weights += self.learning_rate * error * inputs
                self.bias += self.learning_rate * error

# Training data for the "add" function
add_training_data = [
    (np.array([1, 2]), 3),
    (np.array([4, 5]), 9),
    (np.array([2, 3]), 5),
    (np.array([6, 7]), 13),
    (np.array([3, 5]), 8),
]

# Training data for the "multiply" function
multiply_training_data = [
    (np.array([1, 2]), 2),
    (np.array([2, 3]), 6),
    (np.array([3, 4]), 12),
    (np.array([4, 5]), 20),
    (np.array([5, 6]), 30),
]

# Create a perceptron instance
perceptron = SingleLayerPerceptron()

# Train on the "add" function
perceptron.train(add_training_data)
print("After training on addition:")
for inputs, _ in add_training_data:
    print(f"{inputs} -> {perceptron.predict(inputs)}")

# Reinitialize the perceptron for multiplication training
perceptron = SingleLayerPerceptron()

# Train on the "multiply" function
perceptron.train(multiply_training_data)
print("\nAfter training on multiplication:")
for inputs, _ in multiply_training_data:
    print(f"{inputs} -> {perceptron.predict(inputs)}")