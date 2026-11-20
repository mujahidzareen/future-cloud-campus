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

## November 2026 public-site improvements

The site has 74 routes, including tutor matching, family feedback and an interactive mini lesson. The booking form has three steps, combined notes filters use search + subject + stage + curriculum, and articles link to relevant guides. Decorative scenes pause off-screen. No new frontend package is required.

Build the public GitHub Pages output with:

```sh
FCC_INDEXABLE=1 FCC_ORIGIN=https://mujahidzareen.github.io/future-cloud-campus python -B build.py
```

Use `FCC_INDEXABLE=0` for private review builds. Public indexing excludes portals, booking, draft policies and tutor/review pages without approved content. CSS and JS URLs include a content hash to refresh changed assets.

### Live admissions connection

Edit `site_content.json`. The form remains explicitly in preview mode until `admissions.endpoint` is an HTTPS URL, a confirmed `email`, `provider_name`, HTTPS `provider_privacy_url` and `privacy_reviewed: true` are supplied. Approve and update the privacy page with the actual recipient, processing provider and retention/deletion arrangements before enabling live intake. The endpoint and email are public configuration, never place secrets in this file.

The receiving service must accept JSON POSTs and permit CORS from the final site origin. Validate and normalize all fields server-side, rate-limit requests, apply server-side spam protection, enforce consent, deduplicate by `requestId`, and notify the confirmed recipient. It must return a 2xx JSON response with `{"ok":true,"reference":"optional-reference"}` only after the request is durably accepted. An HTML response, an error status or a JSON response without `ok: true` is a failure. A received enquiry is not a confirmed booking. The browser retains fields after an error and offers copying; it never stores guardian details in browser storage. An unchanged retry reuses its request ID. Frontend validation and the honeypot do not replace backend spam protection.

GitHub Pages cannot itself send email or run this receiving service. No live endpoint or FCC admissions contact has been supplied, so live transmission is not enabled in this release.

### Approved people, feedback and prices

Populate `tutors` with objects containing `name`, `bio`, `qualification`, `subjects` (array), `curricula` (array), `photo` (local `/assets/...` path), optional local `video` MP4, `approved: true` and `photo_consent: true`. Unapproved entries and invalid photo paths remain unpublished. The renderer escapes text. Videos use `preload="none"` behind a disclosure control.

Populate `reviews` with `quote`, `display_name`, `context`, `approved: true` and `publication_consent: true`. Keep student identifiers out of public quotes. There are no invented testimonials, ratings or tutor biographies in this release. Empty states explain that introductions/feedback are coming soon.

For each plan, provide confirmed `duration_minutes` and `price` including currency. Confirm cancellation, rescheduling and missed-lesson terms before publishing them; the current comparison asks families to confirm these details in their quote. Four-week session counts are mathematical illustrations, not a billing commitment. The intended FCC-owned domain still requires provisioning; canonical URLs currently use the actual GitHub Pages URL.

### Social channels and Quran visibility

The Quran hero now sets its background and all foreground colours explicitly. This prevents shared light-page themes from combining with the previous white-on-dark text styles. Parent review sections appear on all five Quran programme pages and a direct Reviews link is in the main navigation.

The homepage and footer render six native SVG social icons. In `site_content.json`, set each `socials` entry's `url` to the official profile and `verified` to `true` after confirming ownership. Supported keys are `instagram`, `facebook`, `linkedin`, `youtube`, `tiktok` and `whatsapp`. The renderer accepts HTTPS links on the corresponding platform's domains only. Unconfigured entries are labelled Coming soon and are not clickable links; no account handles or WhatsApp numbers are guessed.

### Illustrative regional pricing and six-card review layout

`pricing_content.py` renders sample four-week plans of 4, 8 and 12 lessons. `site_content.json > sample_pricing` contains the independently illustrative GBP, USD, AED, SAR, QAR and OMR examples adapted from the user-supplied reference at https://protutorsonline.com/pricing/ and its `/app.js` on 20 November 2026. That reference explicitly labels its prices as samples, not live offers. FCC keeps the same distinction. These are not FX conversions or confirmed FCC fees. Canada and Other countries use a personal quote rather than invented example rates. Sample totals are lesson count multiplied by the displayed per-lesson sample; lesson duration and real terms still require confirmation.

The currency selector updates all three prices, totals and enquiry links. Plan, country and an illustrative-price note carry into the existing three-step booking preview. The custom-package link preserves the selected country. A compact GBP sample-pricing preview appears on the homepage.

The homepage and dedicated Reviews page now show six labelled placeholder cards while no approved testimonials exist. No names, quotations, star ratings or results were invented. Once genuine consented reviews are added to the existing `reviews` configuration, the real review renderer replaces the placeholders.
