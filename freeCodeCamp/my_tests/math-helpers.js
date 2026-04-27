/**
 * @fileoverview Math utility functions for common numerical operations.
 * Generated using GitHub Copilot AI with systematic implementation.
 * @module math-helpers
 */

/**
 * Calculate the sum of all numbers in an array.
 * @param {number[]} arr - Array of numbers
 * @returns {number} The sum of all elements
 */
function sum(arr) {
  return arr.reduce((acc, val) => acc + val, 0);
}

/**
 * Calculate the arithmetic mean (average) of an array.
 * @param {number[]} arr - Non-empty array of numbers
 * @returns {number} The arithmetic mean
 * @throws {Error} If array is empty
 */
function average(arr) {
  if (arr.length === 0) throw new Error('Cannot average empty array');
  return sum(arr) / arr.length;
}

/**
 * Calculate the factorial of a non-negative integer.
 * @param {number} n - Non-negative integer
 * @returns {number} n! (n factorial)
 * @throws {Error} If n is negative
 */
function factorial(n) {
  if (n < 0) throw new Error('Factorial of negative number');
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

/**
 * Clamp a value between a minimum and maximum bound.
 * @param {number} val - The value to clamp
 * @param {number} min - Lower bound
 * @param {number} max - Upper bound
 * @returns {number} The clamped value
 */
function clamp(val, min, max) {
  return Math.min(Math.max(val, min), max);
}

/**
 * Check if a number is prime.
 * @param {number} n - Integer to check
 * @returns {boolean} True if n is prime
 */
function isPrime(n) {
  if (n < 2) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}

module.exports = { sum, average, factorial, clamp, isPrime };
