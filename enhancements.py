"""Reusable presentation and business-content components for FCC."""
import json, re
from html import escape as e
from pathlib import Path
from urllib.parse import urlparse
CONFIG=json.loads((Path(__file__).parent/'site_content.json').read_text())
A=CONFIG['admissions']
def https(value):
    p=urlparse(value);return p.scheme=='https' and bool(p.netloc) and not p.username and not p.password
LIVE=bool(https(A['endpoint']) and re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',A['email']) and A['privacy_reviewed'] and A['provider_name'] and https(A['provider_privacy_url']))
TUTORS=[t for t in CONFIG['tutors'] if t.get('approved') is True and t.get('photo_consent') is True and all(t.get(k) for k in ['name','bio','qualification','photo','subjects','curricula'])]
REVIEWS=[r for r in CONFIG['reviews'] if r.get('approved') is True and r.get('publication_consent') is True and all(r.get(k) for k in ['quote','display_name','context'])]
def safe_media(s):return s if isinstance(s,str) and s.startswith('/assets/') and '..' not in s else ''
def tutor_cards():
    cards=[]
    for t in TUTORS:
        photo=safe_media(t['photo']);video=safe_media(t.get('video',''))
        if not photo:continue
        intro=f'<details class="tutor-video"><summary>Watch introduction</summary><video controls preload="none" poster="{e(photo,quote=True)}"><source src="{e(video,quote=True)}" type="video/mp4"></video></details>' if video else ''
        cards.append(f'<article class="tutor-card info-card tilt reveal"><img class="tutor-photo" src="{e(photo,quote=True)}" alt="{e(t["name"],quote=True)}" width="480" height="400" loading="lazy"><div class="tutor-copy"><span class="card-kicker">{e(t["qualification"])}</span><h3>{e(t["name"])}</h3><p>{e(t["bio"])}</p><dl><dt>Subjects</dt><dd>{e(", ".join(t["subjects"]))}</dd><dt>Curricula</dt><dd>{e(", ".join(t["curricula"]))}</dd></dl>{intro}<a class="btn secondary" href="/book-a-demo/">Discuss a tutor match</a></div></article>')
    return '<div class="tutor-grid">'+''.join(cards)+'</div>' if cards else '<div class="content-pending"><span class="clay-icon blue" aria-hidden="true">✦</span><div><h3>Personal introductions, coming soon.</h3><p>Published profiles will include the tutor’s photograph, qualifications and teaching focus. Discuss your subject and availability in the demo enquiry.</p></div><a class="btn secondary" href="/book-a-demo/">Find your starting point</a></div>'
_REVIEW_SEQUENCE=0

def review_carousel(cards, sample=False):
    global _REVIEW_SEQUENCE
    _REVIEW_SEQUENCE+=1
    track_id=f'parent-review-track-{_REVIEW_SEQUENCE}'
    label='Illustrative parent perspectives' if sample else 'Parent reviews'
    count_label='examples' if sample else 'reviews'
    return f'''<div class="review-carousel" data-review-carousel data-review-sample="{str(sample).lower()}" role="region" aria-roledescription="carousel" aria-label="{label}"><div class="review-carousel-toolbar"><p class="review-carousel-status" data-review-status role="status" aria-live="polite">{len(cards)} {count_label}</p><div class="review-carousel-controls" data-review-controls hidden><button class="btn secondary review-arrow" type="button" data-review-prev aria-label="Previous reviews" aria-controls="{track_id}" disabled><span aria-hidden="true">&lt;</span></button><button class="btn secondary review-arrow" type="button" data-review-next aria-label="Next reviews" aria-controls="{track_id}"><span aria-hidden="true">&gt;</span></button></div></div><div class="review-track review-grid" id="{track_id}" data-review-track tabindex="0" role="group" aria-label="Review cards. Use the left and right arrow keys to browse.">{''.join(cards)}</div><p class="review-carousel-hint">Swipe, scroll, or use the &lt; and &gt; buttons to explore.</p></div>'''

def review_cards(limit=None, full=False):
    if not REVIEWS:
        from campus_refresh import illustrative_reviews
        amount=6 if full or limit is None else min(limit,6)
        note='<div class="review-example-disclosure"><span class="review-disclosure-icon" aria-hidden="true">✦</span><p><strong>Illustrative review examples.</strong> These are review-style design examples, not verified FCC customer feedback. Photographs are editorial stock images.</p></div>'
        return note+review_carousel(illustrative_reviews(amount),True)
    cards=[]
    for r in REVIEWS[:limit]:
        picture=safe_media(r.get('photo','')) if r.get('photo_consent') is True else ''
        avatar=f'<img class="review-parent-photo" src="{e(picture,quote=True)}" alt="{e(r["display_name"],quote=True)}" width="48" height="48" loading="lazy">' if picture else '<span class="review-parent-initial" aria-hidden="true">'+e(r['display_name'][0].upper())+'</span>'
        cards.append(f'<figure class="review-card info-card tilt"><span class="review-quote-mark" aria-hidden="true">“</span><blockquote>{e(r["quote"])}</blockquote><figcaption>{avatar}<div><strong>{e(r["display_name"])}</strong><span>{e(r["context"])}</span></div></figcaption></figure>')
    return review_carousel(cards)

SOCIAL_CHANNELS=[('instagram','Instagram','#ad3b82'),('facebook','Facebook','#2460bb'),('linkedin','LinkedIn','#176ba1'),('youtube','YouTube','#c43636'),('tiktok','TikTok','#263b46'),('whatsapp','WhatsApp','#23785a')]
SOCIAL_HOSTS={'instagram':['instagram.com'],'facebook':['facebook.com','fb.com'],'linkedin':['linkedin.com'],'youtube':['youtube.com','youtu.be'],'tiktok':['tiktok.com'],'whatsapp':['wa.me','whatsapp.com']}
SOCIAL_SVGS={
 'instagram':'<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor" stroke="none"/>',
 'facebook':'<path d="M14 21v-8h3l.5-4H14V7c0-1.2.4-2 2-2h2V1.5A25 25 0 0 0 15 1c-3 0-5 1.8-5 5v3H7v4h3v8"/>',
 'linkedin':'<rect x="3" y="8" width="4" height="13" rx=".5"/><circle cx="5" cy="4" r="2"/><path d="M11 21V8h4v2c1-3 6-3 6 2v9h-4v-8c0-2-2-2-2 0v8Z"/>',
 'youtube':'<rect x="2" y="5" width="20" height="14" rx="4"/><path d="m10 9 5 3-5 3Z"/>',
 'tiktok':'<path d="M14 3v12a4 4 0 1 1-4-4M14 3c1 4 3 5 7 5M17 3c.4 1.7 1.9 3 4 3"/>',
 'whatsapp':'<path d="M21 11.5a9 9 0 0 1-13.4 7.9L3 21l1.4-4.6A9 9 0 1 1 21 11.5Z"/><path d="m8 7 2 2-1 1c1 2 2 3 4 4l1-1 2 2c-1 3-4 1-6-1S6 8 8 7Z"/>'}

def verified_social(key):
    record=CONFIG.get('socials',{}).get(key,{})
    url=record.get('url','');host=(urlparse(url).hostname or '').lower()
    return url if record.get('verified') is True and https(url) and any(host==h or host.endswith('.'+h) for h in SOCIAL_HOSTS[key]) else ''

def social_icons(compact=False):
    items=[]
    for key,label,color in SOCIAL_CHANNELS:
        url=verified_social(key)
        svg=f'<svg class="social-glyph" viewBox="0 0 24 24" aria-hidden="true">{SOCIAL_SVGS[key]}</svg>'
        content=svg+f'<span class="social-label">{label}</span>'
        if url: item=f'<a class="social-link" href="{e(url,quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="{label} (opens in a new tab)" style="--social-color:{color}">{content}</a>'
        else: item=f'<span class="social-link is-pending" role="img" aria-label="{label} link coming soon" title="{label} link coming soon" style="--social-color:{color}">{content}<span class="social-pending">Coming soon</span></span>'
        items.append('<li>'+item+'</li>')
    note='Official FCC links are being added.' if not any(verified_social(key) for key,_,_ in SOCIAL_CHANNELS) else 'Choose an official Future Cloud Campus channel.'
    return f'<div class="social-block{(" social-compact" if compact else "")}"><ul class="social-links" aria-label="Future Cloud Campus social channels">'+''.join(items)+f'</ul><p class="social-note">{note}</p></div>'

def social_section():
    return '<section class="shell section campus-social"><div class="section-head"><span class="eyebrow">BEYOND THE CLASSROOM</span><h2>Stay close to campus.</h2><p>Find our social channels for learning ideas, campus updates and ways to connect.</p></div>'+social_icons()+'</section>'

def home_sections():
    return '''<section class="shell section lesson-teaser reveal"><div class="lesson-teaser-art" aria-hidden="true"><div class="lesson-orb">¼</div><div class="lesson-mini-note">Explain.<br>Try.<br>Understand.</div><span class="lesson-spark">✦</span></div><div><span class="eyebrow">A LITTLE LEARNING, RIGHT HERE</span><h2>Curiosity starts with a question.</h2><p>Try a short maths or science activity. Explore an idea, answer a question and see the reasoning behind it.</p><a class="btn primary" href="/try-a-lesson/">Try a mini lesson</a><span class="small-copy">No sign-up. No personal details.</span></div></section><section class="band"><div class="shell section"><div class="section-heading-row"><div class="section-head"><span class="eyebrow">THE PEOPLE BEHIND THE LESSON</span><h2>A good fit comes first.</h2><p>Start with the subject, the school course and the way your child learns.</p></div><a class="text-link" href="/tutors/">Explore tutor matching</a></div>'''+tutor_cards()+'''</div></section><section class="shell section family-feedback"><div class="section-head"><span class="eyebrow">FAMILY PERSPECTIVES</span><h2>A space for family feedback.</h2></div>'''+review_cards(6)+'</section>'+social_section()
def lesson_body():
    return '''<section class="shell section lesson-layout"><aside class="lesson-intro"><span class="eyebrow">YOUR MINI CLASSROOM</span><h2>See the idea.<br>Make it click.</h2><p>Choose a topic, explore the explanation and try three short questions at your own pace.</p><p class="small-copy">An illustrative activity, not an assessment or a live tutoring session. Answers stay on this page.</p><a class="text-link" href="/free-notes/">Explore free topic guides</a></aside><div class="lesson-playground" data-lesson><div class="lesson-topic-bar" aria-label="Choose a lesson"><button type="button" class="country-btn" data-topic="maths" aria-pressed="true">Maths · Percentages</button><button type="button" class="country-btn" data-topic="science" aria-pressed="false">Science · Forces</button></div><div class="lesson-stage"><div class="lesson-diagram" data-lesson-diagram aria-hidden="true"></div><span class="card-kicker" data-lesson-kicker></span><h3 data-lesson-title></h3><p data-lesson-explanation></p></div><form data-lesson-form><fieldset><legend data-lesson-question></legend><div class="lesson-options" data-lesson-options></div></fieldset><button class="btn primary" type="submit">Check my answer</button><p class="lesson-feedback" data-lesson-feedback role="status" aria-live="polite"></p><div class="lesson-bottom"><span class="small-copy" data-lesson-count></span><button class="btn secondary" type="button" data-lesson-next hidden>Next question</button><button class="btn secondary" type="button" data-lesson-reset hidden>Start again</button></div></form><noscript><p>Enable JavaScript for this activity, or <a href="/free-notes/percentages/">read the percentages guide</a>.</p></noscript></div></section>'''
def pricing_details():
    names=['Weekly support','Progress plan','Exam focus']
    def row(title,values):return '<tr><th scope="row">'+title+'</th>'+''.join('<td>'+e(str(v))+'</td>' for v in values)+'</tr>'
    rows=row('Lesson rhythm',['Once a week','Twice a week','Agreed around your goal'])+row('Sessions over four weeks',['4 if held every week','8 if held every week','Confirmed in your plan'])+row('Learning focus',['One main topic or subject','Explanation and follow-up practice','Topic priorities and exam practice'])+row('Session length',[(str(CONFIG['plans'][n]['duration_minutes'])+' minutes') if CONFIG['plans'][n]['duration_minutes'] else 'Confirm in your quote' for n in names])+row('Fees',[CONFIG['plans'][n]['price'] or 'Personal quote' for n in names])
    return '<section class="shell section plan-details"><div class="section-head"><span class="eyebrow">KNOW WHAT YOU’RE CHOOSING</span><h2>A clearer conversation about lessons.</h2><p>Use these details to compare your options before agreeing on a plan.</p></div><div class="comparison-scroll" tabindex="0" role="region" aria-label="Lesson plan comparison"><table class="plan-comparison"><thead><tr><th scope="col">Detail</th>'+''.join('<th scope="col">'+n+'</th>' for n in names)+'</tr></thead><tbody>'+rows+'</tbody></table></div><div class="quote-checklist"><h3>Before you enrol</h3><p>Confirm the tutor, lesson length, platform, time zone, total fee and currency. Ask for the notice period for cancellations, rescheduling and missed lessons before agreeing to a plan.</p><span class="small-copy">The four-week examples show session counts, not a monthly billing promise. Fees and cancellation arrangements are confirmed individually.</span></div></section>'
def filters(notes):
    values=[('subject','Subject','All subjects',sorted({n[2] for n in notes})),('level','School stage','All stages',['Primary / Middle','Secondary']),('curriculum','Curriculum focus','All guides',['General foundations','GCSE / IGCSE'])]
    return '<div class="resource-filters">'+''.join(f'<label>{label}<select data-filter-{key}><option value="">{all_label}</option>'+''.join(f'<option value="{e(v,quote=True)}">{e(v)}</option>' for v in choices)+'</select></label>' for key,label,all_label,choices in values)+'<button class="btn secondary" type="button" data-clear-filters>Clear filters</button></div><p class="filter-help">These are topic starters. Check your school’s specification for exact course and exam requirements.</p>'
def enrich(path,body,notes,articles):
    if path=='/' and 'data-studio-home' not in body:body=body.replace('<section class="shell section faq-grid home-faq">',home_sections()+'<section class="shell section faq-grid home-faq">')
    if path.strip('/') in ['quran-education','quran-reading','noorani-qaida','tajweed','islamic-studies']:
        section='<section class="shell section family-feedback quran-reviews"><div class="section-head"><span class="eyebrow">FAMILY PERSPECTIVES</span><h2>Parent reviews.</h2><p>Feedback from families, published with their permission.</p></div>'+review_cards(3)+'</section>'
        body=body.replace('<section class="shell final-wrap',section+'<section class="shell final-wrap',1)

    if path=='/free-notes/':
        body=body.replace('<div class="resource-grid">',filters(notes)+'<div class="resource-grid">'); iterator=iter(notes)
        def attrs(m):
            n=next(iterator);stages=[]
            if 'primary' in n[3].lower() or 'middle' in n[3].lower():stages.append('Primary / Middle')
            if 'secondary' in n[3].lower() or 'gcse' in n[3].lower():stages.append('Secondary')
            level='|'.join(stages or ['Secondary']);curriculum='GCSE / IGCSE' if 'GCSE' in n[3] else 'General foundations'
            return f'<article data-subject="{e(n[2],quote=True)}" data-level="{level}" data-curriculum="{curriculum}" class="resource-card tilt reveal">'
        body=re.sub('<article class="resource-card tilt reveal">',attrs,body)
    if path.startswith('/journal/') and path!='/journal/':
        mapping={'first-online-lesson':['fractions','diffusion'],'choose-your-syllabus':['balancing-equations','forces-and-motion'],'review-exam-practice':['forces-and-motion','balancing-equations'],'retrieval-practice':['water-cycle','opportunity-cost']}
        selected=[n for n in notes if n[0] in mapping.get(path.strip('/').split('/')[-1],['percentages','averages'])]
        body+='<section class="shell section related-resources"><div class="section-head"><span class="eyebrow">PUT IT INTO PRACTICE</span><h2>Your next small step.</h2></div><div class="related-grid">'+''.join(f'<a class="info-card tilt" href="/free-notes/{n[0]}/"><span class="card-kicker">{e(n[2])}</span><h3>{e(n[1])}</h3><p>Read the idea. Try the questions.</p></a>' for n in selected[:2])+'</div></section>'
    return body
