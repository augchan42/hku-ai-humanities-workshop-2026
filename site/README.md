# Workshop notebook — hosted source

A static, dependency-free website. Serve this directory or `dist/` with any static server. `data.js` and `assets/` contain the curated handout/photo material. The original source files and generator live in the parent workshop repository.

Generated with **GPT 6.1 Sol high**. The Sources & reading guide page contains the generation disclosure, linked from the footer on every page. The original workshop materials remain the work of their credited authors.

GitHub Pages deploys only `dist/` through the parent repository’s `.github/workflows/pages.yml`. All links work under a project subdirectory; no backend or API is required.

This hosted source intentionally excludes John Hawthorne’s private talk transcript, summary, and explanations. They appear only in the parent repository’s ignored local build.

Run `node --check app.js` to check JavaScript syntax. Open `index.html` directly or serve with `python3 -m http.server 8000`.
