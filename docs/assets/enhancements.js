'use strict';
// Topic filters combine search, subject, level and curriculum without another library.
document.querySelectorAll('[data-catalog]').forEach(catalog=>{
 const search=catalog.querySelector('[data-filter]'),selects=[...catalog.querySelectorAll('.resource-filters select')],cards=[...catalog.querySelectorAll('.subject-card,.resource-card,.story-card')];
 const filter=()=>{const words=search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);let count=0;cards.forEach(card=>{const text=card.textContent.toLowerCase();const match=words.every(w=>text.includes(w))&&selects.every(s=>{const key=Object.keys(s.dataset).find(k=>k.startsWith('filter')).slice(6).toLowerCase();return !s.value||(card.dataset[key]||'').split('|').includes(s.value);});card.hidden=!match;if(match){count++;card.classList.add('visible');}});catalog.querySelector('[data-result-count]').textContent=`${count} of ${cards.length} available`;catalog.querySelector('.catalog-empty').hidden=count!==0;};
 search.addEventListener('input',filter);selects.forEach(s=>s.addEventListener('change',filter));catalog.querySelector('[data-clear-filters]')?.addEventListener('click',()=>{search.value='';selects.forEach(s=>s.value='');filter();search.focus();});filter();
});
if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>entries.forEach(entry=>entry.target.classList.toggle('motion-out-of-view',!entry.isIntersecting)),{rootMargin:'80px'});document.querySelectorAll('.hero-art,.page-illustration,.quran-stage,.lesson-teaser-art').forEach(node=>observer.observe(node));}
document.addEventListener('visibilitychange',()=>document.documentElement.classList.toggle('tab-inactive',document.hidden));
document.querySelector('[data-motion-global]')?.addEventListener('click',event=>{const label=event.currentTarget.getAttribute('aria-pressed')==='true'?'Resume animations':'Pause animations';event.currentTarget.setAttribute('aria-label',label);event.currentTarget.title=label;});
const lesson=document.querySelector('[data-lesson]');
if(lesson){
 const topics={maths:{title:'A percentage is a part of 100.',explanation:'25% is one quarter. Divide the whole into four equal parts, then take one of them.',diagram:'<div class="fraction-blocks"><span>20</span><span>20</span><span>20</span><span>20</span></div><strong>80 ÷ 4 = 20</strong><span>One of four equal parts · 25% of 80</span>',questions:[{q:'What is 25% of 80?',options:['10','20','40'],answer:1,why:'25% = ¼. Divide 80 by 4 to get 20.'},{q:'What is 50% of 60?',options:['15','30','50'],answer:1,why:'50% is one half. Half of 60 is 30.'},{q:'A £40 book has a 25% discount. What is the new price?',options:['£10','£25','£30'],answer:2,why:'A quarter of £40 is £10. Subtract the £10 discount from £40 to get £30.'}]},science:{title:'A force can change motion.',explanation:'For a constant mass, resultant force = mass × acceleration. Use kilograms for mass and metres per second squared for acceleration.',diagram:'<div class="force-model"><div class="force-cube">2<span>kg</span></div><div class="force-vector"><i></i><strong>3 m/s²</strong></div></div><strong>F = 2 × 3 = 6 N</strong><span>Resultant force · mass × acceleration</span>',questions:[{q:'A 2 kg object accelerates at 3 m/s². What is the resultant force?',options:['1.5 N','5 N','6 N'],answer:2,why:'F = ma = 2 × 3 = 6 newtons.'},{q:'A resultant force of 12 N acts on a 4 kg object. What is its acceleration?',options:['3 m/s²','8 m/s²','48 m/s²'],answer:0,why:'Rearrange F = ma to a = F ÷ m. 12 ÷ 4 = 3 m/s².'},{q:'At the same mass, doubling the resultant force does what to acceleration?',options:['Halves it','Doubles it','Leaves it unchanged'],answer:1,why:'Since a = F ÷ m, doubling the resultant force at a fixed mass doubles the acceleration.'}]}};
 let topic='maths',index=0,correct=0,answered=false;const form=lesson.querySelector('[data-lesson-form]'),feedback=lesson.querySelector('[data-lesson-feedback]'),question=lesson.querySelector('[data-lesson-question]'),next=lesson.querySelector('[data-lesson-next]'),reset=lesson.querySelector('[data-lesson-reset]'),submit=form.querySelector('[type=submit]');question.tabIndex=-1;
 const render=()=>{const data=topics[topic],q=data.questions[index];answered=false;lesson.querySelector('[data-lesson-diagram]').innerHTML=data.diagram;lesson.querySelector('[data-lesson-kicker]').textContent=topic==='maths'?'MATHS · PERCENTAGES':'SCIENCE · NEWTON’S SECOND LAW';lesson.querySelector('[data-lesson-title]').textContent=data.title;lesson.querySelector('[data-lesson-explanation]').textContent=data.explanation;question.textContent=q.q;const options=lesson.querySelector('[data-lesson-options]');options.replaceChildren();q.options.forEach((text,i)=>{const label=document.createElement('label'),input=document.createElement('input'),span=document.createElement('span');input.type='radio';input.name='answer';input.value=String(i);input.required=true;span.textContent=text;label.append(input,span);options.append(label);});feedback.textContent='';feedback.className='lesson-feedback';next.hidden=true;reset.hidden=true;submit.hidden=false;submit.disabled=false;lesson.querySelector('[data-lesson-count]').textContent=`Question ${index+1} of 3`;};
 lesson.querySelectorAll('[data-topic]').forEach(button=>button.addEventListener('click',()=>{topic=button.dataset.topic;index=0;correct=0;lesson.querySelectorAll('[data-topic]').forEach(item=>item.setAttribute('aria-pressed',String(item===button)));render();}));
 form.addEventListener('submit',event=>{event.preventDefault();if(answered)return;const selected=form.querySelector('input:checked');if(!selected){form.reportValidity();return;}answered=true;const q=topics[topic].questions[index],right=Number(selected.value)===q.answer;if(right)correct++;feedback.textContent=(right?'That’s right. ':'Let’s work through it. ')+q.why;feedback.classList.add(right?'correct':'explain');form.querySelectorAll('input').forEach(i=>i.disabled=true);submit.hidden=true;submit.disabled=true;if(index<2)next.hidden=false;else{reset.hidden=false;lesson.querySelector('[data-lesson-count]').textContent=`Activity complete · ${correct} of 3 correct on the first try. Revisit any explanation you need.`;}});
 next.addEventListener('click',()=>{index++;render();question.focus();});reset.addEventListener('click',()=>{index=0;correct=0;render();question.focus();});render();
}
const booking=document.querySelector('#demo-form');
if(booking){
 const steps=[...booking.querySelectorAll('[data-booking-step]')],f=booking.elements,back=booking.querySelector('[data-booking-back]'),next=booking.querySelector('[data-booking-next]'),submit=booking.querySelector('[data-booking-submit]'),error=booking.querySelector('[data-booking-error]'),confirmation=document.querySelector('#confirmation'),summary=document.querySelector('#request-summary'),notice=document.querySelector('[data-intake-notice]'),query=new URLSearchParams(location.search);
 let step=0,pending=false,sent=false,config={live:false},copyText='',requestId=crypto.randomUUID();booking.addEventListener('input',()=>{requestId=crypto.randomUUID();});
 const showStep=(value,focus=true)=>{step=value;steps.forEach((s,i)=>s.hidden=i!==step);booking.querySelectorAll('.booking-progress li').forEach((li,i)=>{if(i===step)li.setAttribute('aria-current','step');else li.removeAttribute('aria-current');});booking.querySelector('[data-booking-progress]').textContent=`Step ${step+1} of 3`;back.hidden=step===0;next.hidden=step===2;submit.hidden=step!==2;error.textContent='';if(focus){const legend=steps[step].querySelector('legend');legend.tabIndex=-1;legend.focus();}};
 const validStep=index=>{for(const field of steps[index].querySelectorAll('input,select,textarea')){if(field===f.phone){const digits=field.value.replace(/\D/g,'');field.setCustomValidity(digits.length>=7&&digits.length<=15?'':'Enter a phone number with 7 to 15 digits.');}if(!field.checkValidity()){if(index!==step)showStep(index,false);field.reportValidity();field.focus();return false;}}return true;};
 next.addEventListener('click',()=>{if(validStep(step))showStep(step+1);});back.addEventListener('click',()=>showStep(Math.max(0,step-1)));booking.addEventListener('keydown',event=>{if(event.key==='Enter'&&event.target.tagName==='INPUT'&&step<2){event.preventDefault();next.click();}});
 const defaults={uk:'Europe/London',ireland:'Europe/Dublin',pakistan:'Asia/Karachi','new-zealand':'Pacific/Auckland',uae:'Asia/Dubai','saudi-arabia':'Asia/Riyadh',qatar:'Asia/Qatar',oman:'Asia/Muscat','other-countries':'other',other:'other'};const detected=Intl.DateTimeFormat().resolvedOptions().timeZone;
 const syncCountry=()=>{f.code.value=f.country.selectedOptions[0]?.dataset.code||(f.country.value?'other':'');const o=[...f.timezone.options].find(o=>o.value===detected);const match=(f.country.value==='usa'&&o?.textContent.startsWith('US ·'))||(f.country.value==='canada'&&o?.textContent.startsWith('Canada ·'))||(f.country.value==='australia'&&o?.textContent.startsWith('Australia ·'));f.timezone.value=match?detected:defaults[f.country.value]||'';};
 ['country','course','plan'].forEach(key=>{const value=query.get(key);if(value&&[...f[key].options].some(o=>o.value===value))f[key].value=value;});['level','curriculum','goal','time'].forEach(key=>{if(query.get(key))f[key].value=query.get(key).slice(0,f[key].maxLength);});syncCountry();f.country.addEventListener('change',syncCountry);f.phone.addEventListener('input',()=>f.phone.setCustomValidity(''));
 const configReady=fetch(new URL('intake-config.json',document.querySelector('script[src*="enhancements.js"]').src),{credentials:'same-origin'}).then(r=>{if(!r.ok)throw new Error();return r.json();}).then(value=>{if(value.live&&/^https:\/\//.test(value.endpoint)&&value.email&&value.provider&&value.providerPrivacy){config=value;notice.replaceChildren();const strong=document.createElement('strong'),link=document.createElement('a');strong.textContent='Your enquiry goes to '+value.email+'. ';link.href=value.providerPrivacy;link.textContent=value.provider+' privacy information';link.rel='noopener';link.target='_blank';notice.append(strong,'Details are sent through '+value.provider+'. ',link);submit.textContent='Send demo enquiry';}}).catch(()=>{notice.textContent='Preview mode. Use sample details. Sending is unavailable while the admissions connection is being configured.';});
 const values=()=>[['Parent or guardian',f.name.value.trim()],['Email',f.email.value.trim()],['Phone',`${f.code.value} ${f.phone.value.trim()}`],['Subject',f.course.selectedOptions[0].textContent],['School stage',f.level.value.trim()],['Curriculum',f.curriculum.value.trim()||'To discuss'],['Plan',f.plan.value||'To discuss'],['Country',f.country.selectedOptions[0].textContent],['Time zone',f.timezone.selectedOptions[0].textContent],['Availability',f.time.value.trim()||'To discuss'],['Learning goal',f.goal.value.trim()||'To discuss']];
 const showSummary=reference=>{summary.replaceChildren();const entries=values();copyText=entries.map(([k,v])=>`${k}: ${v}`).join('\n');entries.forEach(([k,v])=>{const dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=k;dd.textContent=v;summary.append(dt,dd);});document.querySelector('[data-confirmation-title]').textContent=sent?'Your enquiry has been received.':'Your sample enquiry';document.querySelector('[data-confirmation-copy]').textContent=sent?'Admissions will review your request. A demo is booked only when a time is confirmed.'+(reference?' Reference: '+reference:''):'Review the details. This preview has not sent a request or booked a demo.';confirmation.querySelector('[data-edit]').hidden=sent;booking.hidden=true;confirmation.hidden=false;confirmation.focus();};
 const copyDetails=async(text,status)=>{try{await navigator.clipboard.writeText(text);status.textContent='Enquiry copied. No additional request was sent.';}catch{status.textContent='Copy is unavailable in this browser. Select the visible summary to copy it manually.';}};
 booking.addEventListener('submit',async event=>{event.preventDefault();if(pending||sent)return;for(let i=0;i<3;i++)if(!validStep(i))return;if(f.website.value){error.textContent='Unable to submit this request. Please reload the page and try again.';return;}pending=true;submit.disabled=true;submit.textContent='Checking your enquiry…';error.textContent='';try{await configReady;if(!config.live){showSummary();return;}const payload=Object.fromEntries(new FormData(booking));delete payload.website;payload.consent=true;payload.source='Future Cloud Campus';payload.requestId=requestId;payload.submittedAt=new Date().toISOString();const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),15000);let response;try{response=await fetch(config.endpoint,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(payload),signal:controller.signal,credentials:'omit'});}finally{clearTimeout(timer);}let result;try{result=await response.json();}catch{throw new Error('unconfirmed');}if(!response.ok||result.ok!==true)throw new Error('unconfirmed');sent=true;showSummary(typeof result.reference==='string'?result.reference.slice(0,100):'');}catch{error.textContent='We could not confirm receipt of your enquiry. Your details are still here. Please try again, or copy them to contact admissions directly.';if(!booking.querySelector('[data-copy-failed]')){const copy=document.createElement('button');copy.type='button';copy.className='btn secondary';copy.dataset.copyFailed='';copy.textContent='Copy enquiry details';copy.addEventListener('click',()=>copyDetails(values().map(([k,v])=>`${k}: ${v}`).join('\n'),error));error.after(copy);}}finally{pending=false;submit.disabled=false;submit.textContent=config.live?'Send demo enquiry':'Review sample enquiry';}});
 confirmation.querySelector('[data-edit]').addEventListener('click',()=>{confirmation.hidden=true;booking.hidden=false;showStep(0);});confirmation.querySelector('[data-copy-enquiry]').addEventListener('click',()=>copyDetails(copyText,confirmation.querySelector('[data-copy-status]')));showStep(0,false);
}

