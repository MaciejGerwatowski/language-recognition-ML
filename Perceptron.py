import random


class Perceptron:
    def __init__(self, n, alpha, beta):
        self.n = n
        self.alpha = alpha
        self.beta = beta
        self.weights = []
        self.threshold = 0.0

        for i in range(n):
            self.weights.append(0.0)

    def compute(self, x):
        sum = 0
        for i in range(len(x)):
            sum += self.weights[i] * x[i]

        if (sum >= self.threshold):
            return 1
        return 0

    def learn(self, d, x):
        y = self.compute(x)
        for i in range(len(x)):
            self.weights[i] = self.weights[i] + (d - y) * self.alpha * x[i]
        self.threshold = self.threshold + (d - y) * self.beta * (-1)
