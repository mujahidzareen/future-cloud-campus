# Future Cloud Campus

Review version of the Future Cloud Campus website. The Parent and Teacher Portals have Coming Soon pages. It contains no live student records and does not transmit demo form entries.

## Source and build

- `content.py` holds the original programme, country and FAQ copy.
- `additions.py` holds new subjects, curricula, plans, articles and the original study-guide text.
- `notes_pdf.py` builds the 12 downloadable topic PDFs using ReportLab and DejaVu Sans fonts. After editing a guide, run `python -B notes_pdf.py docs` in the GitHub repository, then run the normal HTML build.
- `artwork.py` creates a distinct vector illustration for each of the 70 inner pages.
- `build.py` renders 74 HTML pages, metadata, the preview robots policy and sitemap.
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

Populate `reviews` with `quote`, `display_name`, `context`, `approved: true` and `publication_consent: true`. Keep student identifiers out of public quotes. Sample review-style copy is explicitly labelled as illustrative and is never presented as genuine customer feedback. No fabricated identities, ratings or results are used. Tutor introductions remain pending.

For each plan, provide confirmed `duration_minutes` and `price` including currency. Confirm cancellation, rescheduling and missed-lesson terms before publishing them; the current comparison asks families to confirm these details in their quote. Four-week session counts are mathematical illustrations, not a billing commitment. The intended FCC-owned domain still requires provisioning; canonical URLs currently use the actual GitHub Pages URL.

### Social channels and Quran visibility

The Quran hero now sets its background and all foreground colours explicitly. This prevents shared light-page themes from combining with the previous white-on-dark text styles. Parent review sections appear on all five Quran programme pages and a direct Reviews link is in the main navigation.

The homepage and footer render native SVG icons for configured official social channels. In `site_content.json`, set each `socials` entry's `url` to the official profile and `verified` to `true` after confirming ownership. Supported keys are `instagram`, `facebook`, `linkedin`, `youtube`, `tiktok` and `whatsapp`. The renderer accepts HTTPS links on the corresponding platform's domains only. Unconfigured channels are omitted; no account handles or WhatsApp numbers are guessed.

### Illustrative regional pricing and six-card review layout

`pricing_content.py` renders sample four-week plans of 4, 8 and 12 lessons. `site_content.json > sample_pricing` contains the independently illustrative GBP, USD, AED, SAR, QAR and OMR examples adapted from the user-supplied reference at https://protutorsonline.com/pricing/ and its `/app.js` on 20 November 2026. That reference explicitly labels its prices as samples, not live offers. FCC keeps the same distinction. These are not FX conversions or confirmed FCC fees. Canada and Other countries use a personal quote rather than invented example rates. Sample totals are lesson count multiplied by the displayed per-lesson sample; lesson duration and real terms still require confirmation.

The currency selector updates all three prices, totals and enquiry links. Plan, country and an illustrative-price note carry into the existing three-step booking preview. The custom-package link preserves the selected country. A compact GBP sample-pricing preview appears on the homepage.

The homepage and dedicated Reviews page show six clearly labelled hypothetical parent perspectives. Each has a topic, short heading, paragraph and generic avatar, with a prominent sample-copy notice. A native horizontal carousel provides previous/next buttons, swipe/scroll, keyboard Left/Right/Home/End, position announcements and disabled end controls. It never auto-advances. Reduced-motion and paused-motion settings disable smooth scrolling. Approved consented entries in `reviews` replace sample copy automatically.

### Quran learning library
All four course cards now open usable study spaces. Quran Reading includes all 114 surahs and 6,236 ayahs, with unmodified Arabic, Urdu translation and complete footnotes from QuranEnc.com. Urdu edition: Muhammad Ibrahim Junagarhi / Rowwad Translation Center, version 1.1.3. The local Hafs v20 font is paired with the publisher-provided Quran_text.csv. Attribution, source links and edition information appear beside the reader and in assets/quran/SOURCES.txt.

Run `python -B scripts/import_quran.py` before a content release to refresh from the publisher’s current edition; preserve all text, footnotes, metadata and attribution. Run `python -B scripts/verify_quran.py` for data integrity. The importer uses official QuranEnc endpoints and its published redistribution terms at https://quranenc.com/en/home/api/. Do not edit imported Quran/translation strings. Report observations through the publisher’s source page.

The reader loads local compressed reading files on demand, with a separate small opening-surah file, 20-ayah pagination, surah/ayah deep links, Urdu visibility, Arabic size controls and a browser-local saved position. It requires a current browser with DecompressionStream support; an explicit error/retry/source-reader link handles unsupported browsers or missing files. No remote API call is needed while reading. Only Quran pages load the new scripts/style/font.

Noorani Qaida provides nine original foundation lessons; Tajweed has eight guided-practice lessons; Islamic Studies has six introductory lessons with links to relevant Quran ayahs. These are original exercises, not a copied Qaida textbook or a substitute for teacher pronunciation feedback. Workbook content remains readable without JavaScript; JavaScript adds single-lesson selection and previous/next controls.

### Editorial design and motion refresh
The homepage now uses the original `studio_design.py` composition: a cobalt hero, oversized Space Grotesk type, floating classroom artwork, a kinetic learning ribbon, subject galleries, layered learning chapters, a dedicated Quran feature, resource cards, pricing, parent perspectives, regional guidance and a large closing invitation. Inner-page headers, typography, cards, buttons and the footer share the same design system. The supplied logo and distinct page illustrations are preserved.

`assets/studio.css` and `assets/studio.js` add native CSS 3D depth, pointer-responsive cards, subtle magnetic buttons, colour washes, scroll reveals, a reading-progress line and supported browser page transitions. Normal page links and document scrolling remain native. The existing pause control persists its choice in session storage; reduced-motion settings suppress decorative motion. Off-screen and inactive-tab animation is paused. No animation library, remote font dependency or loading interstitial was introduced. Space Grotesk is locally hosted with its OFL license.

