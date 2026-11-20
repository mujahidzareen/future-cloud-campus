# Release verification — 20 November 2026

- Generated and checked 74 HTML routes and their relative asset/link targets. No broken local target was found.
- Checked JavaScript syntax and Git whitespace errors.
- Validated public robots/sitemap and indexation exclusions. The private host remains unindexed.
- Browser tested required-field validation, course/plan preselection, country/timezone selection, editable preview summary and preservation of entered data.
- Browser tested search plus curriculum/subject filters, no-results feedback and clearing filters.
- Browser tested correct and incorrect lesson feedback, progression, completion and switching between maths/science topics.
- Browser tested intake against local, deterministic success, HTTP 503 and unexpected HTML-response fixtures. Confirmed receipt appears only for a 2xx JSON response containing `ok: true`; failures preserve entered details and allow retry. No real messages were sent.
- Checked 28 layouts across home, booking, notes, pricing, mini lesson, tutor matching and family feedback at 320, 375, 768 and 1440 pixel frame widths. No horizontal page overflow was found. The plan comparison has its own horizontal scroller on small screens.
- Tutor biographies/photos/videos, parent testimonials, live admissions and fixed prices remain pending confirmed business content. Their rendering and activation paths are implemented without fabricated public records.

## Quran, reviews and social update

- Confirmed and fixed the pale-background/white-text conflict on Quran Education. The hero now uses dark forest text, readable breadcrumbs/body copy and a strong green CTA.
- Checked 20 layouts across Quran Education, Quran Reading, Reviews and Home at 320, 375, 768, 1024 and 1440 pixel frame widths. No horizontal overflow or header item overlap was found.
- Verified that the Reviews navigation and Quran review sections are present, and six labelled social icons render in the homepage section and global footer.
- Empty review/social states remain explicit. Confirmed social URLs are still required to activate links; approved testimonials are still required to display reviews.

## Regional pricing and six-card review update

- Compared all six sample rate tables against the user-supplied ProTutors pricing page and JavaScript, including its illustrative-pricing notice.
- Browser checked all 18 per-lesson prices and all 18 four-week totals across GBP, USD, AED, SAR, QAR and OMR. Checked Canada personal-quote fallback.
- Verified Oman/Exam focus enquiry preselection and the sample-price note, plus Canada country preservation through the custom-package planner.
- Confirmed six explicitly labelled review placeholders on both the homepage and Reviews page.
- Checked 15 layouts across pricing, reviews and home at 320, 375, 768, 1024 and 1440 pixel widths with no horizontal page overflow.
