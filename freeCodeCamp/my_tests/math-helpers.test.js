/**
 * @fileoverview Test suite for math-helpers.js utility functions.
 * Generated using GitHub Copilot AI — covers sum, average, factorial,
 * clamp, and isPrime with parameterized boundary testing.
 */

const { sum, average, factorial, clamp, isPrime } = require('./math-helpers');

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
// sum() — Adds all elements in an array
// ============================================================
console.log('\n--- sum() ---');

const sumTestCases = [
  { input: [1, 2, 3, 4, 5],   expected: 15,    desc: 'positive integers' },
  { input: [-1, -2, -3],      expected: -6,    desc: 'negative integers' },
  { input: [0, 0, 0],         expected: 0,     desc: 'all zeros' },
  { input: [],                expected: 0,     desc: 'empty array returns 0' },
  { input: [1.5, 2.5],        expected: 4.0,   desc: 'floating point numbers' },
  { input: [100],             expected: 100,   desc: 'single element' },
];

sumTestCases.forEach(({ input, expected, desc }) => {
  test(`sum([${input}]) → ${desc}`, sum(input) === expected);
});

// ============================================================
// average() — Arithmetic mean of array elements
// ============================================================
console.log('\n--- average() ---');

const averageTestCases = [
  { input: [2, 4, 6],     expected: 4,    desc: 'even distribution' },
  { input: [10],           expected: 10,   desc: 'single element' },
  { input: [1, 2, 3, 4],  expected: 2.5,  desc: 'fractional result' },
  { input: [-2, 2],       expected: 0,    desc: 'cancelling values' },
];

averageTestCases.forEach(({ input, expected, desc }) => {
  test(`average([${input}]) → ${desc}`, average(input) === expected);
});

// Test error case
let avgThrew = false;
try { average([]); } catch (e) { avgThrew = true; }
test('average([]) → throws on empty array', avgThrew);

// ============================================================
// factorial() — n! computation
// ============================================================
console.log('\n--- factorial() ---');

const factorialTestCases = [
  { input: 0,  expected: 1,       desc: '0! = 1' },
  { input: 1,  expected: 1,       desc: '1! = 1' },
  { input: 5,  expected: 120,     desc: '5! = 120' },
  { input: 10, expected: 3628800, desc: '10! = 3628800' },
];

factorialTestCases.forEach(({ input, expected, desc }) => {
  test(`factorial(${input}) → ${desc}`, factorial(input) === expected);
});

let facThrew = false;
try { factorial(-1); } catch (e) { facThrew = true; }
test('factorial(-1) → throws on negative', facThrew);

// ============================================================
// clamp() — Restricts value to [min, max] range
// ============================================================
console.log('\n--- clamp() ---');

const clampTestCases = [
  { val: 5,   min: 0,  max: 10, expected: 5,  desc: 'within range unchanged' },
  { val: -5,  min: 0,  max: 10, expected: 0,  desc: 'below min clamped up' },
  { val: 15,  min: 0,  max: 10, expected: 10, desc: 'above max clamped down' },
  { val: 0,   min: 0,  max: 10, expected: 0,  desc: 'at min boundary' },
  { val: 10,  min: 0,  max: 10, expected: 10, desc: 'at max boundary' },
];

clampTestCases.forEach(({ val, min, max, expected, desc }) => {
  test(`clamp(${val}, ${min}, ${max}) → ${desc}`, clamp(val, min, max) === expected);
});

// ============================================================
// isPrime() — Primality check
// ============================================================
console.log('\n--- isPrime() ---');

const primeTestCases = [
  { input: 2,   expected: true,  desc: 'smallest prime' },
  { input: 3,   expected: true,  desc: 'prime' },
  { input: 4,   expected: false, desc: 'composite (2x2)' },
  { input: 17,  expected: true,  desc: 'larger prime' },
  { input: 1,   expected: false, desc: '1 is not prime' },
  { input: 0,   expected: false, desc: '0 is not prime' },
  { input: -7,  expected: false, desc: 'negative not prime' },
  { input: 97,  expected: true,  desc: 'two-digit prime' },
];

primeTestCases.forEach(({ input, expected, desc }) => {
  test(`isPrime(${input}) → ${desc}`, isPrime(input) === expected);
});

console.log('\n✅ All math-helpers tests completed.');