The La boite à slides / Awwwards reference informed the broad visual ambition; the implementation, educational copy and composition are original to FCC. The reference's visual browser preview remained on its loader, so no claim is made to have reproduced its exact live animation sequences. Existing sample-pricing and illustrative-review labels, pending contact/social states, Quran content, booking-preview behavior and portal statuses are unchanged.

### Tutor directory and About FCC
Added 12 clearly labelled illustrative tutor profiles with original generated clay portraits, fictional first names, subject focus, learning-stage examples, individual profile pop-ups with lesson approaches, a matching checklist and subject-specific enquiry links. Search and stage filters combine, with count/empty/reset states. The fictional entries are separate from the existing approved `tutors` configuration; they carry no invented degrees, experience claims, ratings or availability. The Tutors page remains noindex until actual approved staff content is provided.

`campus_people.py` owns the directory and expanded About content. About FCC now covers purpose, mission, vision, learning values, three campus pathways, the learning process, family/course fit and planned portals. Statements describe the campus approach and actual website resources; no founding history, awards, accreditations, offices or business performance numbers were invented. Homepage and About teasers link to the directory.

Portrait assets and prompt documentation are in `docs/assets/people/` for GitHub Pages (`dist/assets/people/` in the private build). The two optimized WebP sheets serve all 12 distinct portraits. Original artwork was generated with the built-in image-generation tool. See `assets/people/README.txt` for the prompt set and disclosure requirements.

### Tutor profile pop-ups and CEO message
“View profile details” opens the selected example in one shared native dialog without expanding the card. It includes the corresponding portrait, subject, lesson content and enquiry link, a persistent close button, Escape and backdrop dismissal, keyboard focus wrapping, focus return, background scroll locking and internal scrolling on small screens. Profile search includes the content moved into inert templates. Without JavaScript the subject enquiry links remain available.

About FCC includes a CEO section naming Khawaja Tahir Shafique (provided by the site owner), with a decorative KTS monogram. The original welcome copy is visibly labelled “Draft message · prepared for approval”; replace it with approved wording in `campus_people.py` when available. No CEO photograph, personal history or signature was invented.

### Compact campus refresh
Cards now use a denser responsive scale: four tutor columns on wide screens, three/two at intermediate widths, one on phones. Tutor descriptions stay in the existing accessible profile pop-up; each card keeps a concise subject/stage summary. Home subject/resource cards, general card padding and the mobile enquiry bar are smaller.

`campus_refresh.py` and `assets/campus-refresh.css` own the learning roadmap, photo-source helper and photographic feedback panel. The Learning Levels roadmap has four connected stages, jump links and stage-specific enquiry preselection. About FCC keeps the CEO identity below an editorial learning image on the left and a shorter draft message on the right; this is not a CEO portrait.

The six invented review-style examples have been removed everywhere. Real approved reviews in `site_content.json` render through the existing carousel. Until those are supplied, the new photo-led panel states that approved family stories are pending; no customer quotation, rating or identity is invented. A review photograph is rendered only for a local `photo` asset plus `photo_consent: true`, in addition to the existing approval and publication consent requirements.

Stock tutor photographs are visibly labelled as examples, not FCC staff. Their source list is `assets/people/STOCK-PHOTOS.md`; the Pexels CDN serves the images and requires network availability. Real staff biographies, staff portraits, genuine family reviews and the CEO's own approved portrait still require owner-provided content.

### About illustration, representative portrait and six review examples
Added a custom transparent clay learning illustration to the left column of the About campus story. Its float, rotation, orbit and pointer depth use the existing motion controls. The generated asset and prompt/source documentation are in `assets/people/STORY-ART.md`.

The CEO panel now uses a male stock portrait with a visible “Stock portrait · CEO photograph pending” caption and explicit alternative text. It is not identified as a photograph of Khawaja Tahir Shafique; his own approved portrait remains necessary.

Per the follow-up request, Home and Reviews again show six compact, hypothetical parent-perspective cards, with family stock-photo thumbnails, horizontal arrow controls, swipe/scroll and keyboard navigation. Quran sections show three cards. A section disclosure, each card’s example badge and its attribution state that these are illustrative design copy, not FCC customer testimonials. No invented person, rating or learner result is attributed to FCC. Approved real reviews still use the separate configured renderer and consent requirements.

### Focused homepage and interactive pathways — 26 November 2026

The homepage now follows subjects → three lesson steps → tutors → Quran learning → family perspectives → illustrative pricing → FAQ and demo invitation. The clearer hero uses “Personal online tutoring. A clearer path forward.” with Book a Free Demo as the primary action. The rotating header logo, floating classroom and About illustration remain; secondary spinning decorations, the marquee and cursor halo have been removed from this journey. Hover depth and colour changes remain, with pause and reduced-motion support.

Learning Levels includes native stage/curriculum selectors, context-specific resource links, curriculum guides and an enquiry link that carries both choices into the existing form. All roadmap stages remain visible, and the chosen stage is highlighted. Without JavaScript, the stage navigation and default enquiry remain usable. Route generation preserves GitHub Pages subdirectory links.

Pricing now includes a comparison table for example frequency/count, focus, confirmed session length/fees when supplied, one-to-one format, and cancellation terms. Unconfirmed details request a personal quote. Official social links render only after configuration/verification. The booking form remains an explicit preview until the existing admissions activation requirements are satisfied. Real portraits and reviews still require approved source material.

Space Grotesk uses a local WOFF file (63,324 bytes versus the original 136,676-byte TTF), with its existing OFL license. No measured page-speed or Core Web Vitals score is claimed.