// Independent example currencies; these numbers are not live offers or FX rates.
document.querySelectorAll('[data-sample-pricing]').forEach(section=>{
 const data=JSON.parse(section.querySelector('[data-sample-data]').textContent);
 const select=section.querySelector('[data-sample-market]');
 const incoming=new URLSearchParams(location.search).get('country');
 const initial=data.markets.find(m=>m.slug===incoming);if(initial)select.value=initial.currency;
 const format=(n,c)=>new Intl.NumberFormat('en-GB',{style:'currency',currency:c,maximumFractionDigits:0}).format(n);
 const render=()=>{
  const market=data.markets.find(m=>m.currency===select.value);if(!market)return;
  section.querySelectorAll('[data-sample-card]').forEach(card=>{
   const index=Number(card.dataset.sampleCard),count=[4,8,12][index],rate=market.rates?.[index];
   card.querySelector('[data-sample-rate]').textContent=Number.isFinite(rate)?format(rate,market.currency):'Personal quote';
   card.querySelector('[data-sample-currency-label]').textContent=market.rates?market.currency:'To discuss';
   card.querySelector('.sample-unit').hidden=!market.rates;
   card.querySelector('[data-sample-total]').textContent=Number.isFinite(rate)?format(rate*count,market.currency):'To discuss';
   card.querySelector('.sample-total>span').textContent=market.rates?'sample four-week total':'Fees confirmed after discussing your needs';
   const link=card.querySelector('[data-sample-enquiry]'),url=new URL(link.href);
   url.searchParams.set('country',market.slug);url.searchParams.set('plan',link.dataset.plan);
   url.searchParams.set('goal',`Illustrative plan: ${count} lessons over four weeks${market.rates?`, ${format(rate,market.currency)} per lesson and ${format(rate*count,market.currency)} sample total`:''}. Please confirm actual fees and lesson duration.`);
   link.href=url.href;
  });
  const custom=document.querySelector('[data-sample-custom]');if(custom){const url=new URL(custom.href);url.searchParams.set('country',market.slug);custom.href=url.href;}
  section.querySelector('[data-sample-status]').textContent=market.rates?`Showing illustrative ${market.currency} prices for ${market.country}.`:`No example prices are published for ${market.country}. Request a personal quote.`;
 };
 select.addEventListener('change',render);render();
});

