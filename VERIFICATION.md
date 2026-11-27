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

## Twelve illustrative tutors and About FCC
- Browser verified 12 distinct example profile cards, profile expansion, combined search/stage filtering, reset and subject-specific enquiry preselection (Chemistry).
- Search for chemistry returns two profiles; combining Primary reduces this to the general-science example; clearing filters restores all 12.
- Checked 15 responsive layouts across Tutors, About and Home at 320, 375, 768, 1024 and 1440 iframe widths; no horizontal page overflow. Expanded a profile at the narrowest width without overflow.
- Visually checked the tutor hero, portrait sheets, profile disclosure and expanded About page; confirmed homepage/About each include one tutor teaser.
- Profiles explicitly identify fictional names/illustrations and require real credentials/availability to be confirmed. The approved real-tutor configuration and noindex policy remain separate.

## Profile pop-ups and CEO section
- Replaced the card disclosure with one native dialog and twelve inert profile templates; card heights stayed identical when a profile opened.
- Browser verified Ayaan, Omar and Hamza show their corresponding subject, portrait and lesson details. Opening a second profile replaces the first. Clicking inside the dialog leaves it open.
- Checked close button, Escape and backdrop dismissal, restored opener focus and unlocked page scrolling. Verified forward and reverse keyboard focus wrap at 320 pixels and the enquiry link scrolls into view.
- Combined chemistry search returns two profiles; Primary reduces this to one and reset restores all twelve.
- Checked ten Tutors/About layouts at 320, 375, 768, 1024 and 1440 iframe widths: no horizontal page overflow. The 320px profile fits its viewport and scrolls internally without horizontal overflow.
- Visually reviewed desktop profile and CEO layouts and 320px mobile layouts. CEO name, role, draft label and text remain readable. CEO identity uses the owner-supplied name and a monogram.
- Rebuilt 74 pages; JavaScript syntax and local page/asset targets checked. The dialog entry animation and monogram respect reduced-motion and pause settings.

## Compact cards, photographs and learning roadmap
- Tutor cards measured 499px high in a four-column desktop grid (previously about 879px); all twelve cards align. Pop-up details remain separate from card size.
- All twelve 900px tutor stock photographs loaded in the browser; the family-learning photo and CEO-section study photo loaded at 1000px. Stock-photo disclaimers remain visible; no stock person is presented as FCC staff, a customer or the CEO.
- Removed all six sample review-style quotations and “Sample copy” badges. Home, Reviews and Quran pages share a professional photo-led feedback panel while genuine approved reviews remain pending. Existing real-review carousel rendering is preserved.
- Checked 25 Home/Tutors/Reviews/About/Learning Levels layouts at 320, 375, 768, 1024 and 1440 iframe widths without horizontal page overflow. Rechecked mobile About after scrolling and fixed the older course-card minimum-width overflow.
- Browser verified stock-portrait profile opening and Escape dismissal, roadmap jump navigation and Secondary preselection in the enquiry form. No enquiries were submitted.
- Visually reviewed desktop tutor, CEO, feedback and roadmap layouts; mobile roadmap, feedback and CEO text remained readable. The mobile enquiry bar is shorter.
- Rebuilt 74 pages; checked local targets, generated structure, Python compilation, JavaScript syntax and whitespace. Third-party image CDN availability remains an external dependency.

## About illustration and six restored illustrative review cards
- Checked the custom transparent 3D artwork loading beside the campus story; its CSS animation runs and the global pause control pauses it. Resume restores motion; reduced-motion, off-screen and inactive-tab rules are present.
- Browser verified the male stock portrait loads and the visible caption says the CEO photograph is pending.
- Home and Reviews each render six illustrative cards; the desktop Next arrow moves from examples 1–3 to 2–4, and keyboard End reaches 4–6 with Next disabled. At 320px, Next moves to example 2 without horizontal page overflow.
- Checked 15 Home/About/Reviews layouts at 320, 375, 768, 1024 and 1440 iframe widths without horizontal page overflow. Visually checked desktop and mobile artwork, portrait and review presentation.
- Preserved the existing approved-review configuration branch, tutor pop-ups, roadmap, resource and Quran content. No real enquiries were submitted.

