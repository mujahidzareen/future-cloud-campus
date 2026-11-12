"""Generate the crawlable, dependency-free FCC review site."""
import json
import os
import re
from html import escape
from pathlib import Path
from shutil import copytree
from content import SUBJECTS, QURAN, COUNTRIES, FAQ, STEPS
from artwork import ART, generate_artwork
from additions import EXTRA_SUBJECTS, GULF_COUNTRIES, CURRICULA, LEVELS, PLANS, ARTICLES, NOTES
from urllib.parse import urlencode

SUBJECTS = SUBJECTS + EXTRA_SUBJECTS
COUNTRIES = COUNTRIES + GULF_COUNTRIES

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "dist" / "assets"
if not ASSETS.is_dir():
    ASSETS = ROOT / "docs" / "assets"
DIST = Path(os.environ.get("FCC_OUTPUT", ASSETS.parent))
ORIGIN = os.environ.get("FCC_ORIGIN", "https://future-cloud-campus.greybow37.chatgpt.site").rstrip("/")
PAGES = []

if (DIST / "assets").resolve() != ASSETS.resolve():
    copytree(ASSETS, DIST / "assets", dirs_exist_ok=True)

generate_artwork(DIST)

def icon(name, extra=""):
    return f'<svg class="icon {extra}" aria-hidden="true"><use href="/assets/icons.svg#{name}"></use></svg>'

def button(text="Book a Free Demo", href="/book-a-demo/", variant="primary", glyph="arrow"):
    return f'<a class="btn {variant}" href="{href}">{text}{icon(glyph) if glyph else ""}</a>'

def brand(animate=False):
    image = '<img src="/assets/fcc-symbol.png" width="54" height="54" alt="">'
    emblem = image
    if animate:
        edges = "".join(f'<span class="brand-edge" style="--depth:{depth}px"></span>' for depth in range(-4, 5))
        emblem = f'<span class="brand-emblem"><span class="brand-spin">{edges}<span class="brand-face brand-front">{image}</span><span class="brand-face brand-back">{image}</span></span></span>'
    return f'<a class="brand" href="/" aria-label="Future Cloud Campus home">{emblem}<span>Future Cloud<span class="brand-accent"> Campus</span><small>ONE CAMPUS. ENDLESS LEARNING.</small></span></a>'

def nav(path):
    links = [("/subjects/", "Subjects"), ("/curricula/", "Curricula"), ("/free-notes/", "Free Notes")]
    def link(url, label):
        return f'<a href="{url}"{(" aria-current=page" if path == url else "")}>{label}</a>'
    def dropdown(label, links):
        return f'<details class="nav-dropdown"><summary>{label}<span aria-hidden="true">⌄</span></summary><div class="nav-popover">{"".join(link(url, text) for url, text in links)}</div></details>'
    items = "".join(link(url, label) for url, label in links)
    items += dropdown("Pricing", [("/pricing/", "Plans & pricing"), ("/custom-package/", "Custom packages")])
    items += dropdown("Discover", [("/about/", "About FCC"), ("/how-it-works/", "How it works"), ("/learning-levels/", "Learning levels"), ("/test-prep/", "Exam preparation"), ("/progress/", "Learning & progress"), ("/journal/", "Blogs & Articles"), ("/countries/", "Countries"), ("/parents/", "For parents"), ("/contact/", "Contact & FAQs")])
    return f'''<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="shell nav">{brand(True)}
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-links" aria-label="Open menu">{icon("menu")}</button>
    <nav id="nav-links" class="nav-links" aria-label="Main navigation">{items}<a class="mobile-portal" href="/portal/">Portal</a></nav>
    <div class="nav-actions"><button class="site-motion" type="button" data-motion-global aria-pressed="false" aria-label="Pause animations" title="Pause animations" hidden><svg class="icon" aria-hidden="true" viewBox="0 0 24 24"><path class="pause-bars" d="M9 5v14M15 5v14"/><path class="resume-triangle" d="m8 5 11 7-11 7z"/></svg></button><a class="portal-link" href="/portal/">{icon("lock")} Portal</a>{button("Free Demo")}</div></div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="shell footer-main"><div class="footer-brand">{brand()}<p>Live online learning for families across time zones.</p></div>
    <div><strong>Explore</strong><a href="/subjects/">Academic subjects</a><a href="/quran-education/">Quran Education</a><a href="/curricula/">Curricula</a><a href="/test-prep/">Exam preparation</a><a href="/countries/">Countries</a></div>
    <div><strong>Families</strong><a href="/how-it-works/">How it works</a><a href="/parents/">For parents</a><a href="/pricing/">Plans &amp; pricing</a><a href="/free-notes/">Free Notes</a><a href="/faq/">FAQs</a><a href="/portal/">Parent &amp; Teacher Portal</a></div>
    <div><strong>Campus</strong><a href="/about/">About FCC</a><a href="/contact/">Contact &amp; admissions</a><a href="/journal/">Blogs &amp; Articles</a><a href="/careers/">Careers</a></div></div>
    <div class="shell footer-legal"><span>© 2026 Future Cloud Campus</span><div><a href="/privacy/">Privacy</a><a href="/cookies/">Cookies</a><a href="/terms/">Terms</a><a href="/refund-cancellation/">Cancellations</a><a href="/safeguarding/">Safeguarding</a></div></div></footer>'''