// User-controlled review carousel. Native overflow remains usable without JS.
document.querySelectorAll('[data-review-carousel]').forEach(carousel=>{
 const track=carousel.querySelector('[data-review-track]');
 const cards=[...track.children];
 const controls=carousel.querySelector('[data-review-controls]');
 const previous=carousel.querySelector('[data-review-prev]');
 const next=carousel.querySelector('[data-review-next]');
 const status=carousel.querySelector('[data-review-status]');
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let frame=0,settle=0,targetIndex=null;
 const metrics=()=>{
  const gap=parseFloat(getComputedStyle(track).columnGap)||0;
  const step=(cards[0]?.getBoundingClientRect().width||track.clientWidth)+gap;
  const visible=Math.min(cards.length,Math.max(1,Math.floor((track.clientWidth+gap)/step)));
  const start=Math.max(0,Math.min(cards.length-visible,Math.round(track.scrollLeft/step)));
  return{step,visible,start,max:Math.max(0,track.scrollWidth-track.clientWidth)};
 };
 const paint=()=>{
  frame=0;const m=metrics();controls.hidden=m.max<2;
  previous.disabled=track.scrollLeft<2;next.disabled=track.scrollLeft>=m.max-2;
 };
 const announce=()=>{
  const m=metrics(),end=Math.min(cards.length,m.start+m.visible);
  const type=carousel.dataset.reviewSample==='true'?'Examples':'Reviews';
  status.textContent=`${type} ${m.start+1}${end>m.start+1?'–'+end:''} of ${cards.length}`;
 };
 const go=index=>{
  const m=metrics();targetIndex=Math.max(0,Math.min(cards.length-m.visible,index));
  const left=Math.min(m.max,targetIndex*m.step);
  track.scrollTo({left,behavior:reduced.matches||document.documentElement.classList.contains('motion-paused')?'auto':'smooth'});
 };
 previous.addEventListener('click',()=>go((targetIndex??metrics().start)-1));
 next.addEventListener('click',()=>go((targetIndex??metrics().start)+1));
 track.addEventListener('keydown',event=>{
  if(event.target!==track)return;
  if(['ArrowLeft','ArrowRight','Home','End'].includes(event.key)){
   event.preventDefault();
   const current=targetIndex??metrics().start;
   go(event.key==='Home'?0:event.key==='End'?cards.length-1:current+(event.key==='ArrowRight'?1:-1));
  }
 });
 const manual=()=>{targetIndex=null;};
 track.addEventListener('pointerdown',manual,{passive:true});
 track.addEventListener('wheel',manual,{passive:true});
 track.addEventListener('scroll',()=>{
  if(!frame)frame=requestAnimationFrame(paint);
  clearTimeout(settle);settle=setTimeout(()=>{targetIndex=null;paint();announce();},140);
 },{passive:true});
 if('ResizeObserver' in window)new ResizeObserver(()=>{targetIndex=null;paint();announce();}).observe(track);
 else window.addEventListener('resize',()=>{paint();announce();},{passive:true});
 paint();announce();
});

