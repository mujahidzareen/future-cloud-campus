"""Generate the crawlable, dependency-free FCC review site."""
import json
import os
import re
from html import escape
from pathlib import Path
from shutil import copytree
from content import SUBJECTS, QURAN, COUNTRIES, FAQ, STEPS

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "dist" / "assets"
if not ASSETS.is_dir():
    ASSETS = ROOT / "docs" / "assets"
DIST = Path(os.environ.get("FCC_OUTPUT", ASSETS.parent))
ORIGIN = os.environ.get("FCC_ORIGIN", "https://future-cloud-campus.greybow37.chatgpt.site").rstrip("/")
PAGES = []

if (DIST / "assets").resolve() != ASSETS.resolve():
    copytree(ASSETS, DIST / "assets", dirs_exist_ok=True)

def icon(name, extra=""):
    return f'<svg class="icon {extra}" aria-hidden="true"><use href="/assets/icons.svg#{name}"></use></svg>'

def button(text="Book a Free Demo", href="/book-a-demo/", variant="primary", glyph="arrow"):
    return f'<a class="btn {variant}" href="{href}">{text}{icon(glyph) if glyph else ""}</a>'

def brand():
    return '<a class="brand" href="/" aria-label="Future Cloud Campus home"><img src="/assets/fcc-symbol.png" width="54" height="54" alt=""><span>Future Cloud<span class="brand-accent"> Campus</span><small>ONE CAMPUS. ENDLESS LEARNING.</small></span></a>'

def nav(path):
    links = [("/subjects/", "Subjects"), ("/how-it-works/", "How It Works"), ("/countries/", "Countries"), ("/parents/", "For Parents")]
    items = "".join(f'<a href="{url}"{(" aria-current=page" if path == url else "")}>{label}</a>' for url, label in links)
    return f'''<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="shell nav">{brand()}
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-links" aria-label="Open menu">{icon("menu")}</button>
    <nav id="nav-links" class="nav-links" aria-label="Main navigation">{items}<a class="mobile-portal" href="/portal/">Portal</a></nav>
    <div class="nav-actions"><a class="portal-link" href="/portal/">{icon("lock")} Portal</a>{button("Free Demo")}</div></div></header>'''

def footer():
    return f'''<footer class="site-footer"><div class="shell footer-main"><div class="footer-brand">{brand()}<p>Live online learning for families across time zones.</p></div>
    <div><strong>Explore</strong><a href="/subjects/">Academic subjects</a><a href="/quran-education/">Quran Education</a><a href="/countries/">Countries &amp; curricula</a></div>
    <div><strong>Families</strong><a href="/how-it-works/">How it works</a><a href="/parents/">For parents</a><a href="/faq/">FAQs</a><a href="/portal/">Parent &amp; Teacher Portal</a></div>
    <div><strong>Campus</strong><a href="/about/">About FCC</a><a href="/contact/">Contact &amp; admissions</a><a href="/careers/">Careers</a></div></div>
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
    <link rel="stylesheet" href="/assets/site.css"><script defer src="/assets/site.js"></script>{structured_markup}
    </head><body>{nav(path)}<main id="main">{body}</main>{footer()}</body></html>'''
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

def hero_small(kicker, title, text, crumbs, actions="", tile="book", tone="violet"):
    return f'''<section class="inner-hero"><div class="shell">{breadcrumb(crumbs)}<div class="inner-hero-content"><div>
    <div class="eyebrow"><i></i>{kicker}</div><h1>{title}</h1><p>{text}</p>{f'<div class="hero-actions">{actions}</div>' if actions else ''}</div>
    <div class="inner-art" aria-hidden="true"><span class="orb-ring"></span><span class="orb-ring ring2"></span><span class="orbit-dot"></span><div class="clay-icon {tone}">{icon(tile)}</div></div>
    </div></div></section>'''

def cards():
    return '<div class="subject-grid">' + ''.join(f'''<a class="subject-card tilt reveal" href="/{slug}/">
    <span class="clay-icon {color}">{icon(glyph)}</span><h3>{name}</h3><p>{tag}</p><span class="card-arrow">{icon("diagonal")}<span class="sr-only">Explore {name}</span></span></a>'''
    for slug, name, glyph, color, tag, *_ in SUBJECTS) + '</div>'

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
    return '<div class="info-grid">' + ''.join(f'<article class="info-card reveal"><span class="tile-number">{i:02}</span><h3>{h}</h3><p>{p}</p></article>' for i,(h,p) in enumerate(items,1)) + '</div>'