def page(path, title, description, body, crumbs=None):
    full_title = title if path == "/" else f"{title} | Future Cloud Campus"
    meta = escape(description, quote=True)
    canonical = ORIGIN + path
    schema = {"@context":"https://schema.org","@type":"EducationalOrganization","name":"Future Cloud Campus","url":ORIGIN+"/","logo":ORIGIN+"/assets/fcc-lockup.png"}
    structured = [schema] if path == "/" else []
    if crumbs:
        structured.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":name,"item":ORIGIN+url} for i,(name,url) in enumerate(crumbs)]})
    structured_markup = "".join(f'<script type="application/ld+json">{json.dumps(item)}</script>' for item in structured)
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>{escape(full_title)}</title><meta name="description" content="{meta}"><meta name="theme-color" content="#f8f7ff">
    <meta name="robots" content="noindex, nofollow"><link rel="canonical" href="{canonical}"><link rel="icon" href="/assets/fcc-symbol.png" type="image/png">
    <meta property="og:type" content="website"><meta property="og:title" content="{escape(full_title)}"><meta property="og:description" content="{meta}">
    <meta property="og:url" content="{canonical}"><meta property="og:image" content="{ORIGIN}/assets/fcc-lockup.png"><meta name="twitter:card" content="summary">
    <link rel="preload" href="/assets/fonts/inter-variable.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/assets/site.css"><script defer src="/assets/site.js"></script>{structured_markup}
    </head><body>{nav(path)}<main id="main">{body}</main>{footer()}<details class="quick-help"><summary>{icon("language")}<span>Quick help</span></summary><div><h2>Find your next step.</h2><a href="/subjects/">Explore subjects</a><a href="/pricing/">Plans &amp; fees</a><a href="/free-notes/">Read free notes</a><a href="/faq/">Common questions</a><a href="/book-a-demo/">Book a free demo</a></div></details></body></html>'''
    relative_root = "../" * len(Path(path.strip("/")).parts) or "./"
    doc = re.sub(r'(\b(?:href|src)="/)(?!/)', lambda match: match[0][:-1] + relative_root, doc)
    file = DIST / path.strip("/") / "index.html"
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(doc, encoding="utf-8")
    PAGES.append(path)

def section_head(kicker, title, description=""):
    return f'<div class="section-head"><div class="eyebrow"><i></i>{kicker}</div><h2>{title}</h2>{f"<p>{description}</p>" if description else ""}</div>'

def breadcrumb(items):
    return '<nav aria-label="Breadcrumb" class="crumb">' + " / ".join(f'<a href="{url}">{label}</a>' for label, url in items[:-1]) + f' / <span aria-current="page">{items[-1][0]}</span></nav>'

def page_illustration(route, extra=""):
    key = route.strip("/")
    title = ART[key][0]
    image = key.replace("/", "-") + ".svg"
    return f'<figure class="page-illustration tilt {extra}"><img class="ambient-art" src="/assets/pages/{image}" alt="{escape(title, quote=True)}" width="480" height="360" decoding="async"></figure>'

def hero_small(kicker, title, text, crumbs, actions="", tile="book", tone="violet"):
    return f'<section class="inner-hero"><div class="shell">{breadcrumb(crumbs)}<div class="inner-hero-content"><div><div class="eyebrow"><i></i>{kicker}</div><h1>{title}</h1><p>{text}</p>{f"<div class=hero-actions>{actions}</div>" if actions else ""}</div>{page_illustration(crumbs[-1][1])}</div></div></section>'

def cards(limit=None):
    return '<div class="subject-grid">' + ''.join(f'''<a class="subject-card tilt reveal" href="/{slug}/">
    <span class="clay-icon {color}">{icon(glyph)}</span><h3>{name}</h3><p>{tag}</p><span class="card-arrow">{icon("diagonal")}<span class="sr-only">Explore {name}</span></span></a>'''
    for slug, name, glyph, color, tag, *_ in SUBJECTS[:limit]) + '</div>'

def timeline():
    return '<ol class="steps">' + ''.join(f'''<li class="step reveal"><div class="step-mark"><span class="clay-icon violet">{icon(glyph)}</span><span class="step-num">{i:02}</span></div><h3>{title}</h3><p>{desc}</p></li>'''
    for i, (title, desc, glyph) in enumerate(STEPS, 1)) + '</ol>'

def accordions(items):
    return '<div class="accordion">' + ''.join(f'<details><summary>{q}<span>{icon("plus")}</span></summary><p>{a}</p></details>' for q,a in items) + '</div>'

def cta(course=""):
    href = f"/book-a-demo/?course={course}" if course else "/book-a-demo/"
    return f'''<section class="shell final-wrap reveal"><div class="final-cta"><div><span class="eyebrow"><i></i>YOUR FIRST STEP</span><h2>Let’s find the right starting point.</h2><p>Tell us what your child would like to work on.</p></div>{button("Book a Free Demo", href, "light")}</div></section>'''

def progress():
    return f'''<div class="report tilt reveal"><div class="report-header"><div class="clay-icon violet">{icon("chart")}</div><div><h3>Learning progress</h3><p>Mathematics · Sample evaluation</p></div><span class="badge">Illustrative</span></div>
    <div class="report-row"><span>{icon("check")} Strength</span><b>Explains equivalent fractions</b></div>
    <div class="report-row"><span>{icon("book")} Practise</span><b>Adding unlike denominators</b></div>
    <div class="report-row"><span>{icon("calendar")} Next lesson</span><b>Use visual models, then practise</b></div></div>'''

def country_picker():
    tabs = ''.join(f'<button type="button" class="country-btn" data-country="{slug}" aria-pressed="{str(i==0).lower()}"><span aria-hidden="true">{flag}</span> {name}</button>' for i,(slug,name,flag,*_) in enumerate(COUNTRIES))
    panels = ''.join(f'''<div class="country-panel" data-panel="{slug}"{"" if i==0 else " hidden"}><div><h3>{heading}</h3><p>{summary}</p></div>{button("Explore "+name, f"/{slug}/", "secondary", "diagonal")}</div>''' for i,(slug,name,flag,heading,summary,_) in enumerate(COUNTRIES))
    return f'<div class="country-picker reveal"><div class="country-buttons" aria-label="Select a country">{tabs}</div>{panels}<noscript><p><a href="/usa/">United States</a> · <a href="/canada/">Canada</a></p></noscript></div>'

def tiles(items):
    return '<div class="info-grid">' + ''.join(f'<article class="info-card tilt reveal"><span class="tile-number">{i:02}</span><h3>{h}</h3><p>{p}</p></article>' for i,(h,p) in enumerate(items,1)) + '</div>'

def catalog_filter(label, placeholder):
    return f'<div class="catalog-toolbar"><label>{label}<input type="search" data-filter placeholder="{placeholder}" autocomplete="off"></label><p data-result-count role="status"></p></div>'

def image_card(route, title, description, label="Explore", kicker=""):
    image = route.strip("/").replace("/", "-") + ".svg"
    return f'<a class="story-card tilt reveal" href="{route}"><div class="story-picture"><img src="/assets/pages/{image}" alt="" width="480" height="360" loading="lazy"></div><div class="story-copy">{f"<span class=card-kicker>{kicker}</span>" if kicker else ""}<h3>{title}</h3><p>{description}</p><span class="text-link">{label} {icon("diagonal")}</span></div></a>'

def resource_teasers():
    return image_card("/free-notes/", "Free study notes", "Twelve topic guides with worked examples and practice answers.", "Open the library", "READ & DOWNLOAD") + image_card("/journal/", "Blogs & Articles", "Practical ideas for studying, online lessons and exam practice.", "Browse articles", "THE STUDY JOURNAL")

def extra_page(route, title, kicker, intro, body, actions=""):
    crumbs = [("Home", "/"), (title, route)]
    if route.startswith("/curricula/") and route != "/curricula/":
        crumbs.insert(1, ("Curricula", "/curricula/"))
    if route.startswith("/journal/") and route != "/journal/":
        crumbs.insert(1, ("Blogs & Articles", "/journal/"))
    if route.startswith("/free-notes/") and route != "/free-notes/":
        crumbs.insert(1, ("Free Notes", "/free-notes/"))
    page(route, title, intro, hero_small(kicker, title, intro, crumbs, actions) + body, crumbs)


def home():
    return f"""
    <section class="hero"><div class="shell hero-grid">
      <div class="hero-copy">
        <div class="hero-tag"><span>{icon("star")}</span> LIVE ONLINE TUTORING</div>
        <h1>Learning that<br><em>fits your child.</em></h1>
        <p>One-to-one lessons that build confidence in school subjects, at your child’s pace.</p>
        <div class="hero-actions">{button()}{button("Explore Subjects","/subjects/","secondary","diagonal")}</div>
      </div>
      <figure class="hero-art tilt" data-hero>
        <img class="hero-learning-picture" src="/assets/hero-live-learning.webp" width="1280" height="960" alt="A clay-style laptop showing a live lesson, resting on books with a pencil and science model" fetchpriority="high" decoding="async">
        <figcaption>ONE CAMPUS. ENDLESS LEARNING.</figcaption>
      </figure>
    </div></section>
    <section class="trust shell" aria-label="What families can expect">
      <div>{icon("people")}<strong>Live 1-to-1 lessons</strong></div>
      <div>{icon("clock")}<strong>Flexible scheduling</strong></div>
      <div>{icon("chart")}<strong>Clear progress goals</strong></div>
      <div>{icon("globe")}<strong>Learn from anywhere</strong></div>
    </section>
    <section class="shell section" id="subjects"><div class="section-heading-row">{section_head("ACADEMIC TUTORING","Explore our subjects.")}<a class="text-link" href="/subjects/">All subjects {icon("arrow")}</a></div>{cards(5)}</section>
    <section class="shell program-wrap reveal" aria-labelledby="quran-feature-title">
      <div class="quran-feature">
        <div class="quran-stage tilt" aria-hidden="true">
          <div class="quran-stage-bg"></div><span class="quran-orbit"></span><span class="quran-star quran-star-top">✧</span><span class="quran-star quran-star-bottom">✦</span>
          <img src="/assets/quran.svg" alt="" width="500" height="350" loading="lazy">
        </div>
        <div class="quran-feature-copy">
          <div class="eyebrow"><i></i> OUR QURAN PROGRAMME</div><h2 id="quran-feature-title">Quran Education</h2>
          <p>Build confidence in Quran reading and recitation with live, one-to-one guidance.</p>
          <ul class="program-topics" aria-label="Featured courses"><li>Noorani Qaida</li><li>Quran Reading</li><li>Tajweed</li><li>Islamic Studies</li></ul>
          {button("Explore Quran Education","/quran-education/","quran-btn","diagonal")}
        </div>
      </div>
    </section>
    <section class="band"><div class="shell section"><div class="section-heading-row">{section_head("THE LEARNING JOURNEY","How it works.")}<a class="text-link" href="/how-it-works/">See the steps {icon("arrow")}</a></div>{timeline()}</div></section>
    <section class="shell section regional-strip">{section_head("LOCAL SUPPORT","Find your country.")}<div class="region-links">{''.join(f'<a class="region-pill tilt" href="/{slug}/"><span aria-hidden="true">{flag}</span>{name}{icon("diagonal")}</a>' for slug,name,flag,*_ in COUNTRIES[:3])}</div></section>
    <section class="shell section learning-pathways">{section_head("YOUR NEXT STEP","Support beyond the lesson.")}
      <div class="feature-links">
        <a class="feature-link tilt reveal" href="/curricula/"><span class="clay-icon blue">{icon("globe")}</span><h3>Follow your curriculum</h3><p>British, American, IB and Pakistan school courses.</p>{icon("diagonal")}</a>
        <a class="feature-link tilt reveal" href="/test-prep/"><span class="clay-icon mint">{icon("calendar")}</span><h3>Prepare for an exam</h3><p>Make a focused plan around your subject and date.</p>{icon("diagonal")}</a>
        <a class="feature-link tilt reveal" href="/pricing/"><span class="clay-icon violet">{icon("people")}</span><h3>Find a lesson plan</h3><p>Explore weekly support and custom packages.</p>{icon("diagonal")}</a>
      </div>
    </section>
    <section class="band"><div class="shell section"><div class="section-heading-row">{section_head("THE RESOURCE ROOM","Read. Practise. Explore.")}<a class="text-link" href="/free-notes/">Free study notes {icon("arrow")}</a></div><div class="resource-teasers">{resource_teasers()}</div></div></section>
    <section class="shell section faq-grid home-faq"><div>{section_head("GOOD TO KNOW","Questions families ask.")}<a class="text-link" href="/faq/">All questions {icon("arrow")}</a></div>{accordions(FAQ[:3])}</section>
    {cta()}"""

page("/", "Future Cloud Campus | Online Tutoring & Quran Education", "Live one-to-one online tutoring and Quran Education for families. Explore academic subjects and find the right starting point with a free demo.", home())

crumbs = [("Home","/"),("Subjects","/subjects/")]
page("/subjects/","Academic subjects","Explore school subjects, from mathematics and sciences to languages, humanities, business and computing.",hero_small("ACADEMIC TUTORING","Find your subject. Build your confidence.","Explore the subject library and find the right starting point for your child.",crumbs,button())+f'<section class="shell section subject-catalog" data-catalog>{catalog_filter("Find a subject", "Search subjects and learning goals")}{cards()}<p class="catalog-empty" hidden>No subjects match. Try a different word.</p></section>'+cta(),crumbs)

for slug,name,glyph,tone,tag,desc,topics,audience,faq in SUBJECTS:
    path=f"/{slug}/"
    crumbs=[("Home","/"),("Subjects","/subjects/"),(name,path)]
    page(path,name+" tutoring",desc,hero_small("LIVE ACADEMIC TUTORING",name,desc,crumbs,button(href=f"/book-a-demo/?course={slug}"),glyph,tone)+
        f'<section class="shell section">{section_head("WHAT STUDENTS LEARN",tag)}{tiles(topics)}</section><section class="band"><div class="shell section two-col">{section_head("WHO IT’S FOR","Start with the learner.",audience)}{tiles([("One-to-one lessons","The tutor explains a concept, guides a practice task and checks understanding. Discuss lesson length and platform during the demo."),("Assessment and progress","The first session helps identify the starting level. Goals and periodic evaluations guide the next lessons.")])}</div></section><section class="shell section faq-grid">{section_head("QUESTIONS",f"About {name} tutoring")}{accordions([faq, FAQ[0]])}</section>'+cta(slug),crumbs)

crumbs=[("Home","/"),("Quran Education","/quran-education/")]
quran_cards=''.join(f'<a class="subject-card quran-subject tilt reveal" href="/{slug}/"><span class="clay-icon mint">{icon("book")}</span><h3>{name}</h3><p>{desc}</p><span class="card-arrow">{icon("diagonal")}</span></a>' for slug,name,desc,_ in QURAN)
page("/quran-education/","Quran Education","Explore live Quran Reading, Noorani Qaida, Tajweed and Islamic Studies at Future Cloud Campus.",
    f'<section class="inner-hero quran-inner"><div class="shell">{breadcrumb(crumbs)}<div class="inner-hero-content"><div><div class="eyebrow"><i></i>DEDICATED LEARNING PATH</div><h1>Quran Education</h1><p>One-to-one learning with a clear starting level, guided practice and progress updates for families.</p><div class="hero-actions">{button(href="/book-a-demo/?course=quran-education",variant="light")}</div></div>{page_illustration("/quran-education/", "quran-page-art")}</div></div></section>'
    +f'<section class="shell section">{section_head("COURSES","Find a starting point.")}<div class="subject-grid quran-grid">{quran_cards}</div></section><section class="band"><div class="shell section">{section_head("THE LEARNING APPROACH","Assessment, practice and review.")}{tiles([("Initial placement","Discuss age, prior reading and preferred times. The teacher can check letter recognition or listen to a short reading sample."),("Teacher match","Ask admissions about teacher fit, the selection process and gender matching availability for your schedule."),("Progress feedback","Review the previous lesson, fluency and Tajweed. The evaluation can record strengths, practice areas and the recommended pace.")])}</div></section>'+cta("quran-education"),crumbs)
for slug,name,desc,outcomes in QURAN:
    path=f"/{slug}/"
    crumbs=[("Home","/"),("Quran Education","/quran-education/"),(name,path)]
    page(path,name,desc,hero_small("QURAN EDUCATION",name,desc,crumbs,button(href=f"/book-a-demo/?course={slug}"),"book","mint")+
        f'<section class="shell section">{section_head("INSIDE THE LESSON","Learn at an appropriate pace.")}{tiles([("What we practise",outcomes),("Who it’s for","Share the learner’s age and previous experience. The initial assessment helps place the learner at a suitable level."),("How we review progress","The teacher checks the previous lesson, offers feedback and identifies a realistic focus for the next class.")])}</section><section class="shell section faq-grid">{section_head("QUESTIONS","Scheduling and assessment")}{accordions([FAQ[0],FAQ[2]])}</section>'+cta(slug),crumbs)

crumbs=[("Home","/"),("Countries & curricula","/countries/")]
page("/countries/","Countries & curricula","Find curriculum and time zone guidance for families in the UK, USA, Canada and Gulf countries.",hero_small("GLOBAL LEARNING","Find guidance for your country.","Share the school curriculum, current topics and local time zone so we can discuss the right support.",crumbs,tile="globe")+f'<section class="shell section">{country_picker()}</section>'+cta(),crumbs)
for slug,name,flag,heading,desc,time in COUNTRIES:
    path=f"/{slug}/"
    crumbs=[("Home","/"),("Countries","/countries/"),(name,path)]
    page(path,f"Online tutoring in {name}",desc,hero_small("COUNTRY & CURRICULUM",f"Online tutoring in {name}",desc,crumbs,button(href=f"/book-a-demo/?country={slug}"),"globe")+
        f'<section class="shell section">{section_head("PLAN YOUR LESSONS",heading)}{tiles([("Before the demo",desc),("Scheduling",time),("Available subjects","Explore Mathematics, English, Science, Computer & IT, Logical Reasoning and Quran Education.")])}</section><section class="shell section">{cards(5)}<a class="text-link" href="/subjects/">Explore all subjects</a></section>'+cta(),crumbs)

crumbs=[("Home","/"),("How it works","/how-it-works/")]
page("/how-it-works/","How it works","Learn how tutor matching, a free demo and a personalised learning plan fit together.",hero_small("THE LEARNING JOURNEY","Start with one conversation.","Tell us what’s going well, where your child is getting stuck and what you’d like to achieve.",crumbs,button(),"calendar")+f'<section class="shell section">{timeline()}</section><section class="band"><div class="shell section faq-grid">{section_head("PLANNING YOUR FIRST LESSON","Questions before you start.")}{accordions(FAQ)}</div></section>'+cta(),crumbs)

crumbs=[("Home","/"),("For Parents","/parents/")]
page("/parents/","For parents","See how Future Cloud Campus uses learning goals and progress evaluations to guide the next lesson.",hero_small("FOR FAMILIES","Stay close to your child’s learning.","Follow the learning plan and use tutor feedback to see what needs practice next.",crumbs,button("See what’s coming to the Parent Portal","/portal/parent/","secondary"),"chart")+f'<section class="shell section two-col">{section_head("EXAMPLE EVALUATION","What a progress update can tell you.","This example shows how a tutor can translate lesson observations into a practical next step.")}{progress()}</section><section class="band"><div class="shell section">{section_head("PARENT RESOURCES","Before and between lessons.")}{tiles([("Before the demo","Have a recent school topic or a question in mind. Consider what would make the next few weeks of learning feel successful."),("Between lessons","Ask the tutor for a short practice activity and give your child time to explain how they approached it."),("At a progress review","Look for the current goal, an example of progress, and the focus for the next lesson.")])}</div></section>'+cta(),crumbs)

crumbs=[("Home","/"),("FAQs","/faq/")]
page("/faq/","FAQs","Answers about live lessons, tutor matching, progress and preparing for a free demo.",hero_small("FAMILY FAQ","Questions families ask.","Find out what to prepare and how online lessons are designed.",crumbs,tile="language")+f'<section class="shell section faq-grid">{section_head("COMMON QUESTIONS","Before your first lesson.")}{accordions(FAQ)}</section>'+cta(),crumbs)

crumbs=[("Home","/"),("About","/about/")]
page("/about/","About Future Cloud Campus","Learn about Future Cloud Campus and its one-to-one academic tutoring and Quran Education.",hero_small("OUR CAMPUS","One campus. Endless learning.","Future Cloud Campus brings live one-to-one academic tutoring and Quran Education together in a single learning experience for families.",crumbs,button(),"globe")+f'<section class="shell section">{section_head("OUR APPROACH","A lesson built around the learner.")}{tiles([("Start with the right level","A short assessment and a conversation about the learner’s goals help set the starting point."),("Practise with guidance","The tutor adapts the activity and pace based on how the learner responds."),("Review progress","Use lesson observations and periodic evaluations to agree on the next area to practise.")])}</section>',crumbs)

for slug, name, desc, details, glyph in [
    ("contact","Contact & admissions","Tell admissions which programme, level and time zone you’re interested in.","Start with a demo enquiry for lessons or a custom package. Share your school course, subject and preferred local times.","language"),
    ("careers","Careers","Teach live online with a focus on individual learning goals and clear feedback.","Open roles and a secure application form can be published here once the hiring team confirms its recruitment details.","people"),
]:
    path=f"/{slug}/"
    crumbs=[("Home","/"),(name,path)]
    page(path,name,desc,hero_small("FUTURE CLOUD CAMPUS",name,desc,crumbs,button("Preview the demo form",variant="secondary") if slug=="contact" else "",glyph)+f'<section class="shell section"><div class="notice">{icon("language")}<p>{details}</p></div>{("<div class=resource-teasers>"+resource_teasers()+"</div>") if slug == "contact" else ""}</section>'+(f'<section class="shell section faq-grid">{section_head("ADMISSIONS","Before you get in touch.")}{accordions(FAQ[:3])}</section>' if slug == "contact" else ""),crumbs)

POLICIES = {
    "privacy":("Privacy","The preview form is for sample details. It does not transmit or store submissions. Before live intake, FCC must approve how guardian details are collected, retained, shared and deleted."),
    "cookies":("Cookies","The site preview does not set application cookies or load analytics or advertising scripts. The hosting provider may use its own sign-in controls."),
    "terms":("Terms","This is a review version. Enrollment terms, class arrangements and payment conditions must be confirmed by Future Cloud Campus before public launch."),
    "refund-cancellation":("Refunds & cancellations","Future Cloud Campus will need to confirm how families can reschedule or cancel lessons and when refunds are available before taking live bookings or payments."),
    "safeguarding":("Safeguarding","The portals are coming soon. Before opening live services, FCC must approve its safeguarding policy, designate a reporting contact and confirm access and retention rules for any student records."),
}
for slug, (name, desc) in POLICIES.items():
    path=f"/{slug}/"
    crumbs=[("Home","/"),(name,path)]
    page(path,name,f"{name} information for the Future Cloud Campus review site.",hero_small("PREVIEW INFORMATION",name,desc,crumbs,tile="shield"),crumbs)

crumbs=[("Home","/"),("Book a Free Demo","/book-a-demo/")]
options = ''.join(f'<option value="{slug}">{escape(name)}</option>' for slug, name, *_ in SUBJECTS + [("quran-education","Quran Education")] + QURAN)
country_options = ''.join(f'<option value="{slug}" data-code="{code}">{name}</option>' for slug,name,code in [
    ("uk","United Kingdom","+44"),("usa","United States","+1"),("canada","Canada","+1"),("ireland","Ireland","+353"),("australia","Australia","+61"),("new-zealand","New Zealand","+64"),("pakistan","Pakistan","+92"),("uae","United Arab Emirates","+971"),("saudi-arabia","Saudi Arabia","+966"),("qatar","Qatar","+974"),("oman","Oman","+968"),("other-countries","Other countries",""),("other","Other","")])
form=f'''<section class="form-band"><div class="shell">{breadcrumb(crumbs)}<div class="form-layout">
  <div class="form-intro"><div class="eyebrow"><i></i>ADMISSIONS</div><h1>Book a Free Demo</h1><p>Tell us what your child would like to learn and when your family is available.</p>
  {page_illustration("/book-a-demo/", "booking-art")}<div class="form-guide"><span class="clay-icon violet">{icon("calendar")}</span><div><h2>What happens next?</h2><p>In the live booking process, admissions will review the request, discuss tutor availability and confirm a demo time with you.</p></div></div>
  <div class="notice">{icon("lock")}<p><strong>Preview only.</strong> Use sample details. The form previews the request on this page and sends nothing to admissions.</p></div>
  </div>
  <form class="demo-form" id="demo-form" autocomplete="off" method="dialog" data-preview>
    <h2>Demo request</h2><p class="form-hint">Fields marked with * are required.</p>
    <div class="field-grid">
      <label>Parent or guardian name *<input name="name" required maxlength="100" placeholder="Sample Parent"></label>
      <label>Email *<input name="email" type="email" required maxlength="160" placeholder="parent@example.com"></label>
      <label>Country *<select name="country" required><option value="">Select country</option>{country_options}</select></label>
      <label>Time zone *<select name="timezone" required><option value="">Select time zone</option><option value="Europe/London">UK · London</option><option value="Europe/Dublin">Ireland · Dublin</option><option value="America/New_York">US · Eastern</option><option value="America/Chicago">US · Central</option><option value="America/Denver">US · Mountain</option><option value="America/Los_Angeles">US · Pacific</option><option value="America/Anchorage">US · Alaska</option><option value="Pacific/Honolulu">US · Hawaii</option><option value="America/Toronto">Canada · Eastern</option><option value="America/Vancouver">Canada · Pacific</option><option value="America/Edmonton">Canada · Mountain</option><option value="America/Winnipeg">Canada · Central</option><option value="America/Halifax">Canada · Atlantic</option><option value="America/St_Johns">Canada · Newfoundland</option><option value="Australia/Sydney">Australia · Sydney</option><option value="Australia/Perth">Australia · Perth</option><option value="Pacific/Auckland">New Zealand · Auckland</option><option value="Asia/Karachi">Pakistan · Karachi</option><option value="Asia/Dubai">UAE · Dubai</option><option value="Asia/Riyadh">Saudi Arabia · Riyadh</option><option value="Asia/Qatar">Qatar · Doha</option><option value="Asia/Muscat">Oman · Muscat</option><option value="other">Other / discuss availability</option></select></label>
      <div class="phone-field"><label>Country code *<select name="code" required><option value="">Code</option><option>+44</option><option>+1</option><option>+353</option><option>+61</option><option>+64</option><option>+92</option><option>+971</option><option>+966</option><option>+974</option><option>+968</option><option value="other">Other</option></select></label><label>WhatsApp / phone *<input name="phone" type="tel" required maxlength="22" minlength="7" pattern="[+0-9 \\(\\)\\-]{{7,22}}" title="Enter a phone number using digits, spaces, parentheses, plus or hyphen." placeholder="7700 900000"></label></div>
      <label>Age, year or grade *<input name="level" required maxlength="50" placeholder="e.g. Year 8"></label>
      <label>Subject or course *<select name="course" required><option value="">Select a subject</option>{options}</select></label>
      <label>Preferred days and time<input name="time" maxlength="100" placeholder="e.g. Tuesday after 5 pm"></label>
      <label>Lesson plan<select name="plan"><option value="">Discuss a plan</option><option>Weekly support</option><option>Progress plan</option><option>Exam focus</option><option>Custom package</option></select></label>
      <label>Curriculum or exam<input name="curriculum" maxlength="120" placeholder="e.g. GCSE Chemistry, AQA"></label>
      <label class="field-wide">Learning goal<textarea name="goal" maxlength="400" rows="3" placeholder="e.g. Practise fractions and word problems"></textarea></label>
    </div>
    <button class="btn primary" type="submit" disabled>Preview demo request {icon("arrow")}</button><noscript><p>Enable JavaScript to test the demo request preview.</p></noscript>
  </form>
  <div class="demo-form confirmation" id="confirmation" hidden tabindex="-1"><span class="clay-icon mint">{icon("check")}</span><h2>Your request preview</h2><p>Review the sample booking details below. No demo has been booked.</p><dl id="request-summary"></dl><button class="btn secondary" type="button" data-edit>Edit sample details {icon("arrow")}</button></div>