// Contact enquiries: validate, review, edit and copy locally until a verified receiver is configured.
document.querySelectorAll('[data-contact-form]').forEach(form=>{
 const wrap=form.parentElement,summary=wrap.querySelector('[data-contact-summary]'),details=summary.querySelector('[data-contact-details]'),error=form.querySelector('[data-contact-error]'),submit=form.querySelector('[data-contact-submit]'),notice=document.querySelector('[data-contact-notice]');
 const status=summary.querySelector('[data-contact-status]');let config={contactLive:false},pending=false,sent=false,text='';
 const configReady=fetch(new URL('intake-config.json',document.querySelector('script[src*="enhancements.js"]').src),{credentials:'same-origin'}).then(response=>{if(!response.ok)throw Error();return response.json();}).then(value=>{
  if(value.contactLive&&/^https:\/\//.test(value.contactEndpoint)&&value.email&&value.provider&&/^https:\/\//.test(value.providerPrivacy)){
   config=value;notice.replaceChildren();const heading=document.createElement('strong'),copy=document.createElement('p'),link=document.createElement('a');heading.textContent='Contact admissions';copy.textContent=`Your enquiry goes to ${value.email} through ${value.provider}. `;link.href=value.providerPrivacy;link.target='_blank';link.rel='noopener noreferrer';link.textContent='Provider privacy information';copy.append(link);notice.append(heading,copy);submit.textContent='Send enquiry';
  }
 }).catch(()=>{});
 form.elements.message.addEventListener('input',()=>form.elements.message.setCustomValidity(''));
 const entries=()=>[['Name',form.elements.name.value.trim()],['Email',form.elements.email.value.trim()],['Phone',form.elements.phone.value.trim()||'Not provided'],['Topic',form.elements.topic.value],['Message',form.elements.message.value.trim()]];
 const review=reference=>{
  const values=entries();text=values.map(([key,value])=>`${key}: ${value}`).join('\n');details.replaceChildren();
  values.forEach(([key,value])=>{const dt=document.createElement('dt'),dd=document.createElement('dd');dt.textContent=key;dd.textContent=value;details.append(dt,dd);});
  summary.querySelector('[data-contact-summary-title]').textContent=sent?'Your enquiry has been received.':'Ready to review.';
  summary.querySelector('[data-contact-summary-note]').textContent=sent?'Admissions will review your message.'+(reference?` Reference: ${reference}`:''):'Your message has not been sent. You can edit or copy these details.';
  summary.querySelector('[data-contact-edit]').hidden=sent;status.textContent='';form.hidden=true;summary.hidden=false;summary.focus();
 };
 form.addEventListener('submit',async event=>{
  event.preventDefault();if(pending||sent)return;error.textContent='';
  for(const field of form.querySelectorAll('[required]')){if(typeof field.value==='string'&&field.type!=='checkbox')field.value=field.value.trim();if(field.name==='message')field.setCustomValidity(field.value.length>=10?'':'Please write at least 10 characters.');if(!field.checkValidity()){field.reportValidity();field.focus();return;}}
  if(form.elements.website.value){error.textContent='Unable to process this enquiry. Please reload and try again.';return;}
  pending=true;submit.disabled=true;submit.textContent='Checking enquiry…';
  try{
   await configReady;if(!config.contactLive){review();return;}
   const payload=Object.fromEntries(new FormData(form));delete payload.website;payload.consent=true;payload.type='contact';payload.source='Future Cloud Campus';payload.requestId=crypto.randomUUID();payload.submittedAt=new Date().toISOString();
   const controller=new AbortController(),timeout=setTimeout(()=>controller.abort(),15000);let response;
   try{response=await fetch(config.contactEndpoint,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(payload),signal:controller.signal,credentials:'omit'});}finally{clearTimeout(timeout);}
   const result=await response.json();if(!response.ok||result.ok!==true)throw Error('Receipt unconfirmed');sent=true;review(typeof result.reference==='string'?result.reference.slice(0,100):'');
  }catch{error.textContent='We could not confirm receipt. Your details are still here; please try again.';}
  finally{pending=false;submit.disabled=false;submit.textContent=config.contactLive?'Send enquiry':'Review enquiry';}
 });
 summary.querySelector('[data-contact-edit]').addEventListener('click',()=>{summary.hidden=true;form.hidden=false;form.elements.name.focus();});
 summary.querySelector('[data-contact-copy]').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(text);status.textContent='Enquiry copied. No additional message was sent.';}catch{status.textContent='Select the visible details to copy them manually.';}});
});
