'use strict';
document.querySelectorAll('[data-faculty-directory]').forEach(directory=>{
 const controls=directory.querySelector('[data-faculty-filters]');if(!controls)return;
 const search=directory.querySelector('[data-faculty-search]'),stage=directory.querySelector('[data-faculty-stage]'),cards=[...directory.querySelectorAll('[data-faculty-card]')],count=directory.querySelector('[data-faculty-count]'),empty=directory.querySelector('[data-faculty-empty]');
 const dialog=directory.querySelector('[data-faculty-dialog]');
 if(dialog&&typeof dialog.showModal==='function'){
  const content=dialog.querySelector('[data-profile-content]'),close=dialog.querySelector('[data-profile-close]');
  const profiles=new Map([...directory.querySelectorAll('[data-profile-template]')].map(template=>[template.dataset.profileTemplate,template]));
  let opener=null;
  directory.querySelectorAll('[data-profile-open]').forEach(button=>{
   if(!profiles.has(button.dataset.profileOpen))return;
   button.hidden=false;
   button.addEventListener('click',()=>{
    opener=button;
    content.replaceChildren(profiles.get(button.dataset.profileOpen).content.cloneNode(true));
    document.documentElement.classList.add('faculty-modal-open');
    dialog.showModal();content.scrollTop=0;close.focus({preventScroll:true});
   });
  });
  close.addEventListener('click',()=>dialog.close());
  dialog.addEventListener('keydown',event=>{
   if(event.key!=='Tab')return;
   const focusable=[...dialog.querySelectorAll('button,a[href]')],first=focusable[0],last=focusable[focusable.length-1];
   if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus();}
   else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}
  });
  dialog.addEventListener('click',event=>{
   if(event.target!==dialog)return;
   const rect=dialog.getBoundingClientRect();
   if(event.clientX<rect.left||event.clientX>rect.right||event.clientY<rect.top||event.clientY>rect.bottom)dialog.close();
  });
  dialog.addEventListener('close',()=>{
   document.documentElement.classList.remove('faculty-modal-open');
   opener?.focus({preventScroll:true});
  });
  window.addEventListener('pagehide',()=>{if(dialog.open)dialog.close();});
 }
 controls.hidden=false;
 const filter=()=>{const words=search.value.toLowerCase().trim().split(/\s+/).filter(Boolean);let visible=0;cards.forEach(card=>{const text=(card.dataset.profileSearch||card.textContent).toLowerCase(),match=words.every(word=>text.includes(word))&&(!stage.value||card.dataset.stages.split(' ').includes(stage.value));card.hidden=!match;if(match){visible++;card.classList.add('is-revealed');}});count.textContent=`${visible} of ${cards.length} illustrative profiles`;empty.hidden=visible!==0;};
 search.addEventListener('input',filter);stage.addEventListener('change',filter);directory.querySelector('[data-faculty-reset]').addEventListener('click',()=>{search.value='';stage.value='';filter();search.focus();});
});
