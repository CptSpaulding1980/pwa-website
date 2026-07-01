const markdownIt = require("markdown-it");

module.exports = function(eleventyConfig) {
  // Passthrough copy
  eleventyConfig.addPassthroughCopy("src/img");
  eleventyConfig.addPassthroughCopy("src/styles");

  // Markdown
  let md = markdownIt({ html: true, breaks: true, linkify: true });
  eleventyConfig.setLibrary("md", md);

  // Collections
  eleventyConfig.addCollection("events", function(c) {
    return c.getFilteredByTag("events").sort((a, b) =>
      (b.data.date || "").localeCompare(a.data.date || ""));
  });
  eleventyConfig.addCollection("wrestlers", function(c) {
    return c.getFilteredByTag("wrestlers").sort((a, b) =>
      (a.data.title || "").localeCompare(b.data.title || ""));
  });
  eleventyConfig.addCollection("championships", function(c) {
    return c.getFilteredByTag("championships").sort((a, b) =>
      (a.data.title || "").localeCompare(b.data.title || ""));
  });

  // Filters
  eleventyConfig.addFilter("year", d => d ? d.split("-")[0] : "");
  eleventyConfig.addFilter("groupByYear", function(events) {
    const groups = {};
    for (const e of events) {
      const y = e.data.date ? e.data.date.split("-")[0] : "Unknown";
      if (!groups[y]) groups[y] = [];
      groups[y].push(e);
    }
    return groups;
  });
  eleventyConfig.addFilter("sortedYears", g =>
    Object.keys(g).sort((a, b) => b.localeCompare(a)));
  eleventyConfig.addFilter("groupByFirstLetter", function(wrestlers) {
    const groups = {};
    for (const w of wrestlers) {
      const letter = (w.data.title || "?")[0].toUpperCase();
      if (!groups[letter]) groups[letter] = [];
      groups[letter].push(w);
    }
    return groups;
  });
  eleventyConfig.addFilter("sort", (arr) => [...arr].sort());

  return {
    dir: { input: "src", output: "docs", data: "_data", includes: "_includes", layouts: "_includes/layouts" },
    pathPrefix: "/pwa-website/",
    templateFormats: ["njk", "md"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk",
  };
};
