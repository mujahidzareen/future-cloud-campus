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

## Horizontal review carousel update
- Replaced six skeleton cards with clearly labelled hypothetical parent-perspective paragraphs; no fabricated customers, ratings or results.
- Browser verified desktop next-arrow stepping, initial/last disabled controls, position announcements and keyboard Home. Mobile next, End and ArrowLeft were exercised.
- Checked both home and Reviews in 320, 375, 768, 1024 and 1440 pixel iframe widths: six cards present, responsive one/two/three-card views, no horizontal page overflow.
- Native overflow supports touch/swipe. There is no autoplay; smooth scrolling respects reduced-motion and the site motion-pause control.

## Quran learning library update
- Verified the imported dataset: 114 surahs and 6,236 unique sequential ayahs, complete translation/footnote fields and matching Hafs v20 WOFF2 font.
- Browser-tested the Quran Education link into the reader, all 114 selector options, Al-Fatihah, Al-Baqarah 2:255 and 2:282, Ta-Ha 20:114, An-Nas and final-surah controls.
- Tested previous-ayah pagination, Urdu visibility, Arabic text size, saving/resuming a reading position across reload/navigation and opening source footnotes.
- Tested course-card navigation into Noorani Qaida, lesson selection/next, Tajweed Iqlab selection and the Islamic Studies dua link into the correct Quran ayah.
- Checked 20 responsive layouts across all five Quran pages at 320, 375, 768 and 1440 widths with no horizontal page overflow. Checked a long ayah at the smallest reader width.
- Reader Arabic/translation use textContent and translate=no. Source credits, translation edition and footnotes stay visible and unmodified. Data loads on demand from the same site.

## Editorial design and motion refresh
- Checked 35 responsive layouts across home, subjects, pricing, Quran reader, demo booking, Free Notes and parent portal at 320, 375, 768, 1024 and 1440 iframe widths. Fixed a resource-title minimum-width overflow on the smallest homepage view; all tested widths have no horizontal page overflow after the fix.
- Visually reviewed desktop/mobile hero compositions, inner-page contrast, Quran reader controls and family-review card spacing.
- Tested mobile menu opening and Escape dismissal; course navigation; pausing classroom motion with the headline remaining visible; persistence of the pause setting when opening another page; resuming motion across navigation.
- Tested AED sample pricing (80 / 72 / 64), Free Notes search (fractions: 1 of 12 available), homepage review next control (examples 2–4 of 6), and the Quran reader loading Al-Ikhlas with its four ayahs.
- Reduced-motion rules are present for all new motion and page transitions. New pointer/scroll code uses event-triggered animation frames, native links and normal document scrolling; decorative motion pauses off-screen.
