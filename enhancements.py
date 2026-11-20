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
def review_cards(limit=None):
    if not REVIEWS:return '<div class="feedback-invitation"><div><span class="card-kicker">PARENT VOICES</span><h3>Every learning journey is personal.</h3><p>Family feedback and progress stories will appear here with permission. No parent reviews have been published yet.</p></div><a class="btn secondary" href="/reviews/">About family feedback</a></div>'
    return '<div class="review-grid">'+''.join(f'<figure class="review-card info-card"><blockquote>{e(r["quote"])}</blockquote><figcaption><strong>{e(r["display_name"])}</strong><span>{e(r["context"])}</span></figcaption></figure>' for r in REVIEWS[:limit])+'</div>'
def home_sections():
    return '''<section class="shell section lesson-teaser reveal"><div class="lesson-teaser-art" aria-hidden="true"><div class="lesson-orb">¼</div><div class="lesson-mini-note">Explain.<br>Try.<br>Understand.</div><span class="lesson-spark">✦</span></div><div><span class="eyebrow">A LITTLE LEARNING, RIGHT HERE</span><h2>Curiosity starts with a question.</h2><p>Try a short maths or science activity. Explore an idea, answer a question and see the reasoning behind it.</p><a class="btn primary" href="/try-a-lesson/">Try a mini lesson</a><span class="small-copy">No sign-up. No personal details.</span></div></section><section class="band"><div class="shell section"><div class="section-heading-row"><div class="section-head"><span class="eyebrow">THE PEOPLE BEHIND THE LESSON</span><h2>A good fit comes first.</h2><p>Start with the subject, the school course and the way your child learns.</p></div><a class="text-link" href="/tutors/">Explore tutor matching</a></div>'''+tutor_cards()+'''</div></section><section class="shell section family-feedback"><div class="section-head"><span class="eyebrow">LEARNING, THROUGH A FAMILY’S EYES</span><h2>Small steps. Meaningful progress.</h2></div>'''+review_cards(3)+'</section>'
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
    if path=='/':body=body.replace('<section class="shell section faq-grid home-faq">',home_sections()+'<section class="shell section faq-grid home-faq">')
    if path=='/pricing/':body=body.replace('<section class="shell section package-banner">',pricing_details()+'<section class="shell section package-banner">')
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
