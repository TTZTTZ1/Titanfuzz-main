const assert = require("assert");

global.window = {};
require("../webapp/static/charts.js");

const { buildPath } = global.window.TensorCharts;
const path = buildPath(
  [{ x: 0, y: 1 }, { x: 1, y: null }, { x: 2, y: 3 }],
  (value) => value,
  (value) => value,
);

assert.strictEqual(path, "M0,1 M2,3");
console.log("ok");