def home():
    symbol = '<img src="/assets/fcc-symbol.png" alt="" width="54" height="54">'
    logo_edge = "".join(f'<span class="logo-edge" style="--depth:{depth}px"></span>' for depth in range(-13, 14))
    return f"""
    <section class="hero"><div class="shell hero-grid">
      <div class="hero-copy">
        <div class="hero-tag"><span>{icon("star")}</span> LIVE ONLINE TUTORING</div>
        <h1>Learning that<br><em>fits your child.</em></h1>
        <p>One-to-one lessons that build confidence in school subjects, at your child’s pace.</p>
        <div class="hero-actions">{button()}{button("Explore Subjects","/subjects/","secondary","diagonal")}</div>
      </div>
      <div class="hero-art tilt" data-hero>
        <button class="motion-control" type="button" data-motion aria-pressed="false" hidden>Pause animation</button>
        <div class="art-visual" aria-hidden="true">
          <div class="art-index"><span></span> FUTURE CLOUD CAMPUS</div>
          <div class="art-grid"></div><div class="art-orbit orbit1"></div><div class="art-orbit orbit2"></div>
          <div class="scene">
            <div class="logo-platform"></div>
            <div class="logo-float"><div class="logo-spinner">
              {logo_edge}
              <span class="logo-face logo-front">{symbol}</span>
              <span class="logo-face logo-back">{symbol}</span>
            </div></div>
            <div class="float-tile art-math"><span>÷</span><span>×</span><span>+</span><span>=</span></div>
            <div class="float-tile art-code">{icon("code")}</div>
            <div class="float-tile art-science">{icon("science")}</div>
            <span class="spark spark-a">✦</span><span class="spark spark-b">✧</span><span class="planet planet-a"></span>
          </div>
          <span class="art-caption">ONE CAMPUS <i></i> ENDLESS LEARNING</span>
        </div>
      </div>
    </div></section>
    <section class="trust shell" aria-label="What families can expect">
      <div>{icon("people")}<strong>Live 1-to-1 lessons</strong></div>
      <div>{icon("clock")}<strong>Flexible scheduling</strong></div>
      <div>{icon("chart")}<strong>Clear progress goals</strong></div>
      <div>{icon("globe")}<strong>Learn from anywhere</strong></div>
    </section>
    <section class="shell section" id="subjects"><div class="section-heading-row">{section_head("ACADEMIC TUTORING","Explore our subjects.")}<a class="text-link" href="/subjects/">All subjects {icon("arrow")}</a></div>{cards()}</section>
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
    <section class="shell section regional-strip">{section_head("LOCAL CURRICULUM SUPPORT","Find your curriculum.")}<div class="region-links">{''.join(f'<a class="region-pill tilt" href="/{slug}/"><span aria-hidden="true">{flag}</span>{name}{icon("diagonal")}</a>' for slug,name,flag,*_ in COUNTRIES)}</div></section>
    <section class="shell section faq-grid home-faq"><div>{section_head("GOOD TO KNOW","Questions families ask.")}<a class="text-link" href="/faq/">All questions {icon("arrow")}</a></div>{accordions(FAQ[:3])}</section>
    {cta()}"""

page("/", "Future Cloud Campus | Online Tutoring & Quran Education", "Live one-to-one online tutoring and Quran Education for families. Explore academic subjects and find the right starting point with a free demo.", home())

crumbs = [("Home","/"),("Subjects","/subjects/")]
page("/subjects/","Academic subjects","Explore one-to-one Mathematics, English, Science, Computer & IT and Logical Reasoning lessons.",hero_small("ACADEMIC TUTORING","Five subjects. A plan for each learner.","Explore the subject library and find the right starting point for your child.",crumbs,button())+f'<section class="shell section">{cards()}</section>'+cta(),crumbs)

