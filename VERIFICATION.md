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
