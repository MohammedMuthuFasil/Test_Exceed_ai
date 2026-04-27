/**
 * @fileoverview Test suite for array-helpers.js utility functions.
 * Generated using GitHub Copilot AI — covers flattenArr and removeDups
 * with parameterized test cases and deep equality checks.
 */

const { flattenArr, removeDups } = require('./array-helpers');

/**
 * Deep equality comparison for arrays.
 * @param {Array} a - First array
 * @param {Array} b - Second array
 * @returns {boolean} Whether both arrays are deeply equal
 */
function deepEqual(a, b) {
  if (a.length !== b.length) return false;
  return a.every((val, i) => {
    if (Array.isArray(val) && Array.isArray(b[i])) return deepEqual(val, b[i]);
    return val === b[i];
  });
}

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
// flattenArr() — Recursively flattens nested arrays
// ============================================================
console.log('\n--- flattenArr() ---');

const flattenTestCases = [
  {
    input: [1, [2, 3], [4, [5, 6]]],
    expected: [1, 2, 3, 4, 5, 6],
    desc: 'multi-level nested arrays',
  },
  {
    input: [1, 2, 3],
    expected: [1, 2, 3],
    desc: 'already flat array unchanged',
  },
  {
    input: [],
    expected: [],
    desc: 'empty array returns empty',
  },
  {
    input: [[[[1]]]],
    expected: [1],
    desc: 'deeply nested single element',
  },
  {
    input: [1, [], 2, [], 3],
    expected: [1, 2, 3],
    desc: 'empty sub-arrays are removed',
  },
  {
    input: [['a', 'b'], ['c', ['d']]],
    expected: ['a', 'b', 'c', 'd'],
    desc: 'works with strings too',
  },
];

flattenTestCases.forEach(({ input, expected, desc }) => {
  const result = flattenArr(input);
  test(`flattenArr → ${desc}`, deepEqual(result, expected));
});

// ============================================================
// removeDups() — Removes duplicate values preserving first occurrence
// ============================================================
console.log('\n--- removeDups() ---');

const removeDupsTestCases = [
  {
    input: [1, 2, 2, 3, 3, 3],
    expected: [1, 2, 3],
    desc: 'removes numeric duplicates',
  },
  {
    input: ['a', 'b', 'a', 'c'],
    expected: ['a', 'b', 'c'],
    desc: 'removes string duplicates',
  },
  {
    input: [1, 2, 3],
    expected: [1, 2, 3],
    desc: 'no duplicates returns same',
  },
  {
    input: [],
    expected: [],
    desc: 'empty array returns empty',
  },
  {
    input: [5, 5, 5, 5],
    expected: [5],
    desc: 'all same element returns single',
  },
  {
    input: [1],
    expected: [1],
    desc: 'single element unchanged',
  },
];

removeDupsTestCases.forEach(({ input, expected, desc }) => {
  const result = removeDups(input);
  test(`removeDups → ${desc}`, deepEqual(result, expected));
});

console.log('\n✅ All array-helpers tests completed.');