</div></div></section>'''
page("/book-a-demo/","Book a Free Demo","Preview the Future Cloud Campus demo request form for academic tutoring and Quran Education.",form,crumbs)

PORTALS = {
    "parent": ("Parent Portal", "A clearer view of your child’s learning, from upcoming lessons to the tutor’s next recommendation.", [
        ("Lesson schedule", "calendar", "See upcoming sessions in your local time."),
        ("Progress updates", "chart", "See what your child is working on and where they need practice."),
        ("Attendance", "check", "Review which lessons your child attended."),
    ]),
    "teacher": ("Teacher Portal", "A workspace for planning lessons, recording attendance and sharing feedback with families.", [
        ("Teaching schedule", "calendar", "Check your upcoming classes and assigned learners."),
        ("Lesson notes", "book", "Record what you covered and what to practise next."),
        ("Learning evaluations", "chart", "Capture strengths, progress and priorities for the next session."),
    ]),
}

def portal_page(role=None):
    path = f"/portal/{role}/" if role else "/portal/"
    title = PORTALS[role][0] if role else "Parent &amp; Teacher Portals"
    intro = PORTALS[role][1] if role else "We’re building dedicated workspaces for families and tutors to manage lessons and follow learning progress."
    crumbs = [("Home", "/"), ("Portal", "/portal/")]
    if role:
        crumbs.append((title, path))
    nav = "".join(
        f'<a href="/portal/{key}/"{" aria-current=page" if key == role else ""}>{icon("people" if key == "parent" else "book")}{name}</a>'
        for key, (name, *_rest) in PORTALS.items()
    )
    art = page_illustration(path, "portal-illustration")
    banner = f"""<section class="launch-section"><div class="shell">{breadcrumb(crumbs)}
      <div class="launch-banner"><div class="launch-copy">
        <span class="launch-status"><i></i> IN DEVELOPMENT</span>
        <p class="launch-product">{title}</p><h1>Coming<br>soon<span>.</span></h1>
        <p class="launch-intro">{intro}</p>
        <div class="hero-actions">{button("Explore Subjects", "/subjects/", "light")}{button("Back to Home", "/", "launch-back", "")}</div>
      </div>{art}</div>
      <nav class="launch-nav" aria-label="Choose a portal">{nav}</nav>
    </div></section>"""
    if role:
        features = PORTALS[role][2]
        upcoming = '<div class="info-grid">' + "".join(
            f'<article class="info-card tilt reveal"><span class="clay-icon {tone}">{icon(glyph)}</span><h3>{name}</h3><p>{desc}</p></article>'
            for (name, glyph, desc), tone in zip(features, ("violet", "blue", "mint"))
        ) + '</div>'
    else:
        upcoming = '<div class="portal-grid">' + "".join(
            f'<a class="subject-card tilt reveal" href="/portal/{key}/"><span class="clay-icon {tone}">{icon(glyph)}</span><h3>{name}</h3><p>{desc}</p><span class="card-arrow">{icon("diagonal")}</span></a>'
            for (key, (name, desc, _)), tone, glyph in zip(PORTALS.items(), ("violet", "blue"), ("people", "book"))
        ) + '</div>'
    body = banner + f'<section class="shell section">{section_head("IN THE WORKS", "What you’ll be able to do.")}{upcoming}</section>'
    page(path, f"{title.replace('&amp;', '&')} Coming Soon", intro, body, crumbs)

for role in (None, *PORTALS):
    portal_page(role)

# Additional learning pathways and resources.
curriculum_cards = "".join(image_card(f"/curricula/{slug}/", name, desc, "Explore curriculum") for slug,name,desc,_ in CURRICULA)
extra_page("/curricula/", "Your course. Your starting point.", "CURRICULA",
           "Explore support shaped around your school syllabus, level and learning goals.",
           f'<section class="shell section"><div class="story-grid two-up">{curriculum_cards}</div></section><section class="shell note-band"><h2>Start with your syllabus.</h2><p>Your country and curriculum can be different. Share the school course, exam board and current topics when you enquire.</p></section>'+cta())
for slug,name,desc,topics in CURRICULA:
    route=f"/curricula/{slug}/"
    href="/book-a-demo/?"+urlencode({"curriculum":name})
    extra_page(route,name,"CURRICULUM SUPPORT",desc,
               f'<section class="shell section">{section_head("THE LEARNING PLAN","Focus on the right course.")}{tiles(topics)}</section><section class="shell section pathway-callout"><div><h2>Bring one recent question.</h2><p>It helps the tutor see what the learner understands and where another explanation could help.</p></div>{button("Discuss this curriculum",href)}</section>',button("Book a Free Demo",href))

exam_options = [
    ("School exams", "Review current topics and prepare for class tests with a manageable checklist.", "School course"),
    ("GCSE & IGCSE", "Use the correct exam board, topic priorities and question styles to guide revision.", "British exams"),
    ("AS & A Level", "Practise multi-step questions, deeper explanations and subject-specific reasoning.", "British exams"),
    ("SAT & ACT", "Discuss the skills and exact test you are preparing for, with a target date.", "US tests"),
    ("AP subjects", "Bring the course name and recent questions to discuss subject support.", "US courses"),
    ("11+ & 13+", "Share the target school's requirements and the subjects being assessed.", "Entrance"),
    ("Matric & FSc", "Review the board syllabus and practise organised solutions and explanations.", "School course"),
    ("School placement", "Discuss the assessment, school transition and topics you want to review.", "Entrance"),
]
exam_cards="".join(f'<article class="exam-card tilt reveal"><span class="card-kicker">{tag}</span><span class="clay-icon {tone}">{icon(glyph)}</span><h3>{name}</h3><p>{desc}</p>{button("Discuss preparation", "/book-a-demo/?"+urlencode({"curriculum":name,"goal":"Exam preparation"}), "secondary","diagonal")}</article>' for (name,desc,tag),tone,glyph in zip(exam_options,["blue","mint","violet","yellow","blue","peach","mint","violet"],["calendar","book","chart","language","science","puzzle","book","calendar"]))
extra_page("/test-prep/","Prepare with a clear focus.","EXAMS & ASSESSMENTS",
           "Choose the assessment, identify the gaps and make each practice session count.",
           f'<section class="shell section"><div class="exam-grid">{exam_cards}</div><p class="section-footnote">Share the exact exam, course and target date so admissions can check tutor availability.</p></section><section class="band"><div class="shell section">{section_head("A PRACTICE CYCLE","Review. Practise. Return.")}{tiles([("Find the gap","Start with a recent answer and locate the first step that needs attention."),("Practise the skill","Use a guided example, then attempt a related question independently."),("Return and review","Revisit the idea and use the result to choose the next priority.")])}</div></section>'+cta())

level_cards="".join(f'<article class="level-card tilt reveal"><span class="level-index">0{i}</span><span class="card-kicker">{level}</span><h3>{title}</h3><p>{desc}</p><a class="text-link" href="/book-a-demo/?{urlencode({"level":level})}">Discuss this level {icon("diagonal")}</a></article>' for i,(level,title,desc) in enumerate(LEVELS,1))
extra_page("/learning-levels/","A plan for every school stage.","LEARNING LEVELS",
           "From the first foundations to more advanced school subjects, start with what the learner needs next.",
           f'<section class="shell section"><div class="level-grid">{level_cards}</div><p class="section-footnote">School-year and grade equivalents vary. We use your school course and current level when discussing a plan.</p></section>'+cta())

market_options="".join(f'<option value="{slug}">{name}</option>' for slug,name,*_ in COUNTRIES)
plan_cards="".join(f'<article class="plan-card tilt reveal{(" recommended" if i==1 else "")}"><span class="card-kicker">{subtitle}</span><h2>{name}</h2><p class="plan-frequency">{frequency}</p><p class="plan-price">Personal quote<span>For your subject, level and schedule</span></p><ul>{"".join(f"<li>{icon("check")}{point}</li>" for point in points)}</ul><a class="btn {("primary" if i==1 else "secondary")}" data-plan-link data-plan="{name}" href="/book-a-demo/?{urlencode({"plan":name})}">Discuss this plan {icon("arrow")}</a></article>' for i,(name,subtitle,frequency,points) in enumerate(PLANS))
extra_page("/pricing/","A lesson plan that fits.","PLANS & PRICING",
           "Explore a regular lesson rhythm or build a package around several subjects and a specific goal.",
           f'<section class="shell section"><div class="pricing-toolbar"><div><h2>Choose a starting point.</h2><p>Final fees and lesson details are confirmed with your quote.</p></div><label>Your location<select data-pricing-country><option value="">Choose a country</option>{market_options}</select></label></div><div class="plan-grid">{plan_cards}</div></section><section class="shell section package-banner"><div><span class="eyebrow"><i></i>FLEXIBLE PLANNING</span><h2>More than one subject?</h2><p>Combine your priorities in a custom package enquiry.</p></div>{button("Build a custom package","/custom-package/")}</section>'+cta())

subject_boxes="".join(f'<label class="subject-choice"><input type="checkbox" name="subjects" value="{name}" data-course="{slug}"><span>{name}</span></label>' for slug,name,*rest in SUBJECTS)
custom=f'''<section class="shell section"><div class="package-layout">
<form id="package-planner" class="package-form"><span class="eyebrow"><i></i>YOUR LEARNING PLAN</span><h2>Choose your focus.</h2><p>Start with the subjects and times that matter to your family.</p>
<fieldset><legend>Subjects to discuss</legend><div class="subject-choices">{subject_boxes}</div></fieldset>
<div class="field-grid"><label>School stage<select name="stage"><option value="">To discuss</option>{"".join(f"<option>{name}</option>" for name,*_ in LEVELS)}</select></label>
<label>Lesson rhythm<select name="frequency"><option>To discuss</option><option>Once a week</option><option>Twice a week</option><option>Three times a week</option><option>Flexible</option></select></label>
<label class="field-wide">Your main goal<input name="goal" maxlength="180" placeholder="e.g. revise science and build maths confidence"></label>
<label class="field-wide">Preferred days and times<input name="schedule" maxlength="120" placeholder="e.g. Mondays and Thursdays after 5 pm, UK time"></label></div>
<button class="btn primary" type="submit">Preview my package {icon("arrow")}</button><noscript><p><a href="/book-a-demo/?plan=Custom+package">Discuss a custom package</a></p></noscript></form>
<aside class="package-summary"><span class="card-kicker">YOUR STARTING POINT</span><h2>A package around you.</h2><dl id="package-summary"><dt>Subjects</dt><dd>Choose one or several</dd><dt>Schedule</dt><dd>To discuss</dd></dl><p>Share this starting point in the demo enquiry. Lesson details and fees are agreed after discussing your needs.</p><a class="btn secondary" id="package-link" href="/book-a-demo/?plan=Custom+package">Continue to demo enquiry {icon("arrow")}</a><p class="small-copy" id="package-feedback" role="status"></p></aside>
</div></section>'''
extra_page("/custom-package/","Build your learning plan.","CUSTOM PACKAGES",
           "One subject or several, regular support or an exam focus. Put your priorities together here.",custom)

resource_cards="".join(f'<article class="resource-card tilt reveal"><img src="/assets/pages/free-notes-{slug}.svg" alt="" width="480" height="360" loading="lazy"><div class="resource-copy"><span class="card-kicker">{subject} · {level}</span><h3>{title}</h3><p>Core ideas, a worked example and three practice questions with answers.</p><div class="resource-actions"><a class="text-link" href="/free-notes/{slug}/">Read guide {icon("arrow")}</a><a href="/assets/notes/{slug}.pdf" target="_blank" rel="noopener">Read PDF <span class="sr-only">{title}</span></a><a href="/assets/notes/{slug}.pdf" download>Download <span class="sr-only">{title}</span>{icon("diagonal")}</a></div></div></article>' for slug,title,subject,level,*_ in NOTES)
extra_page("/free-notes/","Make a little room for practice.","FREE NOTES",
           "Twelve original topic guides. Read online, open the PDF or download a copy for later.",
           f'<section class="shell section" data-catalog>{catalog_filter("Find a subject or topic","Try chemistry, fractions or English")}<div class="resource-grid">{resource_cards}</div><p class="catalog-empty" hidden>No matching guides. Try another subject or topic.</p></section>')
for slug,title,subject,level,intro,points,example,questions in NOTES:
    points_html="".join(f"<li>{escape(point)}</li>" for point in points)
    practice="".join(f'<details class="practice-question"><summary>{i}. {escape(q)}{icon("plus")}</summary><p>{escape(answer)}</p></details>' for i,(q,answer) in enumerate(questions,1))
    body=f'<section class="shell section reader-layout"><article class="reading-panel"><span class="card-kicker">{subject} · {level}</span><h2>Core ideas</h2><ol class="reading-points">{points_html}</ol><div class="worked-example"><span class="card-kicker">WORKED EXAMPLE</span><p>{escape(example)}</p></div><h2>Try it yourself</h2><p>Attempt each question before opening the answer.</p><div class="practice-list">{practice}</div></article><aside class="reader-tools"><h2>Keep a copy.</h2><p>A one-page topic starter with the same example and practice questions.</p><a class="btn primary" href="/assets/notes/{slug}.pdf" download>Download PDF {icon("arrow")}</a><a class="text-link" href="/assets/notes/{slug}.pdf" target="_blank" rel="noopener">Open PDF in a new tab {icon("diagonal")}</a><a class="text-link" href="/free-notes/">Browse all notes {icon("arrow")}</a></aside></section>'
    extra_page(f"/free-notes/{slug}/",title,"FREE TOPIC GUIDE",intro,body)

article_cards="".join(image_card(f"/journal/{slug}/",title,intro,"Read article",category) for slug,title,category,intro,_ in ARTICLES)
extra_page("/journal/","Ideas for better study days.","BLOGS & ARTICLES",
           "Practical reading for students and parents, from planning a study week to reviewing exam practice.",
           f'<section class="shell section" data-catalog>{catalog_filter("Find an article","Try study planning, parents or exams")}<div class="story-grid">{article_cards}</div><p class="catalog-empty" hidden>No articles match. Try another word.</p></section>')
for slug,title,category,intro,sections in ARTICLES:
    sections_html="".join(f'<section id="part-{i}"><span class="chapter-number">0{i}</span><h2>{heading}</h2><p>{body}</p></section>' for i,(heading,body) in enumerate(sections,1))
    contents="".join(f'<a href="#part-{i}">{heading}</a>' for i,(heading,_) in enumerate(sections,1))
    body=f'<section class="shell section reader-layout"><article class="article-body">{sections_html}<div class="article-next"><h2>Turn an idea into practice.</h2><p>Choose a free topic guide and try the questions.</p>{button("Explore free notes","/free-notes/","secondary")}</div></article><aside class="reader-tools"><span class="card-kicker">{category}</span><h2>In this article</h2><nav aria-label="Article contents" class="contents-links">{contents}</nav><a class="text-link" href="/journal/">More articles {icon("arrow")}</a></aside></section>'
    extra_page(f"/journal/{slug}/",title,category.upper(),intro,body)

extra_page("/progress/","See the next step in learning.","LEARNING & PROGRESS",
           "Use clear learning goals and specific feedback to understand what is improving and what needs practice.",
           f'<section class="shell section two-col"><div>{section_head("ILLUSTRATIVE EVALUATION","A useful update is specific.","This example shows how specific feedback can describe a learner’s next step.")}<a class="text-link" href="/parents/">Parent resources {icon("arrow")}</a></div>{progress()}</section><section class="band"><div class="shell section">{tiles([("Understanding","Can the learner explain the idea in their own words and connect it to a familiar example?"),("Independence","Can the learner choose a method and attempt a related task with less guidance?"),("Application","Can the learner use the idea in a new situation and explain the reasoning?")])}</div></section>'+cta())


(DIST / ".nojekyll").touch()
(DIST / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
(DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f"<url><loc>{ORIGIN}{path}</loc></url>" for path in PAGES if not path.startswith("/portal"))+"</urlset>", encoding="utf-8")
print(f"Generated {len(PAGES)} pages.")
