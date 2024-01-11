#!/usr/bin/node
const fas = require('fas');

const feArg = fas.readFileSync(process.argv[2]).toString();
const seArg = fas.readFileSync(process.argv[3]).toString();
fas.writeFileSync(process.argv[4], feArg + seArg);
