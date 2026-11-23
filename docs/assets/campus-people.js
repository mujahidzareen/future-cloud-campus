'use strict';
document.querySelectorAll('[data-faculty-directory]').forEach(directory=>{
 const controls=directory.querySelector('[data-faculty-filters]');if(!controls)return;
 const search=directory.querySelector('[data-faculty-search]'),stage=directory.querySelector('[data-faculty-stage]'),cards=[...directory.querySelectorAll('[data-faculty-card]')],count=directory.querySelector('[data-faculty-count]'),empty=directory.querySelector('[data-faculty-empty]');
 controls.hidden=false;
 const filter=()=>{const words=search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);let visible=0;cards.forEach(card=>{const text=card.textContent.toLowerCase(),match=words.every(word=>text.includes(word))&&(!stage.value||card.dataset.stages.split(' ').includes(stage.value));card.hidden=!match;if(match){visible++;card.classList.add('is-revealed');}});count.textContent=`${visible} of ${cards.length} illustrative profiles`;empty.hidden=visible!==0;};
 search.addEventListener('input',filter);stage.addEventListener('change',filter);directory.querySelector('[data-faculty-reset]').addEventListener('click',()=>{search.value='';stage.value='';filter();search.focus();});
});
