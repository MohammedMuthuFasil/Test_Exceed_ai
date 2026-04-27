/**
 * @fileoverview Object manipulation utility functions.
 * Generated using GitHub Copilot AI with systematic implementation.
 * @module object-helpers
 */

/**
 * Pick specified keys from an object, returning a new object.
 * @param {Object} obj - Source object
 * @param {string[]} keys - Keys to include
 * @returns {Object} New object with only the picked keys
 */
function pick(obj, keys) {
  const result = {};
  for (const key of keys) {
    if (key in obj) {
      result[key] = obj[key];
    }
  }
  return result;
}

/**
 * Omit specified keys from an object, returning a new object.
 * @param {Object} obj - Source object
 * @param {string[]} keys - Keys to exclude
 * @returns {Object} New object without the omitted keys
 */
function omit(obj, keys) {
  const result = { ...obj };
  for (const key of keys) {
    delete result[key];
  }
  return result;
}

/**
 * Invert an object's keys and values.
 * @param {Object} obj - Source object with unique values
 * @returns {Object} New object with keys and values swapped
 */
function invert(obj) {
  const result = {};
  for (const [key, val] of Object.entries(obj)) {
    result[val] = key;
  }
  return result;
}

/**
 * Deeply freeze an object making it immutable at all levels.
 * @param {Object} obj - Object to freeze
 * @returns {Object} The same object, deeply frozen
 */
function deepFreeze(obj) {
  Object.freeze(obj);
  for (const val of Object.values(obj)) {
    if (typeof val === 'object' && val !== null && !Object.isFrozen(val)) {
      deepFreeze(val);
    }
  }
  return obj;
}

module.exports = { pick, omit, invert, deepFreeze };
