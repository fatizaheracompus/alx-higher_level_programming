#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const i in valsUniq) {
  const list = [];
  for (const f in totalist) {
    if (totalist[f][1] === valsUniq[i]) {
      list.unshift(totalist[f][0]);
    }
  }
  newDict[valsUniq[i]] = list;
}
console.log(newDict);
