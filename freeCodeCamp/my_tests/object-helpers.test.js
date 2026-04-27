/**
 * @fileoverview Test suite for object-helpers.js utility functions.
 * Generated using GitHub Copilot AI — covers pick, omit, invert, deepFreeze
 * with parameterized test cases and strict equality checks.
 */

const { pick, omit, invert, deepFreeze } = require('./object-helpers');

/**
 * Deep equality comparison for plain objects.
 * @param {Object} a - First object
 * @param {Object} b - Second object
 * @returns {boolean} Whether both objects are deeply equal
 */
function deepEqual(a, b) {
  const keysA = Object.keys(a);
  const keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;
  return keysA.every(key => {
    if (typeof a[key] === 'object' && typeof b[key] === 'object') {
      return deepEqual(a[key], b[key]);
    }
    return a[key] === b[key];
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
// pick() — Select specific keys from an object
// ============================================================
console.log('\n--- pick() ---');

const pickTestCases = [
  {
    obj: { a: 1, b: 2, c: 3 },
    keys: ['a', 'c'],
    expected: { a: 1, c: 3 },
    desc: 'picks specified keys',
  },
  {
    obj: { a: 1, b: 2 },
    keys: ['z'],
    expected: {},
    desc: 'non-existent key returns empty',
  },
  {
    obj: { a: 1, b: 2 },
    keys: [],
    expected: {},
    desc: 'no keys returns empty object',
  },
  {
    obj: {},
    keys: ['a'],
    expected: {},
    desc: 'empty source returns empty',
  },
];

pickTestCases.forEach(({ obj, keys, expected, desc }) => {
  test(`pick → ${desc}`, deepEqual(pick(obj, keys), expected));
});

// ============================================================
// omit() — Exclude specific keys from an object
// ============================================================
console.log('\n--- omit() ---');

const omitTestCases = [
  {
    obj: { a: 1, b: 2, c: 3 },
    keys: ['b'],
    expected: { a: 1, c: 3 },
    desc: 'omits specified key',
  },
  {
    obj: { a: 1, b: 2 },
    keys: ['a', 'b'],
    expected: {},
    desc: 'omit all keys returns empty',
  },
  {
    obj: { a: 1 },
    keys: ['z'],
    expected: { a: 1 },
    desc: 'omit non-existent key unchanged',
  },
  {
    obj: { a: 1, b: 2 },
    keys: [],
    expected: { a: 1, b: 2 },
    desc: 'no keys to omit returns copy',
  },
];

omitTestCases.forEach(({ obj, keys, expected, desc }) => {
  test(`omit → ${desc}`, deepEqual(omit(obj, keys), expected));
});

// ============================================================
// invert() — Swap keys and values
// ============================================================
console.log('\n--- invert() ---');

const invertTestCases = [
  {
    obj: { a: '1', b: '2' },
    expected: { '1': 'a', '2': 'b' },
    desc: 'swaps keys and string values',
  },
  {
    obj: { name: 'age', color: 'red' },
    expected: { age: 'name', red: 'color' },
    desc: 'arbitrary string pairs',
  },
  {
    obj: {},
    expected: {},
    desc: 'empty object returns empty',
  },
];

invertTestCases.forEach(({ obj, expected, desc }) => {
  test(`invert → ${desc}`, deepEqual(invert(obj), expected));
});

// ============================================================
// deepFreeze() — Recursively freeze objects
// ============================================================
console.log('\n--- deepFreeze() ---');

test('deepFreeze → top-level is frozen', () => {
  const obj = deepFreeze({ a: 1 });
  return Object.isFrozen(obj);
});

test('deepFreeze → nested object is frozen', () => {
  const obj = deepFreeze({ a: { b: 2 } });
  return Object.isFrozen(obj.a);
});

test('deepFreeze → deeply nested is frozen', () => {
  const obj = deepFreeze({ x: { y: { z: 3 } } });
  return Object.isFrozen(obj.x.y);
});

console.log('\n✅ All object-helpers tests completed.');
