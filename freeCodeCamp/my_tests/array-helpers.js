function flattenArr(arr) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i])) {
      result = result.concat(flattenArr(arr[i]));
    } else {
      result.push(arr[i]);
    }
  }
  return result;
}

function removeDups(arr) {
  let seen = {};
  return arr.filter(x => seen[x] ? false : (seen[x] = true));
}

module.exports = { flattenArr, removeDups };