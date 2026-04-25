/**
 * @fileoverview Test suite for validation-helpers.js utility functions.
 * Generated using GitHub Copilot AI — covers email, URL, password,
 * and integer validation with systematic valid/invalid case pairs.
 */

const { isValidEmail, isValidURL, isStrongPassword, isNonNegativeInt } = require('./validation-helpers');

/**
 * Test runner with descriptive pass/fail logging.
 * @param {string} label - Test case description
 * @param {boolean} condition - Assertion result
 */
function test(label, condition) {
  if (!condition) {
    console.error(`  FAIL: ${label}`);
    process.exitCode = 1;
  } else {
    console.log(`  PASS: ${label}`);
  }
}

// ============================================================
// isValidEmail() — RFC-like email format validation
// ============================================================
console.log('\n--- isValidEmail() ---');

const emailTestCases = [
  { input: 'user@example.com',         expected: true,  desc: 'standard email' },
  { input: 'first.last@domain.org',    expected: true,  desc: 'dotted local part' },
  { input: 'user+tag@gmail.com',       expected: true,  desc: 'plus addressing' },
  { input: 'user@sub.domain.com',      expected: true,  desc: 'subdomain' },
  { input: 'userexample.com',          expected: false, desc: 'missing @ sign' },
  { input: 'user@',                    expected: false, desc: 'missing domain' },
  { input: '@domain.com',              expected: false, desc: 'missing local part' },
  { input: 'user@domain',              expected: false, desc: 'missing TLD' },
  { input: '',                         expected: false, desc: 'empty string' },
  { input: 'user @domain.com',         expected: false, desc: 'space in email' },
];

emailTestCases.forEach(({ input, expected, desc }) => {
  test(`isValidEmail("${input}") → ${desc}`, isValidEmail(input) === expected);
});

// ============================================================
// isValidURL() — HTTP/HTTPS URL validation
// ============================================================
console.log('\n--- isValidURL() ---');

const urlTestCases = [
  { input: 'https://example.com',         expected: true,  desc: 'https URL' },
  { input: 'http://example.com/path',     expected: true,  desc: 'http with path' },
  { input: 'https://sub.domain.com:8080', expected: true,  desc: 'with port' },
  { input: 'ftp://files.example.com',     expected: false, desc: 'ftp rejected' },
  { input: 'not-a-url',                   expected: false, desc: 'plain string' },
  { input: '',                            expected: false, desc: 'empty string' },
  { input: 'javascript:alert(1)',         expected: false, desc: 'javascript protocol rejected' },
];

urlTestCases.forEach(({ input, expected, desc }) => {
  test(`isValidURL("${input}") → ${desc}`, isValidURL(input) === expected);
});

// ============================================================
// isStrongPassword() — Password strength validation
// ============================================================
console.log('\n--- isStrongPassword() ---');

const passwordTestCases = [
  { input: 'Str0ng!Pass',   expected: true,  desc: 'meets all requirements' },
  { input: 'Ab1!abcd',      expected: true,  desc: 'exactly 8 chars strong' },
  { input: 'short1!',       expected: false, desc: 'too short (7 chars)' },
  { input: 'alllowercase1!',expected: false, desc: 'no uppercase' },
  { input: 'ALLUPPERCASE1!',expected: false, desc: 'no lowercase' },
  { input: 'NoDigits!!Aa',  expected: false, desc: 'no digit' },
  { input: 'NoSpecial1Aa',  expected: false, desc: 'no special character' },
  { input: '',              expected: false, desc: 'empty string' },
];

passwordTestCases.forEach(({ input, expected, desc }) => {
  test(`isStrongPassword("${input}") → ${desc}`, isStrongPassword(input) === expected);
});

// ============================================================
// isNonNegativeInt() — Non-negative integer validation
// ============================================================
console.log('\n--- isNonNegativeInt() ---');

const intTestCases = [
  { input: 0,     expected: true,  desc: 'zero is valid' },
  { input: 42,    expected: true,  desc: 'positive integer' },
  { input: -1,    expected: false, desc: 'negative integer rejected' },
  { input: 3.14,  expected: false, desc: 'float rejected' },
  { input: '5',   expected: false, desc: 'string rejected' },
  { input: null,  expected: false, desc: 'null rejected' },
  { input: NaN,   expected: false, desc: 'NaN rejected' },
];

intTestCases.forEach(({ input, expected, desc }) => {
  test(`isNonNegativeInt(${JSON.stringify(input)}) → ${desc}`, isNonNegativeInt(input) === expected);
});

console.log('\n✅ All validation-helpers tests completed.');
