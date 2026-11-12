# Future Cloud Campus

Review version of the Future Cloud Campus website. The Parent and Teacher Portals have Coming Soon pages. It contains no live student records and does not transmit demo form entries.

## Source and build

- `content.py` holds the original programme, country and FAQ copy.
- `additions.py` holds new subjects, curricula, plans, articles and the original study-guide text.
- `notes_pdf.py` builds the 12 downloadable topic PDFs using ReportLab and DejaVu Sans fonts. After editing a guide, run `python -B notes_pdf.py docs` in the GitHub repository, then run the normal HTML build.
- `artwork.py` creates a distinct vector illustration for each of the 70 inner pages.
- `build.py` renders 71 HTML pages, metadata, the preview robots policy and sitemap.
- `dist/assets/` contains original logo files, SVG illustrations, CSS and JavaScript.
- Run `python -B build.py` from the root to regenerate pages. Set `FCC_ORIGIN` to override the canonical origin. Serve `dist/` over HTTP for local testing.
- The stylesheet implements the rotating header logo, lesson illustration, clay surfaces, scroll reveals and reduced-motion fallback. The Inter font and its license are stored in assets/fonts. No third-party frontend packages are required.

## GitHub Pages

The GitHub repository publishes the generated site from the `main` branch and the `/docs` folder. To refresh the pages in that repository, run:

```sh
FCC_ORIGIN=https://mujahidzareen.github.io/future-cloud-campus python -B build.py
```

Then commit the regenerated `docs/` files. The pages use relative internal links so that assets, navigation and nested portal routes resolve under the repository URL.

## Review and production gates

1. Approve the review site visually and confirm course, market, safeguarding and recruitment copy. Publish testimonials only when provided and approved.
2. Confirm the existing ERP, staging access and API contracts. Connect guardian demo requests through a server-side, validated, rate-limited intake with idempotency, CRM lead creation, attribution and operator confirmation. Add only verified admissions and WhatsApp contacts.
3. Implement identity and role enforcement for parents, teachers and staff. Confirm class schedules, time zones, assigned learners, attendance, activities, evaluation approval, access logs and retention against the ERP. The portal routes announce planned features.
4. Confirm policies, consent and analytics ownership and configure approved analytics, conversion events, CMS and operational monitoring. Run performance, accessibility, security and cross-device launch checks with the production integrations present.
5. Provision the FCC-controlled production domain and service accounts. Change canonical/social metadata, indexation and robots rules only for the approved public release. Keep sensitive portal routes unindexed.
