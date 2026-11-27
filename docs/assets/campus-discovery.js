'use strict';
// Progressive enhancement: the stage finder is a regular GET form without JavaScript.
document.querySelectorAll('[data-stage-finder]').forEach(form=>{
 const hints={'Primary':'Build reading, number and learning foundations.','Middle school':'Connect subject ideas and develop useful study habits.','Secondary':'Strengthen concepts and practise your school course.','Higher secondary':'Go deeper with your exact advanced school course.'};
 const paint=()=>{const value=form.elements.stage.value;form.querySelector('[data-stage-hint]').textContent=hints[value];const button=form.querySelector('[type="submit"]');button.replaceChildren(`Explore ${value} `);const arrow=document.createElement('span');arrow.setAttribute('aria-hidden','true');arrow.textContent='↗';button.append(arrow);};
 form.addEventListener('change',paint);paint();
});
// An original learning example, with real feedback and no remote requests.
document.querySelectorAll('[data-lesson-peek]').forEach(lab=>{
 const tabs=[...lab.querySelectorAll('[data-peek-tab]')],panels=[...lab.querySelectorAll('[data-peek-panel]')],answers=[...lab.querySelectorAll('[data-peek-answer]')],feedback=lab.querySelector('[data-peek-feedback]'),reset=lab.querySelector('[data-peek-reset]');
 lab.querySelector('[role="tablist"]').hidden=false;
 const show=(key,focus=false)=>{tabs.forEach(tab=>{const selected=tab.dataset.peekTab===key;tab.setAttribute('aria-selected',String(selected));tab.tabIndex=selected?0:-1;if(selected&&focus)tab.focus();});panels.forEach(panel=>panel.hidden=panel.dataset.peekPanel!==key);};
 tabs.forEach((tab,i)=>{tab.addEventListener('click',()=>show(tab.dataset.peekTab));tab.addEventListener('keydown',event=>{const keys=['ArrowLeft','ArrowRight','Home','End'];if(!keys.includes(event.key))return;event.preventDefault();const index=event.key==='Home'?0:event.key==='End'?tabs.length-1:(i+(event.key==='ArrowRight'?1:-1)+tabs.length)%tabs.length;show(tabs[index].dataset.peekTab,true);});});
 answers.forEach(answer=>answer.addEventListener('click',()=>{const right=answer.dataset.peekAnswer==='20';answers.forEach(button=>{button.setAttribute('aria-pressed',String(button===answer));button.classList.toggle('is-correct',button===answer&&right);});feedback.textContent=right?'That’s right. 25% is one quarter: 80 ÷ 4 = 20.':'Let’s break it down. 25% is one quarter, so divide 80 by 4. That gives 20.';feedback.classList.toggle('is-correct',right);reset.hidden=false;}));
 reset.addEventListener('click',()=>{answers.forEach(button=>{button.removeAttribute('aria-pressed');button.classList.remove('is-correct');});feedback.textContent='Think about one of four equal groups.';feedback.classList.remove('is-correct');reset.hidden=true;answers[0].focus();});show('explain');
});
