#!/usr/bin/node
exports.esrever = function (list) {
  let lent = list.length - 1;
  let j = 0;
  while ((lent - j) > 0) {
    const aux = list[lent];
    list[lent] = list[j]
    list[j] = aux;
    j++;
    lent--;
  }
  return list;
};
