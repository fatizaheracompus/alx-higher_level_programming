#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let neOccurrences = 0;
  for (let j = 0; j < list.length; j++) {
    if (searchElement === list[j]) {
      neOccurrences++;
    }
  }
  return neOccurrences;
};
