# Perceptron o ciągłej funkcji aktywacji
import math


class Perceptron2:
    def __init__(self, n, alpha):
        self.n = n
        self.alpha = alpha
        self.weights = []

        for i in range(n):
            self.weights.append(0.0)


    def compute(self, x):
        net = 0.0
        x = self.normalise(x)
        for i in range(len(x)):
            net += x[i] * self.weights[i]
        return net

    def learn(self, d, x):
        x = self.normalise(x)
        y = self.compute(x)
        for i in range(len(x)):
            self.weights[i] += self.alpha * x[i] * self.error_value(y, d)
        self.weights = self.normalise(self.weights)


    def normalise(self, vec):
        norm = 0
        for i in range(len(vec)):
            norm += vec[i]**2
        norm = math.sqrt(norm)
        for i in range(len(vec)):
            vec[i] /= norm
        return vec

    def error_value(self, x, d):
        return 0.5 * (d - x)**2