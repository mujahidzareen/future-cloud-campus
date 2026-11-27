# Scroll stacking, social channels and contact enquiries

Updated 27 November 2026 using the supplied video as the interaction reference.

The homepage hero is preserved. The lesson, tutors, Quran and resources form four opaque overlapping chapters. Native CSS sticky positioning pins a chapter while the next scrolls over it, with bounded recession/dimming. Stacking activates at 900px and only for chapters that fit beneath the live header; tall chapters and small screens use normal document flow. ResizeObserver rechecks changing lesson heights. Pause and reduced motion disable stacking; print uses normal flow. Keyboard focus returns covered chapters to their reading position.

All six social icons remain visible on Home, Contact and the footer. Verified, configured URLs become links. Missing URLs are explicitly unavailable / coming soon rather than guessed accounts.

The Contact form appears immediately below its hero, with required name, email, topic, message (10–2000 characters) and adult/privacy acknowledgement. Phone is optional. Preview review/edit/copy never sends or stores a message. Existing demo booking remains independent.

## Contact receiver contract

Set admissions.contact_endpoint to an approved HTTPS receiver, admissions.email, provider_name, provider_privacy_url and privacy_reviewed after confirming the integration. These determine contactLive in assets/intake-config.json. The demo endpoint is a separate setting. Browser code only posts when contactLive and the required receiver metadata are present; the current deployment is preview-only.

POST JSON fields: name, email, phone (possibly empty), topic, message, consent (true), type (contact), source (Future Cloud Campus), requestId (UUID), submittedAt (ISO timestamp). The honeypot value is never sent. A successful response must have HTTP 2xx and {"ok":true}, optionally reference. Anything else, including timeout or malformed JSON, shows an unconfirmed-receipt error and retains the input. The receiver must implement server validation, rate limiting, idempotency and approved retention/CORS rules. No credentials belong in static configuration.