## Focused homepage and interactive learning pathways — 26 November 2026
- Browser verified the clearer hero, primary demo CTA and eight-section homepage journey; four compact subject cards retain real course links.
- Tested all four learning-stage choices and all four curriculum choices in the pathway picker, curriculum guide destinations, foundation/secondary resource switching, roadmap highlighting and the Higher secondary / Matric & Intermediate enquiry preselection.
- Confirmed the chosen stage, curriculum and goal appear in the booking fields; progressed through Learning, Availability and Contact. Live intake remains disabled and visibly labelled as a preview.
- Measured 20 iframe layouts across Home, Learning Levels, Pricing and About at 320, 375, 768, 1024 and 1440 CSS-pixel frame widths: no horizontal page overflow. The comparison table retains its own small-screen scroller.
- Tested mobile menu open/Escape, global animation pause/resume, continued header-logo rotation and review next-arrow movement to examples 2–4 of 6.
- Verified the local compressed heading font loads; size reduced from 136,676 to 63,324 bytes. No field performance score was measured.
- Existing six illustrative review cards, stock-photo labels, tutor profile dialogs, About sculpture/CEO message, Quran resources and portal Coming Soon pages remain. Inactive social links are now omitted.
- Confirmed pricing comparison uses labelled example frequency/count and quote-required actual fees, duration and cancellation terms. User requested continuing the remaining work without supplying business details.

## Education-inspired discovery redesign — 27 November 2026
- Reviewed current official content and desktop browser-rendered layouts for Novakid, Lingokids, AllviA and Cuemath; documented observations and original FCC adaptations in `design/EDUCATION-REFERENCES.md`.
- Visually reviewed the new hero, original transparent artwork, discovery card, percentages activity and the refreshed Quran header. The artwork loaded at its expected 1100-pixel size.
- Tested lesson tabs by mouse and keyboard (ArrowRight and Home), incorrect 10 and correct 20 feedback, reset control availability, and the 25% of 120 answer disclosure. Repeated the correct-answer flow at the smallest mobile frame width.
- Verified native homepage stage choices for Secondary and Higher secondary lead to the correctly preselected Learning Levels picker, including the stage name containing a space.
- Checked 50 layouts across Home, Subjects, Mathematics, Quran Education, Quran Reading, Tutors, About, Pricing, Learning Levels and Booking at 320, 375, 768, 1024 and 1440 frame widths. Fixed a narrow Mathematics information-card overflow by using a single-column layout and reducing the smallest hero title size; rechecked Mathematics at all five widths with no page overflow. The tested 320-pixel header also keeps Free Demo on one line.
- Tested grouped mobile navigation, resource submenu, submenu Escape then menu Escape, and desktop Resources → Free study notes navigation.
- Opened and closed Ayaan’s specific native profile dialog at the 320-pixel frame width (285-pixel dialog width). Confirmed readable dark-green Quran hero text on pale green and all four Quran course cards.
- Verified the global pause control on the new artwork. Existing reduced-motion, off-screen and inactive-tab rules cover the new motion. No field performance or conversion result is claimed.

## Motion-only update with protected homepage hero — 27 November 2026
- Compared the generated output to a pre-edit baseline: all 74 pages retain identical visible source wording, image attributes and anchor destinations. The homepage hero markup remains byte-for-byte identical (SHA-256 `92150cd32f063b04ec896800f7b22142921bf3242a7671bfaef45648f125e58c`).
- Browser compared the homepage hero before/after: width, height, background, heading font/colour, image URL and text all matched exactly. No new motion attributes occur within the hero.
- Verified stagger delays of 0/85/170/255ms, fully settled opacity and title reveals. Checked About illustration scroll drift changing with scroll, bounded to 22px.
- Found and corrected an entry-mask/IntersectionObserver interaction during QA; titles now reveal correctly on entering the viewport. Interactive cards/groups fade without positional motion, and a cold first click opens Ayaan’s specific tutor dialog.
- Checked 32 layouts across Home, About, Subjects, Mathematics, Pricing, Tutors, Quran Reading and Booking at 320, 375, 768 and 1440 frame widths: no horizontal page overflow.
- Tested mobile lesson feedback, tutor dialog opening/closing, and motion pause/resume. On mobile pause, all new nodes were visible and all new translations were disabled. Protected dialog descendants contain no new motion attributes.
- Reduced-motion, print, off-screen and inactive-tab rules are present; no browser media-preference emulation or field performance benchmark was performed.
