# Mobile header and navigation

27 November 2026

- Reproduced a missed menu activation when switching from Learning to Resources. The old pointerdown handler collapsed Learning before the click completed, moving the target away. Disclosure changes now close other groups after activation; outside presses still dismiss the sheet.
- A null relatedTarget during a touch focus change no longer cancels a pending link tap. Mobile links close the sheet after click activation; Escape, outside clicks, breakpoint changes and restored page history reset state.
- One 1099px navigation breakpoint replaces the mixed header/disclosure breakpoints. The sheet scrolls vertically in a single column and uses the available screen height.
- At 600px and below, the brand uses two lines, header controls retain 44px targets, right alignment matches the container, and the demo CTA moves inside the menu. The menu button displays a close icon while open.
- Added a visible Home link to the shared desktop and mobile navigation on all 71 pages. The existing logo remains a Home link.
- The approved home hero markup is unchanged.

## Verification

- Browser layout audit: Home, Quran Education and Contact at 320, 360, 375, 390, 414, 430, 600, 768, 940, 1024, 1099, 1100 and 1280px. All 39 layouts passed header width, right alignment, menu visibility, disclosure layout, link size, desktop overlap and Home destination checks.
- Real pointer clicks at 375px: menu open, Learning → Resources in one click, Free Notes navigation, and Home navigation from Free Notes passed.
- JavaScript syntax and all local routes/anchors checked.
