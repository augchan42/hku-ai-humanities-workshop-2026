# Minds, Meaning & Machines — workshop notebook

A source-linked study edition of the HKU AI & Humanity workshop, 5–6 November 2026. The archive contains the 12-page scanned PDF, its three handouts transcribed by page and document, 66 plain-language explanations, a synthesis, a glossary, and an inventory of all 222 items retrieved from the shared photo album.

[Open the GitHub Pages notebook](https://augchan42.github.io/hku-ai-humanities-workshop-2026/). The repository’s GitHub Actions workflow builds and publishes the static hosted edition on every push to `main`. Hawthorne’s detailed material is available only in the local edition below.

The original [private Sites edition](https://hku-minds-meaning-machines-notebook.merry-lamb-8416.chatgpt.site) remains available as an earlier version.

## Generation disclosure

This notebook was generated with **GPT 6.1 Sol high**. The website, organization, summaries, plain-language explanations, and OCR-assisted transcription cleanup were AI-generated. The underlying handouts, slides, and talks are the work of their credited authors. The disclosure is also shown on the website’s **Sources & reading guide** page and linked from every page’s footer.

## GitHub Pages

The published site is fully static: HTML, CSS, JavaScript, images, PDF, and Markdown downloads. It uses no backend, database, API key, server-side rendering, or runtime build service. All asset links are relative, so it works under the GitHub Pages project path. The Python build script only prepares files before deployment; visitors need only a browser.

[The workflow](.github/workflows/pages.yml) runs the generator and content checks, uploads **only `site/dist/`**, and deploys it with GitHub Pages. It never uploads `private/` or `site/dist-local/`. The raw source archive and editable content are preserved in the repository; only the hosted edition is served as the website.

## Open the website

Run from this repository:

```sh
python3 scripts/build-notebook.py
python3 -m http.server 8000 --directory site/dist-local
```

Open **http://localhost:8000**. This local edition includes John Hawthorne’s final talk, organized from the existing edited video’s captions. It can also be opened directly at `site/dist-local/index.html` without a server: the data and assets are local and the site uses no external JavaScript or fonts.

`site/dist/` is a separate, hosted edition. It excludes Hawthorne’s transcript, detailed summary, and explanations. The source podcast repository records his request that the recording not be published online. Do not serve `dist-local` on a public network or upload it. Both outputs are generated and ignored by Git.

## Directory map

```text
sources/
  notes/CCF11082026.pdf      Original PDF, moved here without modifying its bytes
  notes/pages/              12 rendered page scans
  notes/ocr/                Uncorrected OCR retained for comparison
  slides/manifest.json      Album order, capture times, photo IDs, source image URLs
  slides/images/            222 reduced-resolution study images / video preview frames
  slides/ocr*/              Machine extraction passes; never treated as verified text
  workshop/                 Archived overview HTML and official programme image
  processing-report.json    Counts, PDF hash, and processing limits
transcripts/
  notes/page-01.md …         Scan-checked PDF transcriptions
  boghossian-on-shanahan.md  Complete first handout (PDF 1–2)
  sharadin-on-shanahan.md    Complete second handout (PDF 3–4)
  boghossian-understanding.md Complete third handout (PDF 5–12)
  slides/                   One machine-text record per album item
  slides-index.md           Combined searchable album inventory
content/
  notes.json                Editable page summaries, 66 explanations, examples, questions
  guide.json                Synthesis points, glossary, and source-linked session guides
  reading-guide.md          Generated complete explanations
  summary.md                Generated workshop synthesis
  glossary.md               Generated plain-language glossary
  sessions.md               Generated guide to both days
private/hawthorne/          Ignored local transcript, captions, and detailed reading guide
scripts/                    Reproducible extraction, generation, and validation helpers
site/
  index.html, app.js, styles.css   Website source
  data.js, assets/, downloads/     Generated hosted-safe content
  dist/                     Generated hosted edition (no private session material)
  dist-local/               Generated local edition (includes private session material)
```

## Reading order

1. Read [the synthesis](content/summary.md).
2. Compare Boghossian’s comments on pain with Sharadin’s comments on practical language: [PDF pages 1–2](transcripts/boghossian-on-shanahan.md) and [PDF pages 3–4](transcripts/sharadin-on-shanahan.md).
3. Read [Boghossian on understanding](transcripts/boghossian-understanding.md), using [the explanations](content/reading-guide.md) alongside it.
4. Explore [the photographed session guide](content/sessions.md) and [album inventory](transcripts/slides-index.md).
5. In the local edition, read Hawthorne’s timestamped guide and its connections to the handouts.

## Editorial conventions and limits

- **Transcription** preserves source wording, including reported incorrect answers and awkward wording. Obvious recognition errors were corrected against scans; typography, indentation, and emphasis were simplified. Use the original scan for precise quotation.
- **PDF pages 3–4 have clipped bottom text.** Missing text is marked instead of silently reconstructed. Page references inside Sharadin’s handout refer to Shanahan’s manuscript, not this PDF.
- **Summary / explanation / example / question** are editorial additions. A critic’s account of Shanahan is identified as a critic’s account. No workshop consensus is inferred.
- **Photo text is unverified OCR.** There are repeated slides, snapshots, handout photos, and still video previews; 222 is the number of album items, not unique slides. The actual audio/video in those album items has not been transcribed.
- **Session attribution** uses visible titles, footers, the official programme, and chronology. Goldstein’s topic label is editorial. Cappelen’s day-two photographs focus on understanding, while the scheduled title concerns consciousness; the guide records that discrepancy.
- **Hawthorne** used no slides. His captions come from the private edited video in `hongkongaipodcast-site`; they were not freshly checked against audio. Q&A speakers are not guessed. Timestamps are edit time (source-camera time minus 20 seconds). His material is local only.
- The multiplication in the handout was independently checked: **5,647 × 8,911 = 50,320,417**. Reported model identities, dialogue, and tool claims were not independently authenticated.

## Rebuild and verify

Requirements: Python 3, Pillow for photo preprocessing/contact sheets, Poppler (`pdfinfo`, `pdftoppm`), Tesseract with English, and Node only for JavaScript checks. Website generation itself uses Python’s standard library; serving the site has no dependency installation or build step.

```sh
python3 scripts/prepare-transcripts.py
# Optional: re-download photos or repeat enhanced OCR
python3 scripts/fetch-slides.py
OMP_THREAD_LIMIT=1 python3 scripts/ocr-slides.py
python3 scripts/build-notebook.py
python3 scripts/check-notebook.py
node --check site/app.js
```

Private material is optional: on another checkout, the builder still creates the handout/photo site when `private/hawthorne/` is absent. To include Hawthorne locally, restore the local-only captions, transcript, and `guide.json` from the original working copy; do not commit or upload them.

Sources: [shared album](https://photos.app.goo.gl/u8Toc2MdmTSncuYq6), [official workshop overview](https://ai-humanity.net/minds-meaning-and-machines-new-work-in-philosophy-of-ai/).
