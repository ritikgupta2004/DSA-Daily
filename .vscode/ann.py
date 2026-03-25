import numpy as np

class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train(self, patterns):
        patterns = np.array(patterns)
        for p in patterns:
            p = p.reshape(self.size, 1)  # column vector
            self.weights += np.dot(p, p.T)
        np.fill_diagonal(self.weights, 0)  # no self-connection

    def recall(self, pattern, steps=10):
        pattern = np.array(pattern).copy()
        for _ in range(steps):
            for i in range(self.size):
                raw = np.dot(self.weights[i], pattern)
                pattern[i] = 1 if raw >= 0 else -1
        return pattern

# ---------------------------
# Example usage
# ---------------------------
if __name__ == "__main__":
    # Training patterns (bipolar: -1 and +1)
    patterns = [
        [1, -1, 1, -1, 1, -1, 1, -1],   # Pattern 1
        [1, 1, -1, -1, 1, 1, -1, -1]    # Pattern 2
    ]

    hopfield = HopfieldNetwork(size=8)
    hopfield.train(patterns)

    # Distorted input (noisy version of Pattern 1)
    test_pattern = [1, -1, 1, -1, -1, -1, 1, -1]

    recalled_pattern = hopfield.recall(test_pattern)

    print("Input Pattern:    ", test_pattern)
    print("Recalled Pattern: ", recalled_pattern.tolist())
