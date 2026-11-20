"""Illustrative four-week prices, adapted from the user-supplied ProTutors reference."""
import json
from html import escape as e
from urllib.parse import urlencode
from enhancements import CONFIG

COUNTS=[4,8,12]
NAMES=['Weekly support','Progress plan','Exam focus']
DESCRIPTIONS=['A regular space to revisit concepts and practise one main subject.','More room for explanation, independent practice and a follow-up.','A focused block for a specific subject, topic list or exam goal.']

def initial_market():return next(m for m in CONFIG['sample_pricing']['markets'] if m['currency']==CONFIG['sample_pricing']['default_currency'])
def money(value,code):return ('£' if code=='GBP' else code+' ')+str(value)

def pricing_preview():
    market=initial_market()
    cards=''.join(f'<a class="pricing-preview-card info-card tilt" href="/pricing/#sample-plans"><span class="card-kicker">{name}</span><h3>{count} lessons</h3><p><strong>{money(rate,market["currency"])}</strong> per lesson</p><span class="small-copy">Illustrative {market["currency"]} rate · four-week plan</span></a>' for name,count,rate in zip(NAMES,COUNTS,market['rates']))
    return '<section class="shell section pricing-preview"><div class="section-heading-row"><div class="section-head"><span class="eyebrow">A RHYTHM THAT WORKS FOR YOU</span><h2>A little support. Room to grow.</h2><p>Compare sample lesson plans, then discuss a personal quote.</p></div><a class="text-link" href="/pricing/">Explore plans & prices</a></div><div class="pricing-preview-grid">'+cards+'</div><p class="sample-disclaimer">Illustrative prices only. Actual fees, lesson length and availability are confirmed before booking.</p></section>'

def pricing_body():
    data=CONFIG['sample_pricing'];market=initial_market()
    options=''.join(f'<option value="{e(m["currency"],quote=True)}"{(" selected" if m["currency"]==market["currency"] else "")}>{e(m["country"])} · {m["currency"] if m["rates"] else "personal quote"}</option>' for m in data['markets'])
    cards=[]
    for i,(name,count,description,rate) in enumerate(zip(NAMES,COUNTS,DESCRIPTIONS,market['rates'])):
        href='/book-a-demo/?'+urlencode({'plan':name,'country':market['slug'],'goal':f'Illustrative plan: {count} lessons over four weeks. Please confirm actual fees and lesson duration.'})
        cards.append(f'''<article class="plan-card sample-plan-card tilt reveal{(" recommended" if i==1 else "")}" data-sample-card="{i}"><span class="card-kicker">{["A STEADY START","ROOM TO GROW","A FOCUSED PUSH"][i]}</span><h2>{name}</h2><div class="lesson-count"><strong>{count:02}</strong><span>lessons<br>over four weeks</span></div><p class="sample-plan-description">{description}</p><ul><li>{i+1} lesson{("s" if i else "")} each week</li><li>Live one-to-one learning</li><li>School-course and topic focus</li><li>Practice and next-step feedback</li></ul><div class="sample-price-block"><p class="sample-price" data-sample-rate>{money(rate,market['currency'])}</p><p class="sample-unit">per lesson · <span data-sample-currency-label>{market['currency']}</span> · sample rate</p><p class="sample-total"><strong data-sample-total>{money(rate*count,market['currency'])}</strong><span>sample four-week total</span></p></div><a class="btn {("primary" if i==1 else "secondary")}" data-sample-enquiry data-plan="{name}" href="{href}">Enquire about this plan</a></article>''')
    encoded=json.dumps(data,ensure_ascii=False).replace('<','\\u003c')
    body='''<section class="shell section sample-pricing" id="sample-plans" data-sample-pricing><div class="pricing-toolbar"><div><span class="eyebrow">FLEXIBLE LESSON PLANNING</span><h2>Choose your lesson rhythm.</h2><p>A regular check-in or a more focused block of practice.</p></div><label>Show sample prices for<select data-sample-market>'''+options+'''</select></label></div><div class="sample-price-notice"><span class="sample-notice-icon" aria-hidden="true">✦</span><div><strong>Illustrative pricing</strong><p>These are sample prices for planning. Actual rates, lesson length and tutor availability must be confirmed in your quote.</p></div></div><div class="plan-grid sample-plan-grid">'''+''.join(cards)+'''</div><p class="sample-disclaimer">Sample rates are independent examples, not currency conversions. The totals assume the stated number of lessons over four weeks. No payment or recurring charge is taken here.</p><p class="sample-market-status" data-sample-status role="status" aria-live="polite"></p><script type="application/json" data-sample-data>'''+encoded+'''</script><noscript><p>Sample GBP prices are shown. Enable JavaScript to change the example currency.</p></noscript></section>'''
    body+='''<section class="band"><div class="shell section pricing-clarity"><div class="section-head"><span class="eyebrow">BEFORE YOU DECIDE</span><h2>Know what your quote includes.</h2><p>Agree the practical details so your family knows what to expect.</p></div><div class="quote-checklist"><h3>A clear starting point.</h3><p>Confirm the subject, tutor, session length, teaching platform, local time, total fee and currency. Ask about cancellations, rescheduling and missed lessons before agreeing to a plan.</p><span class="small-copy">Sample prices are not a confirmed offer or a guarantee of a tutor’s availability.</span></div></div></section><section class="shell section package-banner"><div><span class="eyebrow">TAILORED AROUND YOU</span><h2>More than one subject?</h2><p>Bring your subjects, timetable and goals together in a custom package enquiry.</p></div><a class="btn primary" data-sample-custom href="/custom-package/">Build a custom package</a></section>'''
    return body