for slug,name,glyph,tone,tag,desc,topics,audience,faq in SUBJECTS:
    path=f"/{slug}/"
    crumbs=[("Home","/"),("Subjects","/subjects/"),(name,path)]
    page(path,name+" tutoring",desc,hero_small("LIVE ACADEMIC TUTORING",name,desc,crumbs,button(href=f"/book-a-demo/?course={slug}"),glyph,tone)+
        f'<section class="shell section">{section_head("WHAT STUDENTS LEARN",tag)}{tiles(topics)}</section><section class="band"><div class="shell section two-col">{section_head("WHO IT’S FOR","Start with the learner.",audience)}{tiles([("One-to-one lessons","The tutor explains a concept, guides a practice task and checks understanding. Discuss lesson length and platform during the demo."),("Assessment and progress","The first session helps identify the starting level. Goals and periodic evaluations guide the next lessons.")])}</div></section><section class="shell section faq-grid">{section_head("QUESTIONS",f"About {name} tutoring")}{accordions([faq, FAQ[0]])}</section>'+cta(slug),crumbs)

crumbs=[("Home","/"),("Quran Education","/quran-education/")]
quran_cards=''.join(f'<a class="subject-card quran-subject tilt reveal" href="/{slug}/"><span class="clay-icon mint">{icon("book")}</span><h3>{name}</h3><p>{desc}</p><span class="card-arrow">{icon("diagonal")}</span></a>' for slug,name,desc,_ in QURAN)
page("/quran-education/","Quran Education","Explore live Quran Reading, Noorani Qaida, Tajweed and Islamic Studies at Future Cloud Campus.",
    f'<section class="inner-hero quran-inner"><div class="shell">{breadcrumb(crumbs)}<div class="inner-hero-content"><div><div class="eyebrow"><i></i>DEDICATED LEARNING PATH</div><h1>Quran Education</h1><p>One-to-one learning with a clear starting level, guided practice and progress updates for families.</p><div class="hero-actions">{button(href="/book-a-demo/?course=quran-education",variant="light")}</div></div><img src="/assets/quran.svg" alt="" width="500" height="350"></div></div></section>'
    +f'<section class="shell section">{section_head("COURSES","Find a starting point.")}<div class="subject-grid quran-grid">{quran_cards}</div></section><section class="band"><div class="shell section">{section_head("THE LEARNING APPROACH","Assessment, practice and review.")}{tiles([("Initial placement","Discuss age, prior reading and preferred times. The teacher can check letter recognition or listen to a short reading sample."),("Teacher match","Ask admissions about teacher fit, the selection process and gender matching availability for your schedule."),("Progress feedback","Review the previous lesson, fluency and Tajweed. The evaluation can record strengths, practice areas and the recommended pace.")])}</div></section>'+cta("quran-education"),crumbs)
for slug,name,desc,outcomes in QURAN:
    path=f"/{slug}/"
    crumbs=[("Home","/"),("Quran Education","/quran-education/"),(name,path)]
    page(path,name,desc,hero_small("QURAN EDUCATION",name,desc,crumbs,button(href=f"/book-a-demo/?course={slug}"),"book","mint")+
        f'<section class="shell section">{section_head("INSIDE THE LESSON","Learn at an appropriate pace.")}{tiles([("What we practise",outcomes),("Who it’s for","Share the learner’s age and previous experience. The initial assessment helps place the learner at a suitable level."),("How we review progress","The teacher checks the previous lesson, offers feedback and identifies a realistic focus for the next class.")])}</section><section class="shell section faq-grid">{section_head("QUESTIONS","Scheduling and assessment")}{accordions([FAQ[0],FAQ[2]])}</section>'+cta(slug),crumbs)

crumbs=[("Home","/"),("Countries & curricula","/countries/")]
page("/countries/","Countries & curricula","Find curriculum and time zone guidance for families in the United Kingdom, United States and Canada.",hero_small("GLOBAL LEARNING","Find guidance for your country.","Share the school curriculum, current topics and local time zone so we can discuss the right support.",crumbs,tile="globe")+f'<section class="shell section">{country_picker()}</section>'+cta(),crumbs)
for slug,name,flag,heading,desc,time in COUNTRIES:
    path=f"/{slug}/"
    crumbs=[("Home","/"),("Countries","/countries/"),(name,path)]
    page(path,f"Online tutoring in {name}",desc,hero_small("COUNTRY & CURRICULUM",f"Online tutoring in {name}",desc,crumbs,button(href=f"/book-a-demo/?country={slug}"),"globe")+
        f'<section class="shell section">{section_head("PLAN YOUR LESSONS",heading)}{tiles([("Before the demo",desc),("Scheduling",time),("Available subjects","Explore Mathematics, English, Science, Computer & IT, Logical Reasoning and Quran Education.")])}</section><section class="shell section">{cards()}</section>'+cta(),crumbs)

