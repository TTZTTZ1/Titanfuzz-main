const assert = require("assert");

global.window = {};
require("../webapp/static/markdown.js");

const html = global.window.TensorMarkdown.renderSafeMarkdown("# Report\n\n- one\n\n## Next\n<script>alert(1)</script>");
assert(html.includes("</ul><h2>Next</h2>"));
assert(!html.includes("<script>"));
assert(html.includes("&lt;script&gt;"));
console.log("ok");
