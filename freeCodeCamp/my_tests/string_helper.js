function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function truncate(str, n) {
  return str.length > n ? str.slice(0, n) + '...' : str;
}

function countWords(str) {
  return str.trim().split(/\s+/).length;
}

module.exports = { capitalize, truncate, countWords };