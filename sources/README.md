# Source register

Retrieved/processed: 8 November 2026 (Hong Kong / Shanghai time, UTC+08).

| Source | Role | Processing |
| --- | --- | --- |
| `notes/CCF11082026.pdf` | User-supplied 12-page scan of three printed handouts | Original bytes preserved; rendered at a maximum edge of 2,000 pixels; OCR retained separately; each page visually checked |
| `slides/manifest.json` | 222 records in the order exposed by the shared album | Public album metadata parsed from its embedded data; IDs, timestamps, image dimensions, and base image URLs retained |
| `slides/images/` | Local study copies of photos and video-preview frames | Requested at a maximum dimension of 2,000 pixels; not original camera files; video content was not downloaded |
| `slides/ocr/` | Initial OCR on album images | Unverified and often incomplete |
| `slides/ocr-sparse/` | Sparse OCR pass on album images | Unverified intermediate pass |
| `slides/ocr-enhanced/` | Local-contrast preprocessing and sparse OCR | Selected for search when available; unverified; may recognize background text |
| `workshop/overview.html` | Official event overview | Archived HTML from the supplied AI & Humanity Lab URL |
| `workshop/programme.jpg` | Official published rundown | Downloaded from the overview page; records the planned programme, not proof of actual talk content |

The source PDF divides as follows:

| PDF pages | Printed material | Programme context |
| --- | --- | --- |
| 1–2 | Paul Boghossian, *Comments on Shanahan* | Day-one manuscript symposium |
| 3–4 | Nate Sharadin, *Comments on Shanahan*, dated 5 November 2026 | Day-one manuscript symposium |
| 5–12 | Paul Boghossian, *Understanding in Large Language Models* | Day-two understanding/reasoning talk; handout and scheduled talk titles differ |

A separate private source is documented in `../private/hawthorne/` and excluded from Git and hosted output. The original recording, captions, and footage notes remain in `hongkongaipodcast-site`; this task does not alter that repository.
