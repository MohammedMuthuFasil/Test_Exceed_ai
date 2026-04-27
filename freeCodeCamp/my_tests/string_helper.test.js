/**
 * @fileoverview Test suite for string_helper.js utility functions.
 * Generated using GitHub Copilot AI — covers capitalize, truncate, and countWords
 * with systematic edge case coverage and descriptive assertions.
 */

const { capitalize, truncate, countWords } = require('./string_helper');

/**
 * Test runner utility — logs pass/fail with descriptive labels.
 * @param {string} label - Test description
 * @param {boolean} condition - Assertion to evaluate
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
// capitalize() — Should uppercase only the first character
// ============================================================
console.log('\n--- capitalize() ---');

const capitalizeTestCases = [
  { input: 'hello',       expected: 'Hello',       desc: 'lowercases first char to upper' },
  { input: 'a',           expected: 'A',           desc: 'single character' },
  { input: 'HELLO',       expected: 'HELLO',       desc: 'already uppercase stays same' },
  { input: 'hello world', expected: 'Hello world', desc: 'only first char affected' },
  { input: '',            expected: '',            desc: 'empty string returns empty' },
  { input: '123abc',      expected: '123abc',      desc: 'non-alpha first char unchanged' },
];

capitalizeTestCases.forEach(({ input, expected, desc }) => {
  test(`capitalize("${input}") → ${desc}`, capitalize(input) === expected);
});

// ============================================================
// truncate() — Should shorten string and add ellipsis if needed
// ============================================================
console.log('\n--- truncate() ---');

const truncateTestCases = [
  { input: 'hello world', n: 5,  expected: 'hello...',     desc: 'truncates and adds ellipsis' },
  { input: 'hi',          n: 10, expected: 'hi',           desc: 'shorter than limit unchanged' },
  { input: 'abcdef',      n: 3,  expected: 'abc...',       desc: 'truncates at exact n' },
  { input: '',            n: 5,  expected: '',             desc: 'empty string stays empty' },
  { input: 'exact',       n: 5,  expected: 'exact',        desc: 'equal to limit unchanged' },
  { input: 'abcdef',      n: 0,  expected: '...',          desc: 'zero limit returns only ellipsis' },
];

truncateTestCases.forEach(({ input, n, expected, desc }) => {
  test(`truncate("${input}", ${n}) → ${desc}`, truncate(input, n) === expected);
});

// ============================================================
// countWords() — Should count whitespace-separated words
// ============================================================
console.log('\n--- countWords() ---');

const countWordsTestCases = [
  { input: 'hello world',         expected: 2, desc: 'two words' },
  { input: 'one',                 expected: 1, desc: 'single word' },
  { input: '  spaced   out  ',    expected: 2, desc: 'extra whitespace ignored' },
  { input: 'a b c d e',           expected: 5, desc: 'five single-char words' },
  { input: 'the quick brown fox', expected: 4, desc: 'normal sentence' },
];

countWordsTestCases.forEach(({ input, expected, desc }) => {
  test(`countWords("${input}") → ${desc}`, countWords(input) === expected);
});

console.log('\n✅ All string_helper tests completed.');