crumbs=[("Home","/"),("How it works","/how-it-works/")]
page("/how-it-works/","How it works","Learn how tutor matching, a free demo and a personalised learning plan fit together.",hero_small("THE LEARNING JOURNEY","Start with one conversation.","Tell us what’s going well, where your child is getting stuck and what you’d like to achieve.",crumbs,button(),"calendar")+f'<section class="shell section">{timeline()}</section><section class="band"><div class="shell section faq-grid">{section_head("PLANNING YOUR FIRST LESSON","Questions before you start.")}{accordions(FAQ)}</div></section>'+cta(),crumbs)

crumbs=[("Home","/"),("For Parents","/parents/")]
page("/parents/","For parents","See how Future Cloud Campus uses learning goals and progress evaluations to guide the next lesson.",hero_small("FOR FAMILIES","Stay close to your child’s learning.","Follow the learning plan and use tutor feedback to see what needs practice next.",crumbs,button("See what’s coming to the Parent Portal","/portal/parent/","secondary"),"chart")+f'<section class="shell section two-col">{section_head("EXAMPLE EVALUATION","What a progress update can tell you.","This example shows how a tutor can translate lesson observations into a practical next step.")}{progress()}</section><section class="band"><div class="shell section">{section_head("PARENT RESOURCES","Before and between lessons.")}{tiles([("Before the demo","Have a recent school topic or a question in mind. Consider what would make the next few weeks of learning feel successful."),("Between lessons","Ask the tutor for a short practice activity and give your child time to explain how they approached it."),("At a progress review","Look for the current goal, an example of progress, and the focus for the next lesson.")])}</div></section>'+cta(),crumbs)

crumbs=[("Home","/"),("FAQs","/faq/")]
page("/faq/","FAQs","Answers about live lessons, tutor matching, progress and preparing for a free demo.",hero_small("FAMILY FAQ","Questions families ask.","Find out what to prepare and how online lessons are designed.",crumbs,tile="language")+f'<section class="shell section faq-grid">{section_head("COMMON QUESTIONS","Before your first lesson.")}{accordions(FAQ)}</section>'+cta(),crumbs)

crumbs=[("Home","/"),("About","/about/")]
page("/about/","About Future Cloud Campus","Learn about Future Cloud Campus and its one-to-one academic tutoring and Quran Education.",hero_small("OUR CAMPUS","One campus. Endless learning.","Future Cloud Campus brings live one-to-one academic tutoring and Quran Education together in a single learning experience for families.",crumbs,button(),"globe")+f'<section class="shell section">{section_head("OUR APPROACH","A lesson built around the learner.")}{tiles([("Start with the right level","A short assessment and a conversation about the learner’s goals help set the starting point."),("Practise with guidance","The tutor adapts the activity and pace based on how the learner responds."),("Review progress","Use lesson observations and periodic evaluations to agree on the next area to practise.")])}</section>',crumbs)

for slug, name, desc, details, glyph in [
    ("contact","Contact & admissions","Tell admissions which programme, level and time zone you’re interested in.","This website preview uses a sample booking flow. Admissions contact details and live demo requests will be available once Future Cloud Campus connects its admissions service.","language"),
    ("careers","Careers","Teach live online with a focus on individual learning goals and clear feedback.","Open roles and a secure application form can be published here once the hiring team confirms its recruitment details.","people"),
]:
    path=f"/{slug}/"
    crumbs=[("Home","/"),(name,path)]
    page(path,name,desc,hero_small("FUTURE CLOUD CAMPUS",name,desc,crumbs,button("Preview the demo form",variant="secondary") if slug=="contact" else "",glyph)+f'<section class="shell section"><div class="notice">{icon("language")}<p>{details}</p></div></section>',crumbs)

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
    ("uk","United Kingdom","+44"),("usa","United States","+1"),("canada","Canada","+1"),("ireland","Ireland","+353"),("australia","Australia","+61"),("new-zealand","New Zealand","+64"),("pakistan","Pakistan","+92"),("other","Other","")])
