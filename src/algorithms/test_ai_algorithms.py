"""Tests for small AI-oriented algorithms.

These examples are intended to be easy to run in the current repository while
still being realistic enough for code-generation and test-validation workflows.
"""

import pytest

from ai_algorithms import (
    euclidean_distance,
    fit_linear_regression,
    knn_classify,
    perceptron_predict,
    predict_linear_regression,
    train_perceptron,
)


def test_euclidean_distance_for_two_points():
    assert euclidean_distance((0, 0), (3, 4)) == 5.0


def test_euclidean_distance_dimension_mismatch_raises_error():
    with pytest.raises(ValueError):
        euclidean_distance((1, 2), (1, 2, 3))


def test_knn_classify_returns_expected_label():
    training_data = [
        ((1, 1), "safe"),
        ((1, 2), "safe"),
        ((8, 8), "risk"),
        ((9, 8), "risk"),
    ]

    assert knn_classify(training_data, (2, 2), k=3) == "safe"


def test_knn_rejects_invalid_k():
    training_data = [((1, 1), "safe")]

    with pytest.raises(ValueError):
        knn_classify(training_data, (1, 1), k=0)


def test_fit_linear_regression_returns_expected_model():
    model = fit_linear_regression([(1, 3), (2, 5), (3, 7), (4, 9)])

    slope, intercept = model
    assert slope == pytest.approx(2.0)
    assert intercept == pytest.approx(1.0)


def test_predict_linear_regression_uses_fitted_model():
    model = fit_linear_regression([(1, 3), (2, 5), (3, 7), (4, 9)])

    assert predict_linear_regression(model, 6) == pytest.approx(13.0)


def test_fit_linear_regression_rejects_vertical_line():
    with pytest.raises(ValueError):
        fit_linear_regression([(2, 1), (2, 3), (2, 5)])


def test_perceptron_learns_or_gate():
    samples = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
    ]
    labels = [0, 1, 1, 1]

    model = train_perceptron(samples, labels, epochs=25, learning_rate=0.2)

    predictions = [perceptron_predict(model, sample) for sample in samples]
    assert predictions == labels


def test_perceptron_rejects_mismatched_training_input():
    with pytest.raises(ValueError):
        train_perceptron([(0, 0), (1, 1)], [1])