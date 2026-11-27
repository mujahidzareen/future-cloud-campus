# FCC education design review — 27 November 2026

Reviewed the four user-supplied homepages through their current official page content and browser-rendered desktop layouts. Also inspected programme discovery, section transitions, navigation, resource presentation and lesson-explanation controls where available. This is a qualitative design review, not a conversion or performance benchmark.

| Reference | Observed design principles | Original FCC adaptation |
| --- | --- | --- |
| [Novakid](https://www.novakidenglish.com/) | A clear parent-facing introduction, a prominent age choice, illustrated accents, tactile controls, and distinct lesson/process/teacher sections. | Four school-stage choices lead into FCC’s existing curriculum roadmap. A native GET form preserves the choice without asking for personal details. Stage names avoid assuming a universal age-to-grade mapping. |
| [Lingokids](https://lingokids.com/) | Bold colour changes, character-led imagery, short headlines, content-led galleries, deep button shadows and compact navigation groups. | A new original clay learning island, warm cream/cobalt/mint/yellow palette, compact pastel subject cards, a resource pair and restrained depth on hover/click. No Lingokids characters, media or brand assets are used. |
| [AllviA](https://www.allviaedu.com/en) | Large visual storytelling sections explain the relationship between learners, teachers, content and learning environments, with stage-oriented solution navigation. | An original interactive explanation of a learning cycle: Explain → Try it → Next step. Each panel demonstrates the idea rather than making unsupported platform claims. Existing portals retain their Coming Soon status. |
| [Cuemath](https://www.cuemath.com/en-gb/) | A direct one-to-one tutoring proposition, a highly visible starting action, a secondary lesson-explanation action, resource navigation and prominent family reassurance. | Primary demo enquiry plus a usable on-page learning preview, clearer programme discovery, a retained six-card feedback carousel and a practical pricing comparison. FCC does not inherit the reference’s customer counts, tutor-selection claims, ratings, prices or guarantees. |

## Resulting experience

- A brighter, more visual homepage with a two-line headline, relevant original 3D imagery and clear actions.
- Four stage choices lead to an already selected roadmap stage; a curriculum can then be chosen before continuing to the enquiry preview.
- The on-page percentages example uses native tabs with Left/Right/Home/End keyboard support, correct/incorrect feedback, reset and an answer disclosure. It sends no data and makes no assessment or achievement claim.
- Related content is grouped into Learning, Tutors, Resources, Pricing and About FCC. The Quran learning space stays in the homepage body and footer, as requested.
- New visual styling extends to inner-page heroes, illustration frames, cards, buttons, pricing, feedback, forms and the footer. Existing per-page illustrations, tutor dialogs, Quran reader and CEO section remain.
- Continuous motion is limited to featured artwork and the existing header logo. The new artwork pauses off-screen, in inactive tabs, with the site pause control and under reduced-motion preferences. The unused cursor-halo event handler was removed.
- Real admissions, business terms, official contact channels and approved real portraits/testimonials still depend on FCC content. Their current honest labels and preview gates remain.

## Original artwork

Asset: `dist/assets/people/learning-island-v2.webp` (private source) / `docs/assets/people/learning-island-v2.webp` (GitHub Pages). 1100 × 1100 RGBA, 173,780 bytes. Generated with the built-in image tool, then converted to WebP while preserving alpha. The original PNG remains in the working assets outside this repository.

Prompt: A professional transparent 3D clay learning island for FCC: two school-age learners, a blue/ivory laptop with a tutor illustration, an oversized blue book, cloud base, mint ruler, coral pencil and a small set of maths/science objects. Rounded tactile materials, warm studio lighting, cobalt/cyan/mint/cream/butter-yellow palette, generous silhouette space, no text/logos/watermarks or recognizable branded characters. The full image-generation brief described the same scene, composition, palette and exclusions. All depicted people are illustrations, not identifiable staff or customers.
