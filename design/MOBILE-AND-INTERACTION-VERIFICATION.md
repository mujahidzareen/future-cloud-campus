# Mobile imagery and interaction update — 27 November 2026

Eight original transparent clay educational scenes now accompany the existing route-specific topic artwork. Every one of the 69 inner pages has an animated scene, including the form-led booking page and the custom Reviews and mini-lesson headings. Home retains its exact approved hero markup, image and desktop geometry (1348 × 750.515625; heading font 600 81.78px Space Grotesk).

WebP exports are 900px (roughly 89–123KB) and 480px (roughly 38–51KB); picture sources load the smaller asset on narrow viewports. Prompts, scenes and source mapping are documented in CLAY-PAGE-SCENES.md and page_scenes.py. Fictional art is not presented as actual staff or customers.

## Responsive verification

Browser audit: 70 pages at 320, 375, 430, 768 and 1024px frame widths, 350 layouts. Final pass: zero flagged viewport overflow, text clipping, text/action boxes outside the content viewport or undersized button targets. The audit distinguishes the browser scrollbar gutter from viewport overflow; headings and actions are separately checked against the content viewport. Tested an actual mobile navigation sheet and its learning-levels destination, 320px tutor filtering and profile modal, retained input on the booking summary/edit flow, responsive scene rendering and global motion pause. System reduced-motion fallback was inspected in CSS, not browser-emulated. This covers these tested layouts in Chromium, not a claim of exhaustive testing of every device/browser.

Fixed narrow subject/info-card grids, long headings, header control compression, minimum button hit areas, iOS-size form fonts, wrapped actions, reader text-size buttons, modal width/scrolling, safe-area spacing and footer wrapping. The duplicate mobile header demo CTA is hidden below 421px while the working bottom demo invitation remains; form pages have their own visible actions and no overlay booking bar. Mobile Quick help is hidden to avoid obscuring content.

## Functional checks

- Mobile menu/dropdown destination and tutor search/reset, specific Omar profile popup and Escape.
- Complete sample demo enquiry through all three steps, review and edit with Chemistry retained; no request sent.
- AED sample pricing switch and contextual enquiry URL.
- Free Notes fractions search, reset to 12, and file/route checks for PDF and guide links.
- Quran Al-Baqarah ayah 25 opens ayahs 21–40; Next opens 41–60.
- Custom-package Mathematics selection updates the demo enquiry URL.
- Review Next and keyboard End; artwork pause/resume; four desktop pinned chapters and actual overlapping section positions.

Contact preview review/edit/copy was already tested and its implementation is unchanged. Actual admissions sending still requires a verified receiver; social icons remain explicitly unavailable until official URLs are supplied. These are not active fake links or fabricated receipts.

## Removed placeholders

Removed /portal/, /portal/parent/, /portal/teacher/ and the empty /careers/ placeholder, including header/footer links. Parents now links to the real progress example; the About portal card now opens the Contact form. The remaining site contains 70 substantive/review pages. Removed routes are deleted from static build output on every build and from the GitHub mirror.
