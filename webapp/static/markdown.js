(function () {
  "use strict";

  function escapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function inlineMarkdown(text) {
    return escapeHtml(text)
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  }

  function renderSafeMarkdown(markdown) {
    const lines = String(markdown || "").split("\n");
    const html = [];
    let inCode = false;
    let code = [];
    let listOpen = false;
    const closeList = () => {
      if (listOpen) {
        html.push("</ul>");
        listOpen = false;
      }
    };

    for (let index = 0; index < lines.length; index += 1) {
      const line = lines[index];
      if (line.startsWith("```")) {
        closeList();
        if (inCode) {
          html.push(`<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`);
          code = [];
        }
        inCode = !inCode;
        continue;
      }
      if (inCode) {
        code.push(line);
        continue;
      }
      if (line.startsWith("- ")) {
        if (!listOpen) {
          html.push("<ul>");
          listOpen = true;
        }
        html.push(`<li>${inlineMarkdown(line.slice(2))}</li>`);
        continue;
      }
      closeList();
      if (/^\|.*\|$/.test(line) && /^\|[\s:|-]+\|$/.test(lines[index + 1] || "")) {
        const headers = line.slice(1, -1).split("|");
        index += 1;
        const rows = [];
        while (/^\|.*\|$/.test(lines[index + 1] || "")) rows.push(lines[++index].slice(1, -1).split("|"));
        html.push(`<table><thead><tr>${headers.map((cell) => `<th>${inlineMarkdown(cell.trim())}</th>`).join("")}</tr></thead><tbody>${rows.map((row) => `<tr>${row.map((cell) => `<td>${inlineMarkdown(cell.trim())}</td>`).join("")}</tr>`).join("")}</tbody></table>`);
        continue;
      }
      const heading = line.match(/^(#{1,3})\s+(.+)$/);
      if (heading) {
        html.push(`<h${heading[1].length}>${inlineMarkdown(heading[2])}</h${heading[1].length}>`);
        continue;
      }
      if (line.startsWith("> ")) {
        html.push(`<blockquote>${inlineMarkdown(line.slice(2))}</blockquote>`);
        continue;
      }
      if (line.trim()) html.push(`<p>${inlineMarkdown(line)}</p>`);
    }
    closeList();
    if (inCode) html.push(`<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`);
    return html.join("");
  }

  window.TensorMarkdown = { renderSafeMarkdown };
})();
