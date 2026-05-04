"""Basic AI-oriented algorithms for testing and learning.

This module keeps the implementations lightweight and dependency-free so they
can be validated with plain pytest in the current repository.
"""


def euclidean_distance(point_a, point_b):
    """Return the Euclidean distance between two numeric vectors."""
    if len(point_a) != len(point_b):
        raise ValueError("Points must have the same number of dimensions")

    squared_distance = 0
    for coord_a, coord_b in zip(point_a, point_b):
        difference = coord_a - coord_b
        squared_distance += difference * difference
    return squared_distance ** 0.5


def knn_classify(training_data, candidate_point, k=3):
    """Classify a point using the k-nearest neighbors algorithm.

    The training_data argument must contain tuples in the form:
    ((feature_1, feature_2, ...), label)
    """
    if not training_data:
        raise ValueError("training_data must not be empty")
    if k <= 0:
        raise ValueError("k must be greater than zero")
    if k > len(training_data):
        raise ValueError("k cannot be greater than the training set size")

    ranked_neighbors = sorted(
        training_data,
        key=lambda item: euclidean_distance(item[0], candidate_point)
    )
    label_counts = {}
    for _, label in ranked_neighbors[:k]:
        label_counts[label] = label_counts.get(label, 0) + 1

    return sorted(
        label_counts.items(),
        key=lambda item: (-item[1], item[0])
    )[0][0]


def fit_linear_regression(samples):
    """Fit a simple linear regression model and return slope and intercept."""
    if len(samples) < 2:
        raise ValueError("At least two samples are required")

    x_values = [sample[0] for sample in samples]
    y_values = [sample[1] for sample in samples]

    x_mean = sum(x_values) / len(x_values)
    y_mean = sum(y_values) / len(y_values)

    numerator = sum(
        (x_value - x_mean) * (y_value - y_mean)
        for x_value, y_value in samples
    )
    denominator = sum(
        (x_value - x_mean) ** 2 for x_value in x_values
    )

    if denominator == 0:
        raise ValueError("Cannot fit a vertical line")

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    return slope, intercept


def predict_linear_regression(model, x_value):
    """Predict a y value using a fitted linear regression model."""
    slope, intercept = model
    return slope * x_value + intercept


def train_perceptron(samples, labels, epochs=20, learning_rate=0.1):
    """Train a binary perceptron and return weights and bias.

    Labels must be 0 or 1.
    """
    if not samples:
        raise ValueError("samples must not be empty")
    if len(samples) != len(labels):
        raise ValueError("samples and labels must have the same length")

    feature_count = len(samples[0])
    weights = [0.0] * feature_count
    bias = 0.0

    for _ in range(epochs):
        for features, label in zip(samples, labels):
            prediction = perceptron_predict((weights, bias), features)
            error = label - prediction
            for index, value in enumerate(features):
                weights[index] += learning_rate * error * value
            bias += learning_rate * error

    return weights, bias


def perceptron_predict(model, features):
    """Predict a binary class with a perceptron model."""
    weights, bias = model
    activation = bias
    for weight, value in zip(weights, features):
        activation += weight * value
    return 1 if activation >= 0 else 0