form=f'''<section class="form-band"><div class="shell">{breadcrumb(crumbs)}<div class="form-layout">
  <div class="form-intro"><div class="eyebrow"><i></i>ADMISSIONS</div><h1>Book a Free Demo</h1><p>Tell us what your child would like to learn and when your family is available.</p>
  <div class="form-guide"><span class="clay-icon violet">{icon("calendar")}</span><div><h2>What happens next?</h2><p>In the live booking process, admissions will review the request, discuss tutor availability and confirm a demo time with you.</p></div></div>
  <div class="notice">{icon("lock")}<p><strong>Preview only.</strong> Use sample details. The form previews the request on this page and sends nothing to admissions.</p></div>
  </div>
  <form class="demo-form" id="demo-form" autocomplete="off" method="dialog" data-preview>
    <h2>Demo request</h2><p class="form-hint">Fields marked with * are required.</p>
    <div class="field-grid">
      <label>Parent or guardian name *<input name="name" required maxlength="100" placeholder="Sample Parent"></label>
      <label>Email *<input name="email" type="email" required maxlength="160" placeholder="parent@example.com"></label>
      <label>Country *<select name="country" required><option value="">Select country</option>{country_options}</select></label>
      <label>Time zone *<select name="timezone" required><option value="">Select time zone</option><option value="Europe/London">UK · London</option><option value="Europe/Dublin">Ireland · Dublin</option><option value="America/New_York">US · Eastern</option><option value="America/Chicago">US · Central</option><option value="America/Denver">US · Mountain</option><option value="America/Los_Angeles">US · Pacific</option><option value="America/Anchorage">US · Alaska</option><option value="Pacific/Honolulu">US · Hawaii</option><option value="America/Toronto">Canada · Eastern</option><option value="America/Vancouver">Canada · Pacific</option><option value="America/Edmonton">Canada · Mountain</option><option value="America/Winnipeg">Canada · Central</option><option value="America/Halifax">Canada · Atlantic</option><option value="America/St_Johns">Canada · Newfoundland</option><option value="Australia/Sydney">Australia · Sydney</option><option value="Australia/Perth">Australia · Perth</option><option value="Pacific/Auckland">New Zealand · Auckland</option><option value="Asia/Karachi">Pakistan · Karachi</option><option value="other">Other / discuss availability</option></select></label>
      <div class="phone-field"><label>Country code *<select name="code" required><option value="">Code</option><option>+44</option><option>+1</option><option>+353</option><option>+61</option><option>+64</option><option>+92</option><option value="other">Other</option></select></label><label>WhatsApp / phone *<input name="phone" type="tel" required maxlength="22" minlength="7" pattern="[+0-9 \\(\\)\\-]{{7,22}}" title="Enter a phone number using digits, spaces, parentheses, plus or hyphen." placeholder="7700 900000"></label></div>
      <label>Age, year or grade *<input name="level" required maxlength="50" placeholder="e.g. Year 8"></label>
      <label>Subject or course *<select name="course" required><option value="">Select a subject</option>{options}</select></label>
      <label>Preferred days and time<input name="time" maxlength="100" placeholder="e.g. Tuesday after 5 pm"></label>
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
    art = f"""<div class="launch-art tilt" aria-hidden="true">
      <div class="launch-halo"></div><div class="launch-orbit launch-orbit-one"></div><div class="launch-orbit launch-orbit-two"></div>
      <div class="launch-shadow"></div><div class="launch-core">{icon("lock")}</div>
      <span class="launch-float launch-calendar">{icon("calendar")}</span>
      <span class="launch-float launch-progress">{icon("chart")}</span>
      <span class="launch-float launch-book">{icon("book")}</span>
      <span class="launch-spark launch-spark-one">✦</span><span class="launch-spark launch-spark-two">✧</span>
    </div>"""
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
            f'<article class="info-card reveal"><span class="clay-icon {tone}">{icon(glyph)}</span><h3>{name}</h3><p>{desc}</p></article>'
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

(DIST / ".nojekyll").touch()
(DIST / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
(DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f"<url><loc>{ORIGIN}{path}</loc></url>" for path in PAGES if not path.startswith("/portal"))+"</urlset>", encoding="utf-8")
print(f"Generated {len(PAGES)} pages.")
