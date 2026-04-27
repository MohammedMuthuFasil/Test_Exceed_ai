/**
 * @fileoverview Input validation utility functions for common data formats.
 * Generated using GitHub Copilot AI with regex-based validation patterns.
 * @module validation-helpers
 */

/**
 * Validate an email address against a standard pattern.
 * @param {string} email - The email string to validate
 * @returns {boolean} True if the email matches the expected format
 */
function isValidEmail(email) {
  const pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return pattern.test(email);
}

/**
 * Check if a string is a valid URL (http or https).
 * @param {string} url - The URL string to validate
 * @returns {boolean} True if valid URL format
 */
function isValidURL(url) {
  try {
    const parsed = new URL(url);
    return ['http:', 'https:'].includes(parsed.protocol);
  } catch {
    return false;
  }
}

/**
 * Check if a password meets strength requirements.
 * Requires: 8+ chars, uppercase, lowercase, digit, special char.
 * @param {string} pwd - The password to check
 * @returns {boolean} True if password is strong
 */
function isStrongPassword(pwd) {
  if (pwd.length < 8) return false;
  if (!/[A-Z]/.test(pwd)) return false;
  if (!/[a-z]/.test(pwd)) return false;
  if (!/[0-9]/.test(pwd)) return false;
  if (!/[!@#$%^&*()_+\-=\[\]{}|;':",.<>?/`~]/.test(pwd)) return false;
  return true;
}

/**
 * Check if a value is a non-negative integer.
 * @param {*} val - Value to check
 * @returns {boolean} True if val is an integer >= 0
 */
function isNonNegativeInt(val) {
  return Number.isInteger(val) && val >= 0;
}

module.exports = { isValidEmail, isValidURL, isStrongPassword, isNonNegativeInt };
